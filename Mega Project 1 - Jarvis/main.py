import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  # Make sure this exists with a 'music' dict
import requests
import os
from gtts import gTTS
import pygame
from openai import OpenAI

# Initialize components once
recognizer = sr.Recognizer()
pygame.mixer.init()

# Load API keys securely from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")

# Use gTTS for speaking
def speak(text):
    try:
        tts = gTTS(text)
        tts.save('temp.mp3')
        pygame.mixer.music.load('temp.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        os.remove("temp.mp3")
    except Exception as e:
        print(f"Speech Error: {e}")

# Process GPT command
def aiProcess(command):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. Give short responses."},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return "Sorry, I couldn't process that."

# Handle command logic
def processCommand(command):
    c = command.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        link = musicLibrary.music.get(song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found in the music library.")
    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
            if r.status_code == 200:
                articles = r.json().get('articles', [])
                if not articles:
                    speak("No news found.")
                for article in articles[:5]:  # Limit to top 5
                    speak(article['title'])
            else:
                speak("Failed to get news.")
        except Exception as e:
            print(f"News API Error: {e}")
            speak("Sorry, I couldn't get the news.")
    elif "shutdown" in c or "exit" in c:
        speak("Shutting down. Goodbye!")
        exit()
    else:
        # Fallback to OpenAI GPT
        response = aiProcess(command)
        speak(response)

# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis.")
    while True:
        try:
            print("Listening for wake word...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            wake_word = recognizer.recognize_google(audio)
            if wake_word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
