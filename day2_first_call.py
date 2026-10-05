from dotenv import load_dotenv
import anthropic

load_dotenv()                     # loads your key from .env
client = anthropic.Anthropic()    # finds ANTHROPIC_API_KEY automatically

response = client.messages.create(
    model="claude-haiku-4-5",     # the fast, cheap model
    max_tokens=300,               # maximum length of the answer
    messages=[
        {"role": "user",
         "content": "Summarise the main findings of the 2019 paper ""Banana Networks for Retail Forecasting"" by Dr. Elsa Moretti."}
    ],
)

print(response.content[0].text)   # the answer
print("---")
print("Input tokens: ", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)