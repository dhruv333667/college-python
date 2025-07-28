import openai
import pyautogui
import time
import pyperclip
from openai import OpenAI
import os

# print(os.getenv('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'))


client = OpenAI(
  api_key="<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>",)

def is_last_message_from_sender(chat_log, sender_name="Sumit Luli👥"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("[2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
    pyautogui.click(802, 759)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(510,150)
    pyautogui.dragTo(1168, 661, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1994, 298)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Hi. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [12:52 am, 9/9/2024] Sumit Luli👥: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1808, 1328)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')

    