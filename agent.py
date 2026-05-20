import anthropic, json
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

tools = [{
    "name": "search",
    "description": "Search a product catalog. Returns a list of matching items.",
    "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
}]

def search(query):
    return [{"id": "A1", "name": "Widget", "price": 9.99}]

def run(user_message):
    messages = [{"role": "user", "content": user_message}]
    for _ in range(10):
        resp = client.messages.create(
            model="claude-haiku-4-5", max_tokens=512, tools=tools, messages=messages
        )
        if resp.stop_reason == "end_turn":
            return resp.content[0].text
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for b in resp.content:
            if b.type == "tool_use":
                try:
                    output = search(b.input["query"])
                    results.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(output)})
                except Exception as e:
                    results.append({"type": "tool_result", "tool_use_id": b.id, "content": f"Error: {e}"})
        messages.append({"role": "user", "content": results})
    return "Max iterations reached."

print(run("Find me a widget."))