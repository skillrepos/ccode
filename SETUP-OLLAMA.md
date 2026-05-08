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

We recommend **Qwen3 Coder 30B** for the best agentic coding experience. If your hardware can't handle 30B parameters, use a smaller alternative.

**Recommended (requires ~20GB RAM):**
```bash
ollama pull qwen3-coder:30b
```

**Lighter alternatives:**
```bash
# Good balance of quality and speed (~8GB RAM)
ollama pull qwen3-coder:14b

# Fastest, lowest resource usage (~4GB RAM)
ollama pull qwen3-coder:7b
```

Verify the model is available:
```bash
ollama list
```

<br><br>

---

## Step 3: Start the Ollama Server

Ollama runs a local server that Claude Code connects to. In most installations, the server starts automatically. If not:

```bash
ollama serve
```

Leave this running in a separate terminal window. The server listens on `http://localhost:11434` by default.

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
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:30b"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:30b"
```

**To make it permanent**, add the above lines to your shell config:
```bash
# For bash
echo 'export ANTHROPIC_BASE_URL="http://localhost:11434"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:30b"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:30b"' >> ~/.bashrc

# For zsh (macOS default)
echo 'export ANTHROPIC_BASE_URL="http://localhost:11434"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:30b"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:30b"' >> ~/.zshrc
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

## Step 7: Start Claude Code

```bash
claude
```

You should see Claude Code start up and connect to your local Ollama server. You do **not** need to run `/login` — there is no authentication required for local models.

<br><br>

---

## Step 8: Verify the Connection

In Claude Code, type a simple prompt to confirm everything is working:

```
What model are you, and can you see the files in this directory?
```

The model should identify itself (e.g., "powered by qwen3-coder:30b") and list files in the repo. If you get a connection error, make sure `ollama serve` is running in another terminal.

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
- **Speed**: First response may be slow as the model loads into memory. Subsequent responses are faster.

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

> **Tip**: If a subagent seems stuck or produces poor results, try using a larger model (e.g., `qwen3-coder:30b` instead of `14b`).

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

**Very slow responses:**
Your model may be too large for your hardware. Try a smaller model (`qwen3-coder:14b` or `7b`). On first launch, the model needs to load into memory — subsequent prompts will be faster.

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
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:30b"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder:14b"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder:30b"
```

> **Tip**: Create shell aliases for quick switching:
> ```bash
> alias claude-local='export ANTHROPIC_BASE_URL="http://localhost:11434" && export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder:30b"'
> alias claude-cloud='unset ANTHROPIC_BASE_URL && unset ANTHROPIC_DEFAULT_SONNET_MODEL'
> ```

<br><br>

---

*This alternate setup guide accompanies the workshop "AI-Powered Coding with Claude Code" by Tech Skills Transformations LLC.*
*For the standard setup using Claude's API, see [README.md](./README.md) and [STARTUP.md](./STARTUP.md).*
