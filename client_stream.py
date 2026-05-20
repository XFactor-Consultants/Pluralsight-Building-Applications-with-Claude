import anthropic
from dotenv import load_dotenv
load_dotenv()


client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-haiku-4-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "Count to 10."}]
) as stream:
    for chunk in stream.text_stream:
        print(chunk, end="", flush=True)

