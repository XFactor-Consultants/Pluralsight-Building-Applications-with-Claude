# Pluralsight Building Applications with Claude — Course Setup Guide

Everything you need to get your environment ready before the first lesson. The repo contains both Python and TypeScript examples — follow all steps below and you will have both runtimes, all dependencies, and a live Anthropic API key configured by the end.

---

## Prerequisites

Make sure the following are installed before you begin:

- **Python 3.9 or higher** — check with `python --version` or `python3 --version`
- **Node.js 18 or higher** — check with `node --version`. Download from [nodejs.org](https://nodejs.org) if needed
- **npm** — comes bundled with Node.js; confirm with `npm --version`
- **Git** — check with `git --version`. Download from [git-scm.com](https://git-scm.com) if needed
- **A code editor** — VS Code is recommended

---

## Step 1 — Clone the Repo

```bash
git clone https://github.com/XFactor-Consultants/Pluralsight-Building-Applications-with-Claude.git
cd Pluralsight-Building-Applications-with-Claude
```

All Python and TypeScript course files live at the root of this folder. Keep your terminal here for every step that follows.

---

## Step 2 — Create a Python Virtual Environment

A virtual environment keeps the Python dependencies for this course isolated from the rest of your system.

**macOS / Linux:**

```bash
python3 -m venv venv
```

**Windows:**

```bash
python -m venv venv
```

---

## Step 3 — Activate the Virtual Environment

You need to activate the virtual environment every time you open a new terminal session.

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows (Command Prompt):**

```bash
venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

Your prompt will show `(venv)` when the environment is active. To deactivate at any time:

```bash
deactivate
```

---

## Step 4 — Install Python Dependencies

With the virtual environment active, install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This installs the following packages:

| Package | Purpose |
|---|---|
| `anthropic` | Official Anthropic Python SDK — used in every Python file |
| `python-dotenv` | Loads your API key from `.env` at runtime |
| `fastapi` | Web framework used in the API server examples |
| `uvicorn` | ASGI server for running FastAPI locally |

Confirm the install:

```bash
pip show anthropic
```

---

## Step 5 — Install Node.js / TypeScript Dependencies

From the same project root, install the npm packages:

```bash
npm install
```

This installs everything in `package.json`:

| Package | Purpose |
|---|---|
| `@anthropic-ai/sdk` | Official Anthropic TypeScript/JavaScript SDK |
| `dotenv` | Loads your API key from `.env` in Node |
| `express` | Web framework used in the streaming server examples |
| `ts-node` | Runs TypeScript files directly without a compile step |
| `typescript` | TypeScript compiler |
| `@types/express` | Type definitions for Express |
| `@types/node` | Type definitions for Node.js built-ins |

Confirm the install:

```bash
npx ts-node --version
```

---

## Step 6 — Create an Anthropic Account

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Click **Sign up** and register with your email address
3. Verify your email when prompted
4. Log in to the Anthropic Console

---

## Step 7 — Get Your API Key

1. In the Console, click **API Keys** in the left sidebar
2. Click **Create Key**
3. Name it something like `claude-course`
4. Click **Create Key**
5. **Copy the key immediately** — it is only shown once. If you miss it, delete it and create a new one.

Your API key looks like this:

```
sk-ant-api03-...
```

Keep this key private. Do not commit it to Git, paste it into source files, or share it anywhere.

---

## Step 8 — Add Billing Credits

The Anthropic API is pay-as-you-go. You need a small amount of credit to run the examples.

1. In the Console, click **Billing** in the left sidebar
2. Click **Add credits** and add a minimum amount — $5 is more than enough for the full course
3. Enter your payment details and confirm

All examples default to `claude-haiku-4-5`, the least expensive model. Running every example across all modules typically costs under $1 total.

---

## Step 9 — Configure Your API Key

The repo already includes a `.env` file at the root. Open it and replace the placeholder with your actual key:

```
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

Save the file. The `.env` file is already listed in `.gitignore` so it will never be committed.

Every Python file in the course calls `load_dotenv()` at the top and every TypeScript file uses `dotenv/config` — the key loads automatically with no further configuration needed.

---

## Step 10 — Verify Python Setup

```bash
python first_call.py
```

Expected output:

```
Hello! I'm happy to help you today.
```

---

## Step 11 — Verify TypeScript Setup

```bash
npm run first-call
```

This runs `npx ts-node --esm firstCall.ts` as defined in `package.json`. Expected output:

```
Hello! I'm happy to help you today.
```

If both commands return a response, your full environment is ready.

---

## Repository Structure

All files are at the project root — there are no subfolders.

```
Pluralsight-Building-Applications-with-Claude/
│
├── .env                    # Your API key — never commit this
├── .gitignore
├── requirements.txt        # Python dependencies
├── package.json            # Node/TypeScript dependencies
├── setup.md                # Original setup notes
├── README.md               # This file
│
├── # ── Python files ──────────────────────────────────────
├── first_call.py           # Module 1 — first API call
├── client_stream.py        # Module 2, Clip 1 — Python streaming
├── tools.py                # Module 2, Clip 2 — tool use
├── pipeline.py             # Module 2 — pipeline example
├── agent.py                # Module 3, Clip 1 — support agent
├── support_agent.py        # Module 3, Clip 1 — extended agent
├── service.py              # Module 3 — service layer
├── config.py               # Module 3, Clip 2 — model config
├── main.py                 # Module 3, Clip 2 — task-based selection
├── multi_model.py          # Module 3, Clip 2 — multi-model example
├── routing.py              # Module 3, Clip 3 — fallback + A/B testing
│
└── # ── TypeScript files ───────────────────────────────────
    ├── firstCall.ts          # Module 1 — first API call
    ├── client_server.ts      # Module 2, Clip 1 — browser-side stream client
    ├── client_stream.ts      # Module 2, Clip 1 — stream client
    └── server.ts             # Module 2, Clip 1 — Express SSE server
```

---

## Daily Workflow

Every time you return to work on the course:

1. Navigate to the project folder in your terminal
2. Activate the Python virtual environment:
   - macOS / Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate.bat`
3. Confirm `(venv)` appears in your prompt
4. Run Python files with `python <filename>.py`
5. Run TypeScript files with `npx ts-node --esm <filename>.ts` or via the npm scripts in `package.json`

The `.env` file handles the API key for both runtimes automatically.

---

## npm Scripts

The `package.json` includes two convenience scripts:

```bash
npm run first-call    # runs firstCall.ts
npm run server        # runs server.ts (Express SSE streaming server)
```

For any other TypeScript file not listed as a script, run it directly:

```bash
npx ts-node --esm client_stream.ts
```

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'anthropic'`**
Your virtual environment is not active. Run `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate.bat` (Windows) and try again.

**`Cannot find module '@anthropic-ai/sdk'`**
Node modules are not installed. Run `npm install` from the project root.

**`AuthenticationError: invalid x-api-key` (Python or TypeScript)**
Your API key is missing or incorrect. Open `.env` and confirm the key is on its own line with no quotes, spaces, or extra characters. Also confirm `load_dotenv()` appears before `new Anthropic()` in Python files, and that `import 'dotenv/config'` appears at the top of TypeScript files.

**`SyntaxError: Cannot use import statement` in TypeScript**
Make sure `"type": "module"` is present in `package.json` and you are using the `--esm` flag: `npx ts-node --esm yourfile.ts`.

**`PermissionError` when activating on Windows PowerShell**
Run this once and then try activating again:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**`python` not found on macOS/Linux**
Use `python3` instead of `python`. On some systems `python` points to Python 2.

**Billing / quota errors**
Log in to [console.anthropic.com](https://console.anthropic.com), go to Billing, and confirm your credit balance is above zero.

---

## Useful Links

- [Anthropic Console](https://console.anthropic.com) — manage API keys, usage, and billing
- [Anthropic API Docs](https://docs.anthropic.com) — full API reference
- [Model Overview & Pricing](https://docs.anthropic.com/en/docs/about-claude/models) — current model names and token costs
- [Anthropic Python SDK](https://pypi.org/project/anthropic/) — PyPI page and changelog
- [Anthropic TypeScript SDK](https://www.npmjs.com/package/@anthropic-ai/sdk) — npm page and changelog
- [Node.js Downloads](https://nodejs.org) — install or update Node.js
- [Python Downloads](https://www.python.org/downloads/) — install or update Python
