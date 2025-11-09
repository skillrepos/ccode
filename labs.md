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

![YOLO](./images/ccode32.png?raw=true "YOLO")

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

---


# Lab 3: Built-in Commands and Context Management
**Duration:** 10-12 minutes  
**Difficulty:** Intermediate

## Lab Purpose
Master Claude Code's built-in slash commands for managing conversations, context, and memory. Learn how to effectively manage long coding sessions and optimize token usage.

---

## Step 1: Start Fresh with Claude
**What we're doing:** Beginning a new Claude session to explore commands.  
**Why:** Starting fresh ensures we have a clean context for learning.

**Action:** Start Claude:
```bash
claude
```

---

## Step 2: View Available Commands
**What we're doing:** Discovering all built-in slash commands.  
**Why:** Knowing available commands improves your workflow efficiency.

**Action:** Type:
```
/help
```

Review the list including /clear, /compact, /rewind, /model, and others.

---

## Step 3: Create Some Context
**What we're doing:** Building up conversation history to practice management.  
**Why:** We need content to demonstrate context management commands.

**Action:** Have a multi-turn conversation:
```
1. Create a user.js file with a User class
2. Add methods for getName and setName  
3. Add email validation to the User class
4. Create a test file for the User class
```

Let Claude complete each task to build up context.

---

## Step 4: Check Context Usage
**What we're doing:** Understanding how much context we're using.  
**Why:** Managing context prevents hitting token limits in long sessions.

**Action:** Type:
```
/context
```

You'll see information about current token usage and remaining capacity.


![context command](./images/ccode33.png?raw=true "context command")

---

## Step 5: Compact the Conversation
**What we're doing:** Condensing conversation history while preserving key information.  
**Why:** Compacting extends how long you can work without losing context.

**Action:** Type:
```
/compact Keep the User class implementation details and test structure
```

Claude will summarize earlier parts while keeping specified information.


![compact](./images/ccode36.png?raw=true "compact")

---

## Step 6: Use Rewind Feature
**What we're doing:** Rolling back to a previous state in the conversation.  
**Why:** Rewind lets you undo mistakes or explore different approaches.

**Action:** 
1. Ask Claude: `Delete the test file we created`
2. After deletion, press `Esc` twice or type `/rewind`
3. Select the point before deletion to restore by using the up and down arrow to navigate between the checkpoints listed.


![rewind](./images/ccode34.png?raw=true "rewind")

4. Respond to the clarification question to restore both the code and the conversation.


![rewind](./images/ccode35.png?raw=true "rewind")

---

## Step 7: Switch Models
**What we're doing:** Changing between different Claude models.  
**Why:** Different models offer various speed/capability trade-offs.

**Action:** Type:
```
/model
```

Select a different model (e.g., switch from Opus to Sonnet or vice versa).

![model](./images/ccode37.png?raw=true "model")


![model](./images/ccode38.png?raw=true "model")

---

## Step 8: Create a Project Memory File
**What we're doing:** Setting up a CLAUDE.md file for project context.  
**Why:** CLAUDE.md provides persistent project knowledge across sessions.

**Action:** Type:
```
Create a CLAUDE.md file documenting our User class project structure and testing approach
```

This file will be automatically read in future sessions.

![claude.md](./images/ccode39.png?raw=true "claude.md")

![claude.md](./images/ccode40.png?raw=true "claude.md")

---

## Step 9: Test Memory Persistence
**What we're doing:** Verifying that Claude remembers project context.  
**Why:** Persistent memory improves continuity across sessions.

**Action:**
1. Type `/clear` to clear the conversation
2. Ask: `What's the structure of our User class based on the CLAUDE.md?`

Claude should recall information from the CLAUDE.md file.


![claude.md](./images/ccode42.png?raw=true "claude.md")

---

## Step 10: Create a Session Summary
**What we're doing:** Documenting our work before ending the session.  
**Why:** Summaries help you resume work effectively later.

**Action:** Type:
```
Summarize what we've built today and save it to session-notes.md
```

![session-notes.md](./images/ccode43.png?raw=true "session-notes.md")

![session-notes.md](./images/ccode44.png?raw=true "session-notes.md")

![session-notes.md](./images/ccode45.png?raw=true "session-notes.md")

Then verify with:
```bash
cat session-notes.md
```

---

## Step 11: Advanced Context Trick
**What we're doing:** Using external files to preserve complex context.  
**Why:** This technique helps with very long projects.

**Action:** Type:
```
Save our complete implementation plan and progress to project-state.md, 
```

![project-state.md](./images/ccode45.png?raw=true "project-state.md")

**Action:** Type:
```
/clear
Read project-state.md and continue where we left off
```


![project-state.md](./images/ccode47.png?raw=true "project-state.md")

---

## Lab Summary
✅ You've mastered:
- Using /help to discover commands
- Managing context with /compact
- Undoing changes with /rewind
- Switching models with /model
- Creating persistent memory with CLAUDE.md
- Advanced context preservation techniques

# Lab 4: Creating and Using Custom Commands
**Duration:** 10-12 minutes  
**Difficulty:** Intermediate

