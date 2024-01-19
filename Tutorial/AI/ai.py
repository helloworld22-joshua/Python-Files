# Do not name file "openai.py", leads to conflict!

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.environ.get("OPENAI_API_KEY"),         # Set environment variable in CMD: setx OPENAI_API_KEY “<yourkey>”
)

input = ""                                              # I have no idea if the code works since I ran out of tries

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            {"role": "system",
            "content": "Hello, World!"},
            {"role": "user",
            "content": f"Say {input}"}
        }
    ],
)

print(input)