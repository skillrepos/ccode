#!/usr/bin/env bash
# =============================================================================
# setup-llamacpp.sh — Set up llama.cpp + Claude Code with a local model
#
# This script:
#   1. Detects your OS (macOS, Linux, WSL)
#   2. Installs llama.cpp (via Homebrew on macOS, from source on Linux)
#   3. Starts llama-server with a Qwen3-Coder model (auto-downloaded from HF)
#   4. Configures environment variables for Claude Code
#   5. Optionally installs Claude Code if not present
#
# Usage:
#   chmod +x setup-llamacpp.sh
#   ./setup-llamacpp.sh
#
# For the "AI-Powered Coding with Claude Code" workshop.
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration — edit these if you want a different model or port
# ---------------------------------------------------------------------------
MODEL_HF_REPO="ggml-org/Qwen3-Coder-30B-A3B-Instruct-Q8_0-GGUF"
MODEL_NAME="qwen3-coder"
CONTEXT_SIZE=32768
PORT=8080
SHELL_CONFIG=""

# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

info()  { echo -e "${BLUE}[INFO]${NC}  $*"; }
ok()    { echo -e "${GREEN}[OK]${NC}    $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
err()   { echo -e "${RED}[ERROR]${NC} $*"; }

# ---------------------------------------------------------------------------
# Detect OS
# ---------------------------------------------------------------------------
detect_os() {
    case "$(uname -s)" in
        Darwin)
            OS="macos"
            ;;
        Linux)
            if grep -qi microsoft /proc/version 2>/dev/null; then
                OS="wsl"
            else
                OS="linux"
            fi
            ;;
        *)
            err "Unsupported operating system: $(uname -s)"
            err "This script supports macOS, Linux, and Windows (WSL2)."
            exit 1
            ;;
    esac
    ok "Detected OS: $OS"
}

# ---------------------------------------------------------------------------
# Detect shell config file
# ---------------------------------------------------------------------------
detect_shell_config() {
    if [ -n "${ZSH_VERSION:-}" ] || [ "$(basename "$SHELL")" = "zsh" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    elif [ -n "${BASH_VERSION:-}" ] || [ "$(basename "$SHELL")" = "bash" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    else
        SHELL_CONFIG="$HOME/.profile"
    fi
    info "Shell config: $SHELL_CONFIG"
}

# ---------------------------------------------------------------------------
# Check prerequisites
# ---------------------------------------------------------------------------
check_prerequisites() {
    info "Checking prerequisites..."

    # Check RAM
    case "$OS" in
        macos)
            RAM_GB=$(( $(sysctl -n hw.memsize) / 1073741824 ))
            ;;
        linux|wsl)
            RAM_GB=$(( $(grep MemTotal /proc/meminfo | awk '{print $2}') / 1048576 ))
            ;;
    esac

    if [ "$RAM_GB" -lt 16 ]; then
        err "Only ${RAM_GB}GB RAM detected. At least 16GB is required (32GB+ recommended)."
        exit 1
    elif [ "$RAM_GB" -lt 32 ]; then
        warn "${RAM_GB}GB RAM detected. The 30B model may be slow. 32GB+ is recommended."
    else
        ok "${RAM_GB}GB RAM detected."
    fi

    # Check disk space (~20GB needed)
    case "$OS" in
        macos)
            FREE_GB=$(df -g / | tail -1 | awk '{print $4}')
            ;;
        linux|wsl)
            FREE_GB=$(df -BG / | tail -1 | awk '{print $4}' | tr -d 'G')
            ;;
    esac

    if [ "$FREE_GB" -lt 20 ]; then
        err "Only ${FREE_GB}GB free disk space. At least 20GB is needed for the model."
        exit 1
    else
        ok "${FREE_GB}GB free disk space."
    fi

    # Check for cmake and a C++ compiler (needed on Linux)
    if [ "$OS" != "macos" ]; then
        if ! command -v cmake &>/dev/null; then
            warn "cmake not found. Will attempt to install."
        fi
        if ! command -v g++ &>/dev/null && ! command -v c++ &>/dev/null; then
            warn "C++ compiler not found. Will attempt to install build tools."
        fi
    fi
}