## Lab Purpose
Learn how to create custom slash commands to automate repetitive tasks and establish project-specific workflows. Build reusable commands that enhance your development productivity.

---

## Step 1: Create Commands Directory
**What we're doing:** Setting up the folder structure for global and project-specific custom commands.  
**Why:** Claude looks for custom commands in specific directories.

**Action:** In terminal, create the directory:
```bash
mkdir -p ~/.claude/commands
mkdir -p .claude/commands
```

---

## Step 2: Create a Command Template
**What we're doing:** Bringing over a template for future commands.  
**Why:** Templates ensure consistency across team commands.

**Action:** In terminal, copy the *extra/commands/test.md* file to ~/*.claude/commands/test.md*. This defines a new command that accepts a test type argument (unit, integration, or e2e) and generates appropriate tests. After copying it with the first command, open it up to review and understand the structure with the second command. You do not need to make any changes. Close when done.

```bash
cp extra/commands/template.md.example ~/.claude/commands/
code extra/commands/template.md.example
```

----

## Step 3: Add a New Global Command with Arguments
**What we're doing:** Creating a command that accepts parameters.  
**Why:** Parameterized commands are more flexible and reusable.

**Action:** In terminal, copy the *extra/commands/test.md* file to *~/.claude/commands/test.md*. This defines a new command that accepts a test type argument (unit, integration, or e2e) and generates appropriate tests. After copying it with the first command, open it up to review and understand the structure with the second command. You do not need to make any changes. Close when done.

```bash
cp extra/commands/test.md ~/.claude/commands/
code extra/commands/test.md
```

---

## Step 4: Test Your Custom Command
**What we're doing:** Executing the custom command we just created.  
**Why:** Verifying commands work as expected before relying on them.

**Action:** Type:
```
/test
```

Then try with arguments:
```
/test unit
```

---

## Step 4: Add a Git Workflow Command
**What we're doing:** Building a command for common git operations.  
**Why:** Streamlining git workflows reduces context switching.


**Action:** In terminal, copy the *extra/commands/commit.md* file to *~/.claude/commands/commit.md*. This defines a new command that stages changes, runs tests, and creates a *conventional commits* message for the commit. After copying it with the first command, open it up to review and understand the structure with the second command. You do not need to make any changes. Leave it open.

```bash
cp extra/commands/commit.md ~/.claude/commands/
code extra/commands/commit.md
```

---

## Step 5: Preview the file for the Git Workflow Command
** What we're doing:** Previewing the command definition.
** Why:** This version can be easier to read and understand.

**Action:** In the tab at the top of the open *extra/commands/test.md*, right-click and select the *Open Preview* option. This will give you a markdown preview of the contents of the file.

---

## Step 6: Have Claude Code Create a Documentation Command
**What we're doing:** Automating documentation generation.  
**Why:** Consistent documentation improves code maintainability.

**Action:** Start claude again and tell it to create this command with the following prompt:
```
Create .claude/commands/document.md with:
---
description: Generate comprehensive documentation
---
Analyze the file $ARGUMENTS and create:
1. JSDoc/docstring comments
2. README section explaining the module
3. Usage examples
4. API documentation if applicable
```

---

## Step 7: Add a Project-Specific Refactoring Command
**What we're doing:** Creating a command for code improvement.  
**Why:** Systematic refactoring improves code quality.

**Action:** In terminal, copy the *extra/commands/commit.md* file to *.claude/commands/commit.md*. This defines a new project-specific command that helps with refactoring. After copying it with the first command, open it up to review and understand the structure with the second command. You can close it when done.

```bash
cp extra/commands/refactor.md .claude/commands/
code extra/commands/refactor.md
```


---


## Step 8: List and Verify Commands
**What we're doing:** Confirming all custom commands are recognized.  
**Why:** Ensures Claude can discover and use your commands.

**Action:** Type:
```
/help
```

Look for your custom commands marked with "(project)" in the list.

---


## Step 9: Chain Commands Together
**What we're doing:** Using multiple commands in sequence.  
**Why:** Command chaining creates powerful workflows.

**Action:** Try this workflow:
```
1. /refactor index.js
2. /test unit
3. /document index.js
4. /commit
```

---

## Lab Summary
✅ You've learned to:
- Create custom slash commands
- Use arguments in commands
- Build project-specific workflows
- Chain commands for complex tasks
- Organize commands effectively


# Lab 5: Agent Skills and Advanced Features
**Difficulty:** Advanced

## Lab Purpose
Learn to create and use Agent Skills - modular capabilities that extend Claude's functionality with specialized knowledge and scripts. Build skills for document processing, API integration, and domain-specific tasks.

---

## Step 1: Understand Skills vs Commands
**What we're doing:** Learning the key differences between skills and slash commands.  
**Why:** Skills are AI-invoked based on context, while commands are user-invoked.

**Action:** Start Claude and ask:
```
Explain the difference between Agent Skills in .claude/skills/ and slash commands in .claude/commands/
```

---

## Step 2: Create Skills Directory
**What we're doing:** Setting up the folder structure for Agent Skills.  
**Why:** Skills need proper organization for Claude to discover them.

**Action:** In terminal:
```bash
mkdir -p .claude/skills/api-tester/scripts
mkdir -p .claude/skills/database-helper
mkdir -p .claude/skills/code-quality
```

---

## Step 3: Add Your First Skill
**What we're doing:** Adding a skill for API testing and documentation.  
**Why:** Skills package expertise that Claude can use autonomously.

**Action:** In terminal, copy the *extra/skills/api-tester/SKILL.md* file to *.claude/skills/api-tester/SKILL.md*. This defines a new project-specific skill that helps with API testing and documentation by doing the following:

1. Parse the API endpoint and method
2. Construct appropriate headers and body
3. Make the request using curl or fetch
4. Validate response structure
5. Generate documentation in OpenAPI format

After copying it with the first command, open it up to review and understand the structure with the second command. You can close it when done.

```bash
cp extra/skills/api-tester/SKILL.md .claude/skills/api-tester/
code extra/skills/api-tester/SKILL.md
```

## Examples
- Test GET endpoint: curl -X GET "https://api.example.com/users"
- Test POST with JSON: curl -X POST -H "Content-Type: application/json" -d '{"name":"test"}'

---

## Step 4: Add Scripts to Your Skill
**What we're doing:** Including executable scripts within a skill.  
**Why:** Skills can bundle code for complex operations.

**Action:** In terminal, copy the *extra/skills/api-tester/scripts/test-api.py* file to *.claude/skills/api-tester/scripts/test-api.py*. This defines a new script helps with API testing by doing the following:

- Accepts URL and method as arguments
- Makes HTTP requests
- Validates JSON responses
- Returns formatted results

After copying it with the first command, open it up to review and understand the structure with the second command. You can close it when done.

```bash
cp extra/skills/api-tester/scripts/test-api.py .claude/skills/api-tester/scripts/
code extra/skills/api-tester/scripts/test-api.py
```


---

## Step 5: Test Skill Activation
**What we're doing:** Verifying Claude recognizes and uses the skill.  
**Why:** Skills should activate automatically based on context.

**Action:** Without mentioning the skill directly, ask:
```
I need to test this API endpoint: https://jsonplaceholder.typicode.com/posts/1
```

Claude should automatically use your api-tester skill.

---

## Step 6: Have Claude Create a Database Helper Skill
**What we're doing:** Building a skill for database operations.  
**Why:** Complex database tasks benefit from specialized instructions.

**Action:** In Claude code, give it the following prompt:
```
Create .claude/skills/database-helper/SKILL.md for:
- SQL query optimization
- Migration generation
- Schema documentation
- Index recommendations
Include example queries and best practices
```

Afterwards, you can look at the .claude/skills/database-helper/SKILL.md file if you want.

---

## Step 7: Add a Global Code Quality Skill
**What we're doing:** Creating a comprehensive code analysis skill for all projects.  
**Why:** Systematic code review improves project quality.

**Action:** In terminal, copy the *extra/skills/code-quality/SKILL.md* file to  *~/.claude/skills/code-quality/SKILL.md*. This defines a new global skill that helps with ensuring code quality through: 

- Linting rules for multiple languages
- Security scanning patterns
- Performance analysis
- Complexity metrics
- Refactoring suggestions

After copying it with the first command, open it up to review and understand the structure with the second command. You can close it when done.

```bash
cp extra/skills/code-quality/SKILL.md ~/.claude/skills/code-quality/
code extra/skills/code-quality/SKILL.md
```


---

## Step 8: Add Subagents
**What we're doing:** Creating specialized subagents for focused tasks.  
**Why:** Subagents handle specific responsibilities with dedicated context.

**Action:** In terminal, copy the *extra/agents/test-runner.md* file to  *.claude/agents/test-runner.md*. This defines a new project-specific agent to help with running and fixing failing tests. 


After copying it with the first command, open it up to review and understand the structure with the second command. You can close it when done.

```bash
cp extra/agents/test-runner.md .claude/agents/
code extra/agents/test-runner.md
```

---

## Step 9: Configure Hooks
**What we're doing:** Setting up automated actions at specific points.  
**Why:** Hooks enforce standards and automate repetitive checks.

**Action:** Create hooks configuration:
```
Create .claude/hooks.json with:
{
  "preToolUse": [
    {
      "tool": "Edit",
      "command": "echo 'Editing file: $FILE_PATH'"
    }
  ],
  "postToolUse": [
    {
      "tool": "Write",
      "command": "prettier --write $FILE_PATH"
    }
  ]
}
```

---

## Step 10: Test the Complete System
**What we're doing:** Using skills, subagents, and hooks together.  
**Why:** Real workflows combine multiple advanced features.

**Action:** Test with a complex request:
```
Create a REST API for a todo application with:
- CRUD endpoints
- Input validation
- Error handling
- Tests
- API documentation
```

Watch Claude use skills, potentially delegate to subagents, and apply hooks.

---

## Lab Summary
✅ You've mastered:
- Creating Agent Skills with SKILL.md
- Adding scripts to skills
- Building specialized subagents
- Configuring hooks for automation
- Combining advanced features

**Next:** Proceed to Lab 6 for VS Code integration and collaboration features!
