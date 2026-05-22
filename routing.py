import anthropic, random, time, json, logging
from dotenv import load_dotenv
load_dotenv()

log = logging.getLogger(__name__)
client = anthropic.Anthropic()

CASCADE = ['claude-haiku-4-5', 'claude-sonnet-4-5', 'claude-opus-4-5']

def ask_with_fallback(prompt):
    for model in CASCADE:
        try:
            msg = client.messages.create(
                model=model, max_tokens=256,
                messages=[{'role': 'user', 'content': prompt}]
            )
            if model != CASCADE[0]:
                log.warning(f'Fell back to {model}')
            return msg.content[0].text
        except anthropic.APIStatusError:
            if model == CASCADE[-1]:
                raise
            time.sleep(1)

AB = {'control': 'claude-haiku-4-5', 'treatment': 'claude-sonnet-4-5'}

def ask_ab(request_id, prompt):
    variant = random.choice(list(AB))
    t0 = time.time()
    msg = client.messages.create(
        model=AB[variant], max_tokens=256,
        messages=[{'role': 'user', 'content': prompt}]
    )
    log.info(json.dumps({
        'id': request_id, 'variant': variant, 'model': AB[variant],
        'ms': int((time.time()-t0)*1000),
        'in': msg.usage.input_tokens, 'out': msg.usage.output_tokens
    }))
    return msg.content[0].text

logging.basicConfig(level=logging.INFO)

print(ask_with_fallback('What is 2 + 2?'))
print(ask_ab('req-001', 'What is 2 + 2?'))
