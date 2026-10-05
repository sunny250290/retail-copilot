from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

texts = [
    "late",
    "unbelievably",
    "The parcel arrived unbelievably late!",
    "पार्सल बहुत देर से आया!",   # the same idea in Hindi
]

for text in texts:
    count = client.messages.count_tokens(
        model="claude-haiku-4-5",
        messages=[{"role": "user", "content": text}],
    )
    print(f"{count.input_tokens:>4} tokens  <-  {text}")