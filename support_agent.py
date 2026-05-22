import anthropic, json
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

SYSTEM = """You are a customer support agent.
You must respond with valid JSON only. No markdown, no code fences, no explanation.
Exactly this structure:
{
    "intent": "billing | technical | other",
    "reply": "your response here",
    "escalate": true or false
}"""

def support(message, account):
    resp = client.messages.create(
        model='claude-haiku-4-5', max_tokens=256, system=SYSTEM,
        messages=[{'role': 'user', 'content': f'{message}\n\nAccount: {account}'}]
    )
    text = resp.content[0].text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    result = json.loads(text)
    if account.get('open_issues', 0) > 2:
        result['escalate'] = True
    return result

print(support('I was charged twice!', {'plan': 'pro', 'open_issues': 1}))