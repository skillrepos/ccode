# AI-Powered Coding with Claude Code
## Learn practical workflows, hands-on coding techniques, and structured interactions
## Session Labs
## Revision 1.0 - 11/08/25

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**Copy and paste may not work as expected if using the mouse. If not, use the keyboard shortcuts - *Ctrl+C/Cmd+C and Ctrl+V/Cmd+V*.**

**Make sure you have the following ready to go.**
- A user account on claude.ai for one of the paid plans
- A GitHub userid on the public GitHub.com


---

# Lab 1: Introduction to Claude Code and Basic Setup
**Duration:** 10-12 minutes  
**Difficulty:** Beginner

## Lab Purpose
Get familiar with Claude Code basic command-line interface. You'll learn how to execute your basic commands in Claude Code.

<br><br>
---

## Step 1: Test Basic Interaction
**What we're doing:** Verifying Claude can respond to simple queries.  
**Why:** This confirms the connection is working properly.

**Action:** At the Claude prompt, type:
```
Hello Claude, can you tell me what you can help with?
```

Claude should respond with information about its capabilities.

---

## Step 2: Ask Claude to Explain a Code Snippet
**What we're doing:** Testing Claude's code understanding capabilities.  
**Why:** Understanding code is a fundamental Claude Code feature.

**Action:** Type the following:
```
Explain this code: console.log([1,2,3].map(x => x * 2))
```

Claude will explain the JavaScript array operation.

---

## Step 3: Create Your First File with Claude
**What we're doing:** Using Claude to generate a simple code file.  
**Why:** File creation is a core feature for development workflows.

**Action:** Type:
```
Create a simple hello.js file that prints "Hello from Claude Code!"
```

Claude will create the file and show you the content.

---

## Step 4: View the Created File
**What we're doing:** Verifying the file was created successfully.  
**Why:** Understanding where Claude saves files is important.

**Action:** In a new terminal tab (keep Claude running), type:
```bash
ls -la
cat hello.js
```

You should see your new file and its contents.

---

## Step 5: Ask Claude to Run the File
**What we're doing:** Having Claude execute the code it created.  
**Why:** Claude can run commands and show output directly.

**Action:** Back in Claude, type:
```
Run the hello.js file we just created
```

You'll see the output: "Hello from Claude Code!"

---

## Step 6: Use the Help Command
**What we're doing:** Exploring available slash commands.  
**Why:** Slash commands provide quick access to common operations.

**Action:** Type:
```
/help
```

Review the list of available commands like /clear, /compact, etc.

---

## Step 7: Exit and Resume
**What we're doing:** Learning how to properly exit and resume sessions.  
**Why:** You'll often need to pause and continue work later.

**Action:** 
1. Type `exit` or press `Ctrl+D` to exit Claude
2. Restart with: `claude --resume`
3. Claude will restore your previous session context

---

## Lab Summary
✅ You've successfully:
- Verified Claude Code installation
- Authenticated your account
- Created and executed code with Claude
- Learned basic navigation and commands
- Practiced session management



# Lab 2: Working with Claude Code Modes
**Difficulty:** Beginner

## Lab Purpose
Master Claude Code's different operating modes including default mode, plan mode, and auto-accept mode. Learn when and how to use each mode effectively for different development scenarios.

---

## Step 1: Understand Default Mode
**What we're doing:** Starting Claude in its standard interactive mode.  
**Why:** Default mode gives you full control with permission prompts for each action.

**Action:** Start Claude normally:
```bash
claude
```

You're now in default mode where Claude asks permission before file changes.

---

## Step 2: Test Default Mode Permissions
**What we're doing:** Creating a file to see permission prompts in action.  
**Why:** Understanding permission flow helps you maintain control over changes.

**Action:** Type:
```
Create a config.json file with database connection settings
```

Notice how Claude asks permission before creating the file. Type `y` to accept.


![Creating config.json](./images/ccode24.png?raw=true "Creating config.json")

---

## Step 3: Activate Plan Mode
**What we're doing:** Switching to Plan Mode for complex task planning.  
**Why:** Plan Mode helps Claude think through multi-step tasks before executing.

**Action:** Press `Shift+Tab` until you see *Plan mode*

<br><br>

---
## Step 4: Prompt for a complex task
**What we're doing:** Prompting Claude for complex task planning.  
**Why:** Plan Mode helps Claude think through multi-step tasks before executing.

**Action:** Type:

```
Create a complete user authentication system with login, signup, and password reset
```

Claude will create a detailed plan before starting implementation.

---

## Step 5: Respond to questions
**What we're doing:**  Responding to questions from Claude
**Why:** Claude needs our input on some things before proceeding.

**Action:** Read any questions that come up and select number of answer to proceed.

![Responding to questions](./images/ccode26.png?raw=true "Responding to questions")


![Responding to questions](./images/ccode27.png?raw=true "Responding to questions")


![Responding to questions](./images/ccode28.png?raw=true "Responding to questions")

---

## Step 6: Review and Modify the Plan
**What we're doing:** Interacting with Claude's proposed plan.  
**Why:** You can review plans before execution to ensure desired outcomes.

**Action:** After Claude presents the plan, select option 1 to proceed and auto-accept edits.

![Reviewing plan](./images/ccode29.png?raw=true "Reviewing plan")

---

## Step 7: Clear the Conversation
**What we're doing:** Using /clear to start fresh.  
**Why:** Clearing context helps when switching between unrelated tasks.

**Action:** Type:
```
/clear
```

Your conversation history is now cleared, giving you a clean slate.

---

## Step 8: Try Edit Mode (Auto-Accept)
**What we're doing:** Running Claude with automatic permission granting.  
**Why:** This speeds up development when you trust Claude's actions.

**Action:** Exit Claude (`exit`), then restart with:
```bash
claude --dangerously-skip-permissions
```

⚠️ **Note:** Use with caution! Claude won't ask before making changes.

---

## Step 9: Test Auto-Accept Mode
**What we're doing:** Creating multiple files without interruption.  
**Why:** See how much faster development is without permission prompts.

**Action:** Type:
```
Create a simple Express.js API with routes for users and products
```

Notice Claude creates all files without asking for permission.

---

## Step 9: Use Headless Mode for Scripts
**What we're doing:** Running Claude in non-interactive mode.  
**Why:** Headless mode is perfect for automation and CI/CD pipelines.

**Action:** Exit Claude and run:
```bash
claude -p "List all JavaScript files in the current directory"
```

Claude executes and returns results without entering interactive mode.

---

## Step 10: Pipe Data to Claude
**What we're doing:** Sending data directly to Claude via pipes.  
**Why:** This enables powerful command-line integrations.

**Action:** In terminal, type:
```bash
echo "function broken() { return }" | claude -p "Fix any syntax errors in this JavaScript"
```

Claude will analyze and fix the code directly.

---

## Step 11: Combine Modes Effectively
**What we're doing:** Using different modes for a complete workflow.  
**Why:** Different tasks benefit from different modes.

**Action:** Try this workflow:
1. Start with Plan Mode (`Shift+Tab Tab`) for architecture
2. Switch to default mode for careful implementation
3. Use headless mode (`-p`) for quick fixes
4. Document your approach

**Action:** In terminal, type:  
```
Create a MODES.md file explaining when to use each Claude Code mode
```

---

## Lab Summary
✅ You've successfully learned:
- Default mode with permission prompts
- Plan mode for complex task planning
- Auto-accept mode for rapid development
- Headless mode for automation
- How to combine modes effectively
