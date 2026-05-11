import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
 
const client = new Anthropic();
 
const msg = await client.messages.create({
  model: "claude-haiku-4-5",
  max_tokens: 256,
  messages: [{ role: "user", content: "What is the Claude API?" }],
});
 
console.log(msg.content[0].text);
