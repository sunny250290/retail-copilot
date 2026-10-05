from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

prompt = "Suggest one name for a new electronics shop. Reply with only the name."

for temp in [0, 1]:
    print(f"\nTemperature {temp}:")
    for attempt in range(3):          # ask the same question 3 times
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=20,
            extra_body={"temperature": temp},   # new way to pass temperature
            messages=[{"role": "user", "content": prompt}],
        )
        print(" -", response.content[0].text)