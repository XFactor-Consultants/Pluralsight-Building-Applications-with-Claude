import anthropic
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Anthropic()
 
msg = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "What is the Claude API?"}]
 )
  
print(msg.content[0].text)
