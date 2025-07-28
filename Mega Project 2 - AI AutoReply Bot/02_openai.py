from openai import OpenAI


# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<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>",
)

command = '''
[12:48 am, 9/9/2024] Iam_patel14: hi
[12:48 am, 9/9/2024] Sumit Luli👥: Hi
[12:49 am, 9/9/2024] Iam_patel14: lolu
[12:49 am, 9/9/2024] Sumit Luli👥: Bol
[12:50 am, 9/9/2024] Sumit Luli👥: Su key
[12:52 am, 9/9/2024] Iam_patel14: hi
[12:52 am, 9/9/2024] Iam_patel14: kon che
[12:52 am, 9/9/2024] Iam_patel14: story par
[12:52 am, 9/9/2024] Sumit Luli👥: Ben
[2:58 pm, 11/9/2024] Iam_patel14: hi
[2:58 pm, 11/9/2024] Sumit Luli👥: Hi
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Iam_patel14 who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Iam_patel14"},
    {"role": "user", "content": command}
  ]
)


print(completion.choices[0].message.content)