# ---------------------------------------------------------------------------
# Install llama.cpp
# ---------------------------------------------------------------------------
install_llamacpp() {
    if command -v llama-server &>/dev/null; then
        ok "llama-server already installed: $(which llama-server)"
        return
    fi

    info "Installing llama.cpp..."

    case "$OS" in
        macos)
            if ! command -v brew &>/dev/null; then
                err "Homebrew not found. Install it first: https://brew.sh"
                exit 1
            fi
            brew install llama.cpp
            ;;

        linux|wsl)
            # Install build dependencies
            if command -v apt-get &>/dev/null; then
                info "Installing build dependencies (apt)..."
                sudo apt-get update -qq
                sudo apt-get install -y -qq build-essential cmake git
            elif command -v dnf &>/dev/null; then
                info "Installing build dependencies (dnf)..."
                sudo dnf install -y gcc-c++ cmake git
            elif command -v pacman &>/dev/null; then
                info "Installing build dependencies (pacman)..."
                sudo pacman -S --noconfirm base-devel cmake git
            else
                err "No supported package manager found (apt, dnf, pacman)."
                err "Please install cmake, git, and a C++ compiler manually."
                exit 1
            fi

            # Build from source
            LLAMA_DIR="$HOME/.local/share/llama.cpp"
            if [ -d "$LLAMA_DIR" ]; then
                info "Updating existing llama.cpp source..."
                cd "$LLAMA_DIR" && git pull
            else
                info "Cloning llama.cpp..."
                git clone https://github.com/ggml-org/llama.cpp "$LLAMA_DIR"
            fi

            cd "$LLAMA_DIR"
            info "Building llama.cpp (this may take a few minutes)..."

            # Detect CUDA
            CMAKE_ARGS=""
            if command -v nvcc &>/dev/null; then
                info "CUDA detected — enabling GPU acceleration."
                CMAKE_ARGS="-DGGML_CUDA=ON"
            fi

            cmake -B build $CMAKE_ARGS -DCMAKE_BUILD_TYPE=Release
            cmake --build build --config Release -j "$(nproc 2>/dev/null || echo 4)"

            # Symlink to PATH
            mkdir -p "$HOME/.local/bin"
            ln -sf "$LLAMA_DIR/build/bin/llama-server" "$HOME/.local/bin/llama-server"
            ln -sf "$LLAMA_DIR/build/bin/llama-cli" "$HOME/.local/bin/llama-cli"

            # Ensure ~/.local/bin is in PATH
            if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
                echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_CONFIG"
                export PATH="$HOME/.local/bin:$PATH"
                info "Added ~/.local/bin to PATH in $SHELL_CONFIG"
            fi
            ;;
    esac

    # Verify
    if command -v llama-server &>/dev/null; then
        ok "llama-server installed successfully."
    else
        err "llama-server installation failed. Please install manually:"
        err "  https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md"
        exit 1
    fi
}

# ---------------------------------------------------------------------------
# Install Claude Code (if not present)
# ---------------------------------------------------------------------------
install_claude_code() {
    if command -v claude &>/dev/null; then
        ok "Claude Code already installed: $(claude --version 2>/dev/null || echo 'installed')"
        return
    fi

    if ! command -v npm &>/dev/null; then
        warn "npm not found. Claude Code requires Node.js."
        warn "Install Node.js from https://nodejs.org/ then run:"
        warn "  npm install -g @anthropic-ai/claude-code"
        return
    fi

    info "Installing Claude Code..."
    npm install -g @anthropic-ai/claude-code
    ok "Claude Code installed."
}

# ---------------------------------------------------------------------------
# Configure environment variables
# ---------------------------------------------------------------------------
configure_env() {
    info "Configuring environment variables for Claude Code..."

    ENVARS=(
        "export ANTHROPIC_AUTH_TOKEN=\"llamacpp\""
        "export ANTHROPIC_BASE_URL=\"http://localhost:${PORT}\""
        "export ANTHROPIC_DEFAULT_SONNET_MODEL=\"${MODEL_NAME}\""
        "export ANTHROPIC_DEFAULT_HAIKU_MODEL=\"${MODEL_NAME}\""
        "export ANTHROPIC_DEFAULT_OPUS_MODEL=\"${MODEL_NAME}\""
    )

    # Set for current session
    for var in "${ENVARS[@]}"; do
        eval "$var"
    done
    ok "Environment variables set for this session."

    # Ask about persisting
    echo ""
    read -rp "Save these to $SHELL_CONFIG for future sessions? [Y/n] " PERSIST
    PERSIST="${PERSIST:-Y}"

    if [[ "$PERSIST" =~ ^[Yy] ]]; then
        echo "" >> "$SHELL_CONFIG"
        echo "# Claude Code + llama.cpp (added by setup-llamacpp.sh)" >> "$SHELL_CONFIG"
        for var in "${ENVARS[@]}"; do
            # Only add if not already present
            if ! grep -qF "$var" "$SHELL_CONFIG" 2>/dev/null; then
                echo "$var" >> "$SHELL_CONFIG"
            fi
        done
        ok "Saved to $SHELL_CONFIG"
    else
        warn "Skipped. You'll need to re-export these variables in each new terminal."
    fi
}

# ---------------------------------------------------------------------------
# Start llama-server
# ---------------------------------------------------------------------------
start_server() {
    info "Starting llama-server..."
    info "Model: $MODEL_HF_REPO (auto-downloads from HuggingFace on first run)"
    info "Context: $CONTEXT_SIZE tokens | Port: $PORT"
    echo ""
    warn "The model download is ~19GB on first run. Subsequent starts use the cached file."
    echo ""

    # Check if port is already in use
    if lsof -ti:"$PORT" &>/dev/null 2>&1 || ss -tlnp 2>/dev/null | grep -q ":$PORT "; then
        warn "Port $PORT is already in use. If llama-server is already running, you're all set."
        warn "Otherwise, stop the process using that port and re-run this script."
        return
    fi

    echo -e "${GREEN}Starting server in the background...${NC}"
    echo "Log file: /tmp/llama-server.log"
    echo ""

    nohup llama-server \
        -hf "$MODEL_HF_REPO" \
        -c "$CONTEXT_SIZE" \
        --jinja \
        --port "$PORT" \
        > /tmp/llama-server.log 2>&1 &

    SERVER_PID=$!
    echo "$SERVER_PID" > /tmp/llama-server.pid
    info "Server PID: $SERVER_PID"

    # Wait for server to be ready
    info "Waiting for server to start (downloading model on first run)..."
    RETRIES=0
    MAX_RETRIES=120  # 10 minutes for first download
    while ! curl -s "http://localhost:${PORT}/health" &>/dev/null; do
        sleep 5
        RETRIES=$((RETRIES + 1))
        if [ $RETRIES -ge $MAX_RETRIES ]; then
            err "Server didn't start within 10 minutes. Check /tmp/llama-server.log"
            exit 1
        fi
        # Show progress every 30 seconds
        if [ $((RETRIES % 6)) -eq 0 ]; then
            info "Still waiting... (${RETRIES}/${MAX_RETRIES} checks, see /tmp/llama-server.log)"
        fi
    done

    ok "llama-server is running at http://localhost:${PORT}"
}

# ---------------------------------------------------------------------------
# Print summary and next steps
# ---------------------------------------------------------------------------
print_summary() {
    echo ""
    echo -e "${GREEN}============================================================${NC}"
    echo -e "${GREEN} Setup complete!${NC}"
    echo -e "${GREEN}============================================================${NC}"
    echo ""
    echo "  Server:  http://localhost:${PORT}"
    echo "  Model:   ${MODEL_NAME} (${MODEL_HF_REPO})"
    echo "  Log:     /tmp/llama-server.log"
    echo ""
    echo -e "  ${BLUE}Next steps:${NC}"
    echo "    1. Clone the workshop repo (if you haven't already):"
    echo "       git clone https://github.com/skillrepos/ccode && cd ccode"
    echo ""
    echo "    2. Start Claude Code:"
    echo "       claude"
    echo ""
    echo "    3. Verify the connection by typing:"
    echo "       What model are you, and can you see the files in this directory?"
    echo ""
    echo -e "  ${YELLOW}To stop the server later:${NC}"
    echo "    kill \$(cat /tmp/llama-server.pid)"
    echo ""
    echo -e "  ${YELLOW}To switch back to Claude's API:${NC}"
    echo "    unset ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL"
    echo "    unset ANTHROPIC_DEFAULT_SONNET_MODEL ANTHROPIC_DEFAULT_HAIKU_MODEL ANTHROPIC_DEFAULT_OPUS_MODEL"
    echo "    claude /login"
    echo ""
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
main() {
    echo ""
    echo -e "${BLUE}=== llama.cpp + Claude Code Setup ===${NC}"
    echo ""

    detect_os
    detect_shell_config
    check_prerequisites
    install_llamacpp
    install_claude_code
    configure_env
    start_server
    print_summary
}

main "$@"
