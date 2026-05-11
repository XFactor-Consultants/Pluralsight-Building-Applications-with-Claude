import anthropic
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
client = anthropic.AsyncAnthropic()

async def ask_claude(prompt: str) -> str:
    msg = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    return msg.content[0].text

@app.post("/summarize")
async def summarize(text: str):
    result = await ask_claude(f"Summarize this:\n\n{text}")
    return {"summary": result}