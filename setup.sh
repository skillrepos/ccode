#!/bin/bash

echo "Setting up Claude Code Training Environment..."

# Install Claude Code CLI
echo "Installing Claude Code CLI..."
npm install -g @anthropic-ai/claude-code

# Create directories for labs
mkdir -p /workspace/labs/{lab1,lab2,lab3,lab4,lab5,lab6}
mkdir -p ~/.claude/commands
mkdir -p ~/.claude/skills

# Create sample files for labs
echo "Creating sample project files..."
cat > /workspace/sample-project/package.json << 'EOF'
{
  "name": "sample-project",
  "version": "1.0.0",
  "description": "Sample project for Claude Code training",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "MIT"
}
EOF

cat > /workspace/sample-project/index.js << 'EOF'
// Sample JavaScript file with intentional issues for Lab 3
function calculate_sum(a, b) {
    return a + b
}

function findMax(numbers) {
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > max)
            max = numbers[i];
    }
    return max;
}

console.log("Sample application ready!");
EOF

cat > /workspace/sample-project/README.md << 'EOF'
# Sample Project

This is a sample project for Claude Code training exercises.

## Features
- Basic JavaScript functions
- Intentional code style issues for training
- Simple structure for learning

## Usage
Run `node index.js` to execute the sample code.
EOF

# Create a sample Python file with bugs for Lab 4
cat > /workspace/sample-project/calculator.py << 'EOF'
# Sample Python calculator with intentional bugs

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Bug: No zero division check
    return a / b

def calculate_average(numbers):
    # Bug: Doesn't handle empty list
    total = sum(numbers)
    return total / len(numbers)

if __name__ == "__main__":
    print("Calculator module loaded")
    # Test with problematic input
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
EOF

echo "Setup complete! Claude Code training environment is ready."
echo ""
echo "Quick start:"
echo "1. Run 'claude --version' to verify installation"
echo "2. Run 'claude' to start Claude Code"
echo "3. Navigate to /workspace/labs to begin the exercises"
