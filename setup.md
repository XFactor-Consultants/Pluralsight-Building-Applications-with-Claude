# Module 1 — Setup Guide

## Prerequisites

- Python 3 installed (`python3 --version`)
- Node.js installed (`node --version`)
- An Anthropic API key — get one at [console.anthropic.com](https://console.anthropic.com)

---

## 1. Get Your API Key

1. Go to **console.anthropic.com** and sign in
2. Click **API Keys** in the left sidebar
3. Click **Create Key**, give it a name (e.g. `pluralsight-building-applications-claude`)
4. Copy the key — it starts with `sk-ant-`
5. You won't see it again after closing the dialog, so copy it now

---

## 2. Python Setup

```bash
cd module1/python

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**requirements.txt**
```
anthropic
python-dotenv
fastapi
uvicorn
```

### Set your API key

```bash
touch .env
nano .env
```

Add this line (replace with your real key):
```
ANTHROPIC_API_KEY=sk-ant-xxxxxx
```

Save and exit: `Ctrl+O` → `Enter` → `Ctrl+X`

Verify it looks right:
```bash
cat .env
```

### Test Python setup

```bash
python3 first_call.py
```

You should see a response about the Claude API. If you see `AuthenticationError`, open `.env` and check for typos or extra spaces around the key.

---

## 3. TypeScript Setup

```bash
cd module1/typescript

# Install dependencies
npm install
```

**package.json**
```json
{
  "name": "claude-module1",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "first-call": "npx ts-node --esm firstCall.ts",
    "server": "npx ts-node --esm server.ts"
  },
  "dependencies": {
    "@anthropic-ai/sdk": "^0.39.0",
    "dotenv": "^16.0.0",
    "express": "^4.18.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.0",
    "@types/node": "^20.0.0",
    "ts-node": "^10.9.0",
    "typescript": "^5.0.0"
  }
}
```

### Set your API key

```bash
touch .env
nano .env
```

Add this line:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxx
```

Save and exit: `Ctrl+O` → `Enter` → `Ctrl+X`

### Test TypeScript setup

```bash
npx ts-node --esm firstCall.ts
```

You should see the same response as the Python version. If the script hangs, confirm `"type": "module"` is in `package.json` and `tsconfig.json` has `"module": "ESNext"`.

---

## 4. Common Errors

| Error | Fix |
|---|---|
| `zsh: command not found: python` | Use `python3` instead |
| `AuthenticationError` | Key missing or has extra whitespace in `.env` |
| `ts-node` hangs silently | Missing `"type": "module"` in `package.json` |
| FastAPI port conflict | `uvicorn main:app --port 8001` |
| Express port conflict | Change `app.listen(3000,...)` to `3001` |
| Lost your API key | Create a new one at console.anthropic.com — old ones can't be recovered |
