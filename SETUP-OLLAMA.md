# Alternate Setup: Claude Code with Ollama (Free Local Models)

## Use Claude Code's agentic workflow without a paid subscription

This guide lets you run all five workshop labs using **free, local models** via [Ollama](https://ollama.com) instead of Anthropic's API. You'll get the same Claude Code interface — slash commands, skills, subagents, and all — powered by open-source models running on your machine.

<br>

> **What works:** All core Claude Code features — `/compact`, `/clear`, `/rewind`, `/help`, `/init`, plan mode, YOLO mode, skills, subagents, custom commands, plugins.
>
> **What's different:** Tool search is disabled (all tools load upfront), the `/model` menu still shows Claude models but your local model is used regardless, and output quality depends on the model you choose.
>
> **What to expect:** Local models handle the labs well for learning purposes. Expect responses in 15–60 seconds depending on your hardware and model. For production coding work, Claude Sonnet/Opus will produce significantly better results and respond faster.

<br>

> **Important: Model compatibility.** Claude Code uses an agentic tool-calling format that not all models handle correctly. Older or smaller models (e.g., `qwen2.5-coder:14b`) may produce malformed JSON output instead of natural language responses. The models recommended below have been verified to work with Claude Code's format.

<br><br>

---

## Prerequisites

- **Hardware:** 32GB+ unified memory (Apple Silicon) or 24GB+ VRAM recommended for the default model. 16GB can work with smaller models but expect slower responses.
- **Disk:** ~20GB free for Ollama + one model.
- **OS:** macOS, Linux, or Windows (WSL2).
- **No Anthropic/Claude account needed.**

<br><br>

---

## Quick Setup (Recommended)

Ollama v0.14.0+ includes a one-command setup that configures Claude Code automatically:

```bash
ollama launch claude --model qwen3-coder
```

This pulls the model (if needed), sets all environment variables, and starts Claude Code. If it works for you, skip to **[Step 6: Clone the Workshop Repo](#step-6-clone-the-workshop-repo)**.

If `ollama launch` isn't available (older version) or you prefer manual setup, follow the step-by-step instructions below.

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

Verify installation (you need v0.14.0 or later for Claude Code compatibility):
```bash
ollama --version
```

<br><br>

---

## Step 2: Pull a Model

Claude Code requires models that support its agentic tool-calling format. The following models are verified to work:

**Recommended — best agentic coding quality:**
```bash
ollama pull qwen3-coder
```
This is a 30B parameter model (~19GB download). It produces the best results with Claude Code's tool-use format but requires 24GB+ VRAM/unified memory and responds in 15–60 seconds depending on hardware.

**Alternative — if `qwen3-coder` is too slow:**
```bash
ollama pull glm-4.7
```

> **⚠️ Models that do NOT work well:** Older models like `qwen2.5-coder` (7b/14b) do not properly handle Claude Code's agentic conversation format. They may produce raw JSON output instead of natural language responses. Stick with the recommended models above.

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

Set the environment variables that point Claude Code to your local Ollama server:

**For this terminal session:**
```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder"
```

**To make it permanent**, add the above lines to your shell config:
```bash
# For bash
echo 'export ANTHROPIC_AUTH_TOKEN="ollama"' >> ~/.bashrc
echo 'export ANTHROPIC_BASE_URL="http://localhost:11434"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder"' >> ~/.bashrc
echo 'export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder"' >> ~/.bashrc

# For zsh (macOS default)
echo 'export ANTHROPIC_AUTH_TOKEN="ollama"' >> ~/.zshrc
echo 'export ANTHROPIC_BASE_URL="http://localhost:11434"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder"' >> ~/.zshrc
echo 'export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder"' >> ~/.zshrc
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

Before starting Claude Code, pre-load the model into memory so your first response is faster:

```bash
ollama run qwen3-coder ""
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

The model should identify itself (e.g., "powered by qwen3-coder") and list files in the repo in natural language. If you see raw JSON output instead, your model doesn't support Claude Code's format — switch to one of the recommended models in Step 2.

If you get a connection error, make sure `ollama serve` is running in another terminal.

> **Note:** The `/model` command will still show the standard Claude models (Opus, Sonnet, Haiku) even when connected to Ollama — that menu always displays the built-in list and does not reflect your environment variable overrides. To confirm which model is running, ask: `What model are you?`

<br><br>

---
<br>

# Lab Adjustments for Ollama

Most lab steps work identically with Ollama. Below are the specific differences you'll encounter.

<br>

## General Notes (All Labs)

- **Skip `/login`**: No authentication needed. If prompted, just proceed.
- **The `/model` command**: When labs say "set your model to Sonnet," you can skip this — your model is already set via the environment variable. The `/model` menu always displays the built-in Claude model list regardless of backend. To confirm which model is actually being used, ask Claude: `What model are you?`
- **Output quality**: Local models may produce slightly different (sometimes less polished) output than Claude Sonnet/Opus. The lab steps and concepts still apply — just expect some variation in the exact text Claude generates.
- **Speed**: Expect responses in 15–60 seconds with `qwen3-coder` on most hardware. The first response after the model loads is the slowest. If you used the warm-up step and `OLLAMA_KEEP_ALIVE=-1`, subsequent responses should be consistent.

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

- **Step 7 (Trigger the skill)**: The skill matching may be slightly less reliable with local models. If the model doesn't automatically pick up the skill, try being more explicit: "Use the api-checker skill to validate GET /health on my service."
- **Steps 8-9 (Subagents)**: Subagent delegation works the same way. Each subagent gets its own context window running on your local model.

> **Tip**: If a subagent seems stuck or produces poor results, consider switching to Claude's API temporarily for the most demanding agentic tasks.

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
Ollama server isn't running. Start it with `OLLAMA_KEEP_ALIVE=-1 ollama serve` in a separate terminal.

**Raw JSON output instead of natural language:**
Your model doesn't support Claude Code's agentic tool-calling format. Switch to a recommended model (`qwen3-coder` or `glm-4.7`). Older models like `qwen2.5-coder` are known to produce structured JSON instead of conversational responses.

**Very slow responses (60+ seconds):**
The model may be too large for your hardware, or it's being loaded from scratch each time. Make sure you started Ollama with `OLLAMA_KEEP_ALIVE=-1` and ran the warm-up step. If responses are still slow, that's the tradeoff with running 30B models locally — the models that work correctly with Claude Code require significant compute.

**"Model not found" error:**
The model name in your environment variable doesn't match what Ollama has. Run `ollama list` and use the exact name shown.

**"Unknown command" for `ollama launch`:**
Your Ollama version is too old. Upgrade to v0.14.0 or later: `brew upgrade ollama` (macOS) or re-run the Linux install script.

**Tool search warnings:**
When `ANTHROPIC_BASE_URL` points to a non-Anthropic endpoint, Claude Code disables tool search (deferred tool loading) because most proxies don't forward `tool_reference` blocks. All tools load upfront instead. This is expected and doesn't affect lab functionality.

**Skill not triggering automatically:**
Local models may not match context-triggered skills as reliably as Claude. Be more explicit in your prompt, or invoke the skill by describing exactly what you want it to do.

**Subagent producing poor results:**
Agentic work (planning, code review, multi-step reasoning) is where model quality matters most. If a subagent consistently underperforms, consider switching to Claude's API for that specific task.

<br><br>

---

# Advanced: Using llama.cpp for Better Performance

[llama.cpp](https://github.com/ggml-org/llama.cpp) is 15–25% faster than Ollama with 20% less memory usage, because it runs the inference engine directly without Ollama's Go wrapper overhead. If you want the best local performance, this is the way to go.

## Automated Setup

A setup script is included that handles everything — OS detection, installation, model download, server startup, and Claude Code configuration:

```bash
chmod +x setup-llamacpp.sh
./setup-llamacpp.sh
```

The script works on macOS (installs via Homebrew), Linux (builds from source with CUDA auto-detection), and WSL2. On first run it downloads the Qwen3-Coder model (~19GB) from HuggingFace automatically.

After the script completes, clone the repo (if you haven't already) and start Claude Code:
```bash
git clone https://github.com/skillrepos/ccode && cd ccode
claude
```

## Manual Setup

If you prefer to set things up yourself:

**Install llama.cpp:**
```bash
# macOS
brew install llama.cpp

# Linux — build from source
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release    # add -DGGML_CUDA=ON for NVIDIA GPUs
cmake --build build --config Release
```

**Start the server** (auto-downloads the model from HuggingFace on first run):
```bash
llama-server \
    -hf ggml-org/Qwen3-Coder-30B-A3B-Instruct-Q8_0-GGUF \
    -c 32768 \
    --jinja \
    --port 8080
```

> **Critical:** The `--jinja` flag is required for Claude Code's tool-use format to work. Without it, Claude Code loses its ability to call tools and behaves like a basic chatbot.

**Configure Claude Code:**
```bash
export ANTHROPIC_AUTH_TOKEN="llamacpp"
export ANTHROPIC_BASE_URL="http://localhost:8080"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder"
claude
```

## Stopping llama-server

```bash
# If started with the setup script:
kill $(cat /tmp/llama-server.pid)

# If started manually:
# Press Ctrl+C in the terminal, or:
pkill llama-server
```

The rest of the labs work identically — Claude Code doesn't know or care whether the backend is Ollama or llama.cpp.

<br><br>

---

# Switching Between Ollama and Claude API

You can switch between local and cloud models at any time by changing (or unsetting) the environment variables:

**Switch to Claude API:**
```bash
unset ANTHROPIC_AUTH_TOKEN
unset ANTHROPIC_BASE_URL
unset ANTHROPIC_DEFAULT_SONNET_MODEL
unset ANTHROPIC_DEFAULT_HAIKU_MODEL
unset ANTHROPIC_DEFAULT_OPUS_MODEL
claude /login
```

**Switch back to Ollama:**
```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder"
```

> **Tip**: Create shell aliases for quick switching:
> ```bash
> alias claude-local='export ANTHROPIC_AUTH_TOKEN="ollama" && export ANTHROPIC_BASE_URL="http://localhost:11434" && export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"'
> alias claude-cloud='unset ANTHROPIC_AUTH_TOKEN && unset ANTHROPIC_BASE_URL && unset ANTHROPIC_DEFAULT_SONNET_MODEL'
> ```

<br><br>

---

# Cleaning Up After the Labs

When you're done with the workshop, you can free up the memory and disk space used by Ollama.

**Unload the model from memory** (frees RAM/VRAM immediately):
```bash
ollama stop qwen3-coder
```

**Stop the Ollama server** (if you started it manually):
Press `Ctrl+C` in the terminal where `ollama serve` is running, or:
```bash
pkill ollama
```

**Remove the model from disk** (optional — frees ~19GB):
```bash
ollama rm qwen3-coder
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
