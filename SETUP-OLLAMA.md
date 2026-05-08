# Alternate Setup: Claude Code with Ollama (Free Local Models)

## Use Claude Code's agentic workflow without a paid subscription

This guide lets you run all five workshop labs using **free, local models** via [Ollama](https://ollama.com) instead of Anthropic's API. You'll get the same Claude Code interface — slash commands, skills, subagents, and all — powered by open-source models running on your machine.

<br>

> **What works:** All core Claude Code features — `/compact`, `/clear`, `/rewind`, `/help`, `/init`, plan mode, YOLO mode, skills, subagents, custom commands, plugins.
>
> **What's different:** Tool search is disabled (all tools load upfront), model selection via `/model` shows local models instead of Claude models, and output quality depends on the model you choose.
>
> **What to expect:** Local models handle the labs well for learning purposes. For production coding work, Claude Sonnet/Opus will produce significantly better results on complex multi-file tasks.

<br><br>

---

## Prerequisites

- **Hardware:** 16GB+ RAM recommended (32GB+ for larger models). A GPU with 8GB+ VRAM helps but isn't required — Ollama runs on CPU too.
- **Disk:** ~20GB free for Ollama + one model.
- **OS:** macOS, Linux, or Windows (WSL2).
- **No Anthropic/Claude account needed.**

<br><br>

---

## Step 1: Install Ollama

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:** Download from [ollama.com/download](https://ollama.com/download) and install.

Verify installation:
```bash
ollama --version
```

<br><br>

---

## Step 2: Pull a Model

We recommend **Qwen3 Coder 14B** as the best balance of quality and response speed for local use. Even on fast Apple Silicon MacBooks, larger models (30B+) can take 30–60 seconds per response, which makes the labs tedious.

**Recommended (requires ~8GB RAM, responds in seconds):**
```bash
ollama pull qwen3-coder:14b
```

**Alternatives:**
```bash
# Fastest, lowest resource usage (~4GB RAM) — good for older hardware
ollama pull qwen3-coder:7b

# Highest quality but SLOW (~20GB RAM, 30-60s per response even on M3/M4 Macs)
# Only use this if you have 64GB+ RAM and patience
ollama pull qwen3-coder:30b
```

Verify the model is available:
```bash
ollama list
```

<br><br>

---

## Step 3: Start the Ollama Server

Ollama runs a local server that Claude Code connects to. In most installations, the server starts automatically. If not, start it in a separate terminal:

```bash
OLLAMA_KEEP_ALIVE=-1 ollama serve
```

The `OLLAMA_KEEP_ALIVE=-1` setting tells Ollama to keep the model loaded in memory indefinitely. Without this, Ollama unloads the model after 5 minutes of idle time, and the next prompt pays the full reload penalty (30+ seconds) again. Leave this terminal running.

> **Already have Ollama running as a system service?** Set the environment variable globally instead:
> ```bash
> launchctl setenv OLLAMA_KEEP_ALIVE -1   # macOS
> # or
> export OLLAMA_KEEP_ALIVE=-1             # add to ~/.bashrc or ~/.zshrc
> ```
> Then restart the Ollama service.

<br><br>

---

## Step 4: Install Claude Code

If you haven't already:
```bash
npm install -g @anthropic-ai/claude-code
```

<br><br>

---

## Step 5: Configure Claude Code to Use Ollama

Set the environment variables that point Claude Code to your local Ollama server. Ollama provides an Anthropic-compatible API endpoint.

**For this terminal session:**
```bash
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:14b"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:14b"
```

**To make it permanent**, add the above lines to your shell config:
```bash
# For bash
echo 'export ANTHROPIC_BASE_URL="http://localhost:11434"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:14b"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:14b"' >> ~/.bashrc

# For zsh (macOS default)
echo 'export ANTHROPIC_BASE_URL="http://localhost:11434"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:14b"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:14b"' >> ~/.zshrc
```

> **Adjust model names** if you pulled a different model in Step 2. Use the exact name shown by `ollama list`.

<br><br>

---

## Step 6: Clone the Workshop Repo

```bash
git clone https://github.com/skillrepos/ccode
cd ccode
```

<br><br>

---

## Step 7: Warm Up the Model

Before starting Claude Code, pre-load the model into memory so your first response is fast:

```bash
ollama run qwen3-coder:14b ""
```

This loads the model weights into RAM without generating output. You'll see it briefly think and then return to the prompt. Type `/bye` to exit the Ollama shell.

<br><br>

---

## Step 8: Start Claude Code

```bash
claude
```

You should see Claude Code start up and connect to your local Ollama server. You do **not** need to run `/login` — there is no authentication required for local models.

<br><br>

---

## Step 9: Verify the Connection

In Claude Code, type a simple prompt to confirm everything is working:

```
What model are you, and can you see the files in this directory?
```

The model should identify itself (e.g., "powered by qwen3-coder:14b") and list files in the repo. The response should come back within a few seconds if the warm-up step worked. If you get a connection error, make sure `ollama serve` is running in another terminal.

> **Note:** This prompt is the reliable way to confirm which model is running. The `/model` command will still show the standard Claude models (Opus, Sonnet, Haiku) even when connected to Ollama — that menu always displays the built-in list and does not reflect your environment variable overrides.

<br><br>

---
<br>

# Lab Adjustments for Ollama

Most lab steps work identically with Ollama. Below are the specific differences you'll encounter.

<br>

## General Notes (All Labs)

- **Skip `/login`**: No authentication needed. If prompted, just proceed.
- **The `/model` command**: When labs say "set your model to Sonnet," you can skip this — your model is already set via the environment variable. **Important:** If you run `/model`, it will still show the standard Claude models (Opus, Sonnet, Haiku) — not your Ollama models. This is expected. The `/model` menu always displays the built-in list regardless of backend. Your environment variables (`ANTHROPIC_DEFAULT_SONNET_MODEL`, etc.) override what actually runs, so the model shown in `/model` is effectively ignored. To confirm which model is actually being used, ask Claude: `What model are you?`
- **Output quality**: Local models may produce slightly different (sometimes less polished) output than Claude Sonnet/Opus. The lab steps and concepts still apply — just expect some variation in the exact text Claude generates.
- **Speed**: The first response after starting Ollama will be slow as the model loads into memory. Subsequent responses with `qwen3-coder:14b` should take just a few seconds. If every response takes 30+ seconds, you're likely running a model that's too large — switch to `14b`.

<br>

## Lab 1: Introduction to Claude Code and Basic Setup

- **Step 6 (Exit and Resume)**: The `/resume` command should work normally. Session history is stored locally regardless of which model you use.

No other changes needed. All basic interactions, file creation, and editing work the same.

<br>

## Lab 2: Working with Claude Code Modes

- **Step 4 (Plan Mode)**: Plan mode works with local models, but plans may be less detailed than with Claude Opus/Sonnet. This is expected.
- **Step 9 (YOLO Mode)**: `claude --dangerously-skip-permissions` works identically — it's a Claude Code feature, not model-dependent.

No other changes needed.

<br>

## Lab 3: Built-in Commands and Context Management

- **Step 4 (Check Context Usage)**: Token counts will differ from screenshots since local models use different tokenizers.
- **Step 5 (/compact)**: Works normally. The compacted summary quality depends on your model.
- **Step 7 (/init for CLAUDE.md)**: Works normally — CLAUDE.md is a Claude Code feature that works with any backend model.

No other changes needed.

<br>

## Lab 4: Skills + Subagents

This lab creates a skill (api-checker) and subagents (planner, test-runner). All of these are Claude Code features that work regardless of the backend model.

- **Step 7 (Trigger the skill)**: The skill matching may be slightly less reliable with smaller models. If the model doesn't automatically pick up the skill, try being more explicit: "Use the api-checker skill to validate GET /health on my service."
- **Steps 8-9 (Subagents)**: Subagent delegation works the same way. Each subagent gets its own context window running on your local model.

> **Tip**: If a subagent seems stuck or produces poor results with `7b`, try upgrading to `qwen3-coder:14b`. For the most demanding agentic tasks, consider switching to Claude's API temporarily.

<br>

## Lab 5: Supervised Subagent Workflow + Plugin Packaging + VS Code

- **Steps 1-4 (Commands, Agents, Plugin manifest)**: File creation and directory structure are Claude Code features — they work identically.
- **Step 5 (/skills, /help)**: Discovery commands work the same.
- **Step 6 (Supervised Delegation)**: The Plan-Implement-Review pattern works, but plan quality depends on model capability.
- **Step 7 (Reviewer Subagent)**: The `disallowedTools: Write, Edit` constraint is enforced by Claude Code regardless of backend model — this is a tool-level restriction, not a model-level one.
- **Step 9 (VS Code Extension)**: If using VS Code, the extension connects through the same `ANTHROPIC_BASE_URL` environment variable.

<br><br>

---

# Troubleshooting

**"Connection refused" error:**
Ollama server isn't running. Start it with `ollama serve` in a separate terminal.

**Very slow responses (30-60+ seconds):**
The 30B model is likely too large for interactive use on your hardware. Switch to `qwen3-coder:14b` — it responds in seconds on most modern machines while still handling the labs well. Update your environment variables and restart Claude Code. Note: the very first response after starting Ollama is always slower as the model loads into memory; subsequent prompts should be faster.

**"Model not found" error:**
The model name in your environment variable doesn't match what Ollama has. Run `ollama list` and use the exact name shown.

**Tool search warnings:**
When `ANTHROPIC_BASE_URL` points to a non-Anthropic endpoint, Claude Code disables tool search (deferred tool loading) because most proxies don't forward `tool_reference` blocks. All tools load upfront instead. This is expected and doesn't affect lab functionality.

**Skill not triggering automatically:**
Smaller models may not match context-triggered skills as reliably. Be more explicit in your prompt, or invoke the skill by describing exactly what you want it to do.

**Subagent producing poor results:**
Agentic work (planning, code review, multi-step reasoning) is where model quality matters most. If a subagent consistently underperforms, consider upgrading to a larger model or switching to Claude's API for that specific task.

<br><br>

---

# Switching Between Ollama and Claude API

You can switch between local and cloud models at any time by changing (or unsetting) the environment variables:

**Switch to Claude API:**
```bash
unset ANTHROPIC_BASE_URL
unset ANTHROPIC_DEFAULT_SONNET_MODEL
unset ANTHROPIC_DEFAULT_HAIKU_MODEL
unset ANTHROPIC_DEFAULT_OPUS_MODEL
claude /login
```

**Switch back to Ollama:**
```bash
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:14b"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:14b"
```

> **Tip**: Create shell aliases for quick switching:
> ```bash
> alias claude-local='export ANTHROPIC_BASE_URL="http://localhost:11434" && export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:14b"'
> alias claude-cloud='unset ANTHROPIC_BASE_URL && unset ANTHROPIC_DEFAULT_SONNET_MODEL'
> ```

<br><br>

---

# Cleaning Up After the Labs

When you're done with the workshop, you can free up the memory and disk space used by Ollama.

**Unload the model from memory** (frees RAM/VRAM immediately):
```bash
ollama stop qwen3-coder:14b
```

**Stop the Ollama server** (if you started it manually):
Press `Ctrl+C` in the terminal where `ollama serve` is running, or:
```bash
pkill ollama
```

**Remove the model from disk** (optional — frees ~8-20GB depending on model):
```bash
ollama rm qwen3-coder:14b
```

**Uninstall Ollama entirely** (optional):
```bash
# macOS (Homebrew)
brew uninstall ollama

# Linux
sudo rm $(which ollama)
```

<br><br>

---

*This alternate setup guide accompanies the workshop "AI-Powered Coding with Claude Code" by Tech Skills Transformations LLC.*
*For the standard setup using Claude's API, see [README.md](./README.md) and [STARTUP.md](./STARTUP.md).*
