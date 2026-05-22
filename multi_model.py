import anthropic
from dotenv import load_dotenv
from config import MODELS
load_dotenv()
client = anthropic.Anthropic()
def ask(task, prompt):
    cfg = MODELS[task]
    msg = client.messages.create(
        model=cfg['model'], max_tokens=cfg['max_tokens'],
        messages=[{'role': 'user', 'content': prompt}]
    )
    return msg.content[0].text

print(ask('classify', 'Classify: My invoice is wrong'))
print(ask('summarize', 'Summarize in one sentence: The global economy is shaped by trade, technology, labor markets, and monetary policy working together in complex ways.'))
print(ask('analyze',   'Analyze the main argument in one sentence: Democracy requires an informed citizenry, free press, and rule of law to function.'))