import anthropic
from datetime import date
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

tools = [{
    "name": "today",
    "description": "Returns today's date as YYYY-MM-DD.",
    "input_schema": {"type": "object", "properties": {}, "required": []}
}]

messages = [{"role": "user", "content": "What is today's date?"}]
resp = client.messages.create(model="claude-haiku-4-5", max_tokens=256, tools=tools, messages=messages)

tb = resp.content[0]
result = date.today().isoformat()

messages += [
    {"role": "assistant", "content": resp.content},
    {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tb.id, "content": result}]}
]

final = client.messages.create(model="claude-haiku-4-5", max_tokens=256, tools=tools, messages=messages)
print(final.content[0].text)
