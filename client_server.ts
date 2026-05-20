import Anthropic from "@anthropic-ai/sdk";
import express from "express";
import dotenv from "dotenv";
dotenv.config();

const app = express();
app.use(express.json());

const client = new Anthropic();

app.post("/stream", async (req, res) => {
  console.log("hit, message:", req.body.message);
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");

  try {
    const stream = await client.messages.create({
      model: "claude-haiku-4-5",
      max_tokens: 256,
      messages: [{ role: "user", content: req.body.message }],
      stream: true,
    });

    for await (const event of stream) {
      console.log("event:", event.type);
      if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
        res.write(`data: ${event.delta.text}\n\n`);
      }
    }
  } catch (err: any) {
    console.error("Stream error:", err);
  } finally {
    res.end();
  }
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));