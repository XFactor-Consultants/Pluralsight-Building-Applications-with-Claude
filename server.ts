import Anthropic from "@anthropic-ai/sdk";
import express from "express";
import "dotenv/config";

const app = express();
app.use(express.json());
const client = new Anthropic({ maxRetries: 3 });

async function askClaude(prompt: string): Promise<string> {
    const msg = await client.messages.create({
        model: "claude-haiku-4-5",
        max_tokens: 512,
        messages: [{ role: "user", content: prompt }],
    });
    return (msg.content[0] as any).text;
}

app.post("/summarize", async (req, res) => {
    const summary = await askClaude(`Summarize this:\n\n${req.body.text}`);
    res.json({ summary });
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));