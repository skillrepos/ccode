# Alternate Setup: Claude Code Without a Paid Anthropic Account

## Use Claude Code's agentic workflow for free

This guide lets you run all five workshop labs **without a paid Claude/Anthropic account**. Three options are covered, from easiest to most advanced:

| Option | Speed | Setup Time | Hardware Needs | Cost |
|--------|-------|-----------|----------------|------|
| **A. HuggingFace Inference** (recommended) | Fast (server-side GPUs) | ~5 minutes | Any laptop with internet | Free (with limits) |
| **B. Ollama** (local) | Slow (15–60s/response) | ~15 minutes + download | 32GB+ RAM | Free |
| **C. llama.cpp** (local, advanced) | Moderate (15–25% faster than Ollama) | ~20 minutes + build | 32GB+ RAM | Free |

<br>

> **What works with all options:** All core Claude Code features — `/compact`, `/clear`, `/rewind`, `/help`, `/init`, plan mode, YOLO mode, skills, subagents, custom commands, plugins.
>
> **What's different:** Tool search is disabled (all tools load upfront), the `/model` menu still shows Claude models but your chosen model is used regardless, and output quality depends on the model.
>
> **What to expect:** Open models handle the labs well for learning purposes. For production coding work, Claude Sonnet/Opus will produce significantly better results.

<br><br>

---
---

# Option A: HuggingFace Inference Providers (Recommended)

Run open-source models on HuggingFace's cloud GPUs — no downloads, no hardware requirements, fast responses. This is the easiest and fastest free option.

<br>

---

## A1: Create a HuggingFace Account

If you don't already have one, sign up for a free account at [huggingface.co/join](https://huggingface.co/join).

<br><br>

---

## A2: Create an Access Token

1. Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Click **Create new token**
3. Give it a name (e.g., "claude-code-workshop")
4. Select **Read** access (that's all you need)
5. Click **Create token** and copy the token value

<br><br>

---

## A3: Install Claude Code

If you haven't already:
```bash
npm install -g @anthropic-ai/claude-code
```

<br><br>

---

## A4: Configure Claude Code to Use HuggingFace

Set the environment variables that route Claude Code through HuggingFace's Inference Providers. Replace `hf_YOUR_TOKEN_HERE` with the token you created in step A2.

**For this terminal session:**
```bash
export ANTHROPIC_BASE_URL="https://router.huggingface.co"
export ANTHROPIC_AUTH_TOKEN="hf_YOUR_TOKEN_HERE"
export ANTHROPIC_API_KEY="hf_YOUR_TOKEN_HERE"
export ANTHROPIC_DEFAULT_SONNET_MODEL="Qwen/Qwen3-Coder"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="Qwen/Qwen3-Coder"
export ANTHROPIC_DEFAULT_OPUS_MODEL="Qwen/Qwen3-Coder"
```

**To make it permanent**, add the above lines to your shell config:
```bash
# For zsh (macOS default)
cat >> ~/.zshrc << 'EOF'
export ANTHROPIC_BASE_URL="https://router.huggingface.co"
export ANTHROPIC_AUTH_TOKEN="hf_YOUR_TOKEN_HERE"
export ANTHROPIC_API_KEY="hf_YOUR_TOKEN_HERE"
export ANTHROPIC_DEFAULT_SONNET_MODEL="Qwen/Qwen3-Coder"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="Qwen/Qwen3-Coder"
export ANTHROPIC_DEFAULT_OPUS_MODEL="Qwen/Qwen3-Coder"
EOF

# For bash
# Replace ~/.zshrc with ~/.bashrc in the command above
```

> **Other models you can try:** Replace `Qwen/Qwen3-Coder` with any model available on [HuggingFace Inference Providers](https://huggingface.co/docs/inference-providers/index), such as `THUDM/GLM-5.1` or `google/gemma-4`. Append `:fastest` or `:cheapest` to prefer faster or cheaper providers (e.g., `Qwen/Qwen3-Coder:fastest`).

<br><br>

---

## A5: Alternative — Use the Interactive Picker

Instead of setting environment variables manually, HuggingFace offers an interactive CLI tool that lets you pick a model and provider:

```bash
pip install huggingface_hub
huggingface-cli login
hf claude
```

This launches an interactive picker where you select a model, then starts Claude Code with everything pre-configured.

<br><br>

---

## A6: Clone the Workshop Repo

```bash
git clone https://github.com/skillrepos/ccode
cd ccode
```

<br><br>

---

## A7: Start Claude Code and Verify

```bash
claude
```

Check the **welcome banner** — it should show your HuggingFace model name (e.g., `Qwen/Qwen3-Coder`). Type a simple prompt to verify:

```
Can you see the files in this directory? List them.
```

Claude should respond in natural language within a few seconds. If you get a token/authentication error, double-check your `ANTHROPIC_AUTH_TOKEN` value.

> **Note:** If you ask "What model are you?", the model will likely claim to be Claude — this is because Claude Code's system prompt tells the model to act as Claude. The welcome banner is the actual indicator of which model is running.

<br><br>

---

## HuggingFace Free Tier Limits

The free tier includes monthly inference credits. If you hit rate limits during the labs:
- Wait a few minutes and retry — limits often reset quickly
- Consider upgrading to [HuggingFace PRO](https://huggingface.co/pricing) ($9/month) for 20x more credits
- Switch to a local option (B or C below) as a fallback

For a typical 3-hour workshop, the free tier should be sufficient if you're not running excessive prompts outside the labs.

<br><br>

---
---

# Option B: Ollama (Local Models)

Run models entirely on your machine with no internet required after setup. Slower than HuggingFace but fully offline and private.

<br>

---

## Prerequisites

- **Hardware:** 32GB+ unified memory (Apple Silicon) or 24GB+ VRAM. 16GB can work but expect very slow responses.
- **Disk:** ~20GB free for Ollama + one model.
- **OS:** macOS, Linux, or Windows (WSL2).

<br><br>

---

## B1: Install Ollama

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

## B2: Quick Setup (Recommended)

If you have Ollama v0.14.0+, this one command handles everything — pulls the model, sets environment variables, and starts Claude Code:

```bash
ollama launch claude --model qwen3-coder
```

If it works, skip to **[B6: Clone the Workshop Repo](#b6-clone-the-workshop-repo)**.

If `ollama launch` isn't available or you prefer manual setup, continue with B3 below.

<br><br>

---

## B3: Pull a Model

Claude Code requires models that support its agentic tool-calling format. The following models are verified to work:

**Recommended:**
```bash
ollama pull qwen3-coder
```
This is a 30B parameter model (~19GB download). It produces the best results with Claude Code but requires 24GB+ VRAM/unified memory and responds in 15–60 seconds depending on hardware.

**Alternative:**
```bash
ollama pull glm-4.7
```

> **⚠️ Models that do NOT work well:** Older models like `qwen2.5-coder` (7b/14b) do not properly handle Claude Code's agentic conversation format. They may produce raw JSON output instead of natural language responses. Stick with the recommended models above.

<br><br>

---

## B4: Start the Ollama Server

Start the server with keep-alive set to prevent the model from being unloaded during idle time:

```bash
OLLAMA_KEEP_ALIVE=-1 ollama serve
```

Leave this running in a separate terminal.

> **Already have Ollama running as a system service?** Set the environment variable globally instead:
> ```bash
> launchctl setenv OLLAMA_KEEP_ALIVE -1   # macOS
> # or
> export OLLAMA_KEEP_ALIVE=-1             # add to ~/.bashrc or ~/.zshrc
> ```
> Then restart the Ollama service.

<br><br>

---

## B5: Configure Claude Code

**For this terminal session:**
```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder"
```

**To make it permanent**, add the above lines to your shell config (`~/.zshrc` or `~/.bashrc`).

<br><br>

---

## B6: Clone the Workshop Repo

```bash
git clone https://github.com/skillrepos/ccode
cd ccode
```

<br><br>

---

## B7: Warm Up the Model

Pre-load the model into memory so your first Claude Code response is faster:

```bash
ollama run qwen3-coder ""
```

Type `/bye` to exit the Ollama shell after the model loads.

<br><br>

---

## B8: Start Claude Code and Verify

```bash
claude
```

Check the **welcome banner** — it should show `qwen3-coder`. Type a prompt to verify:

```
Can you see the files in this directory? List them.
```

Expect responses in 15–60 seconds. If you see raw JSON output instead of natural language, your model doesn't support Claude Code's format — switch to one of the recommended models.

<br><br>

---
---

# Option C: llama.cpp (Local, Advanced)

[llama.cpp](https://github.com/ggml-org/llama.cpp) is 15–25% faster than Ollama with 20% less memory usage, because it runs the inference engine directly without Ollama's Go wrapper overhead.

<br>

---

## Prerequisites

Same as Ollama: 32GB+ RAM, ~20GB disk, macOS/Linux/WSL2.

<br><br>

---

## C1: Automated Setup

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

<br><br>

---

## C2: Manual Setup

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

<br><br>

---
---

# Lab Adjustments (All Options)

Most lab steps work identically regardless of which option you chose. Below are the differences.

<br>

## General Notes

- **Skip `/login`**: No authentication needed. If prompted, just proceed.
- **The `/model` command**: When labs say "set your model to Sonnet," skip this — your model is already set via environment variables. The `/model` menu always displays the built-in Claude model list regardless of backend. To confirm which model is running, check the **welcome banner** when Claude Code starts.
- **Output quality**: Open models may produce slightly different (sometimes less polished) output than Claude Sonnet/Opus. The lab steps and concepts still apply — just expect some variation.
- **Speed** (local options only): Expect responses in 15–60 seconds with `qwen3-coder`. HuggingFace Inference should respond in a few seconds.

<br>

## Lab 1: Introduction to Claude Code and Basic Setup

- **Step 6 (Exit and Resume)**: The `/resume` command works normally with all options.

No other changes needed.

<br>

## Lab 2: Working with Claude Code Modes

- **Step 4 (Plan Mode)**: Plans may be less detailed than with Claude Opus/Sonnet. This is expected.
- **Step 9 (YOLO Mode)**: `claude --dangerously-skip-permissions` works identically — it's a Claude Code feature, not model-dependent.

No other changes needed.

<br>

## Lab 3: Built-in Commands and Context Management

- **Step 4 (Check Context Usage)**: Token counts will differ from screenshots since open models use different tokenizers.
- **Step 5 (/compact)**: Works normally. Summary quality depends on your model.
- **Step 7 (/init for CLAUDE.md)**: Works normally — CLAUDE.md is a Claude Code feature that works with any backend.

No other changes needed.

<br>

## Lab 4: Skills + Subagents

- **Step 7 (Trigger the skill)**: Skill matching may be slightly less reliable. If the model doesn't automatically pick up the skill, be more explicit: "Use the api-checker skill to validate GET /health on my service."
- **Steps 8-9 (Subagents)**: Subagent delegation works the same way.

> **Tip**: If a subagent produces poor results, consider switching to Claude's API temporarily for the most demanding agentic tasks.

<br>

## Lab 5: Supervised Subagent Workflow + Plugin Packaging + VS Code

- **Steps 1-4 (Commands, Agents, Plugin manifest)**: File creation and directory structure work identically.
- **Step 6 (Supervised Delegation)**: The Plan-Implement-Review pattern works, but plan quality depends on model capability.
- **Step 7 (Reviewer Subagent)**: The `disallowedTools: Write, Edit` constraint is enforced by Claude Code regardless of backend.
- **Step 9 (VS Code Extension)**: The extension connects through the same `ANTHROPIC_BASE_URL` environment variable.

<br><br>

---

# Troubleshooting

**Authentication error (HuggingFace):**
Double-check your token value. Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and verify it's active and has Read access.

**Rate limit hit (HuggingFace):**
The free tier has usage limits. Wait a few minutes for limits to reset, or switch to a local option (B or C) as a fallback.

**Raw JSON output instead of natural language:**
Your model doesn't support Claude Code's agentic tool-calling format. Use a recommended model (`qwen3-coder`, `glm-4.7`, `GLM-5.1`, `Gemma 4`). Older models like `qwen2.5-coder` are known to produce broken output.

**"Connection refused" error (Ollama):**
The server isn't running. Start it with `OLLAMA_KEEP_ALIVE=-1 ollama serve` in a separate terminal.

**Very slow responses (local options):**
This is expected with 30B models on consumer hardware. Make sure you started Ollama with `OLLAMA_KEEP_ALIVE=-1` and ran the warm-up step. If speed is unacceptable, switch to HuggingFace Inference (Option A).

**"Unknown command" for `ollama launch`:**
Your Ollama version is too old. Upgrade to v0.14.0 or later.

**Tool search warnings:**
When `ANTHROPIC_BASE_URL` points to a non-Anthropic endpoint, Claude Code disables tool search and loads all tools upfront. This is expected and doesn't affect lab functionality.

<br><br>

---

# Switching Between Options

**Switch to Claude's API:**
```bash
unset ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_API_KEY
unset ANTHROPIC_DEFAULT_SONNET_MODEL ANTHROPIC_DEFAULT_HAIKU_MODEL ANTHROPIC_DEFAULT_OPUS_MODEL
claude /login
```

**Switch to HuggingFace:**
```bash
export ANTHROPIC_BASE_URL="https://router.huggingface.co"
export ANTHROPIC_AUTH_TOKEN="hf_YOUR_TOKEN"
export ANTHROPIC_API_KEY="hf_YOUR_TOKEN"
export ANTHROPIC_DEFAULT_SONNET_MODEL="Qwen/Qwen3-Coder"
```

**Switch to Ollama:**
```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"
```

> **Tip**: Create shell aliases for quick switching:
> ```bash
> alias claude-hf='export ANTHROPIC_BASE_URL="https://router.huggingface.co" && export ANTHROPIC_AUTH_TOKEN="hf_YOUR_TOKEN" && export ANTHROPIC_API_KEY="hf_YOUR_TOKEN" && export ANTHROPIC_DEFAULT_SONNET_MODEL="Qwen/Qwen3-Coder"'
> alias claude-local='export ANTHROPIC_AUTH_TOKEN="ollama" && export ANTHROPIC_BASE_URL="http://localhost:11434" && export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"'
> alias claude-cloud='unset ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_API_KEY ANTHROPIC_DEFAULT_SONNET_MODEL'
> ```

<br><br>

---

# Cleaning Up

## HuggingFace
No cleanup needed — nothing is installed locally. To revoke your token, go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

## Ollama

**Unload the model from memory:**
```bash
ollama stop qwen3-coder
```

**Stop the server:**
Press `Ctrl+C` in the terminal where `ollama serve` is running, or: `pkill ollama`

**Remove the model from disk** (frees ~19GB):
```bash
ollama rm qwen3-coder
```

**Uninstall Ollama** (optional):
```bash
brew uninstall ollama          # macOS
sudo rm $(which ollama)        # Linux
```

## llama.cpp

**Stop the server:**
```bash
kill $(cat /tmp/llama-server.pid)    # if started with setup script
pkill llama-server                    # if started manually
```

**Remove cached model files:**
```bash
rm -rf ~/.cache/llama.cpp
```

**Uninstall:**
```bash
brew uninstall llama.cpp                      # macOS
rm -rf ~/.local/share/llama.cpp               # Linux (if built from source)
```

<br><br>

---

*This alternate setup guide accompanies the workshop "AI-Powered Coding with Claude Code" by Tech Skills Transformations LLC.*
*For the standard setup using Claude's API, see [README.md](./README.md) and [STARTUP.md](./STARTUP.md).*
