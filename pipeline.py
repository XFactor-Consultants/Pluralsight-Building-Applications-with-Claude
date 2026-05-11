import asyncio, anthropic
from dotenv import load_dotenv
load_dotenv()

client = anthropic.AsyncAnthropic()

async def classify(text: str) -> str:
    msg = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=8,
        system="Reply with one word: positive, negative, or neutral.",
        messages=[{"role": "user", "content": text}]
    )
    return msg.content[0].text.strip()

async def run_batch(docs: list[str], limit: int = 5) -> list[str]:
    sem = asyncio.Semaphore(limit)
    async def bounded(doc):
        async with sem:
            return await classify(doc)
    return await asyncio.gather(*[bounded(d) for d in docs])

docs = ["Great product!", "Shipment was late.", "Item arrived fine."]
results = asyncio.run(run_batch(docs))
print(results)