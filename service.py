import anthropic, hashlib
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
cache: dict = {}

def ask(prompt: str) -> str:
    key = hashlib.md5(prompt.encode()).hexdigest()
    if key in cache:
        return cache[key]
    msg = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    print(msg)
    cache[key] = msg.content[0].text
    return cache[key]

print("First call (hits Claude):")
print(ask("What is 2+2?"))

print("\nSecond call (from cache):")
print(ask("What is 2+2?"))