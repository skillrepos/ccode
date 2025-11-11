# AI-Powered Coding with Claude Code
## Learn practical workflows, hands-on coding techniques, and structured interactions
## Session Labs
## Revision 3.0 - 11/11/25

<br><br>

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**Copy and paste may not work as expected if using the mouse. If not, use the keyboard shortcuts - *Ctrl+C/Cmd+C and Ctrl+V/Cmd+V*.**

**Make sure you have the following ready to go.**
- A user account on claude.ai for one of the paid plans
- A GitHub userid on the public GitHub.com


---
<br><br>

# Lab 1: Introduction to Claude Code and Basic Setup
## Lab Purpose
Get familiar with Claude Code basic command-line interface. You'll learn how to execute your basic commands in Claude Code.

---
<br><br>

## 1: Test Basic Interaction
**What we're doing:** Verifying Claude can respond to simple queries.  
**Why:** This confirms the connection is working properly.

**Action:** At the Claude prompt, type the prompt below and hit *Enter*. While that is running, hit *Ctrl+o* to have Claude show its thinking process.
```
Hello Claude, can you tell me what you can help with?
```

Claude should respond with information about its capabilities preceded by its thinking process.

![Initial prompt](./images/ccode84.png?raw=true "Initial prompt")


---
<br><br>

## 2: Ask Claude to Explain a Code Snippet
**What we're doing:** Testing Claude's code understanding capabilities.  
**Why:** Understanding code is a fundamental Claude Code feature.

**Action:** Type the following:
```
Explain this code: console.log([1,2,3].map(x => x * 2))
```

Claude will explain the JavaScript array operation.

![Initial prompt](./images/ccode85.png?raw=true "Initial prompt")

---
<br><br>

## 3: Create Your First File with Claude
**What we're doing:** Using Claude to generate a simple code file.  
**Why:** File creation is a core feature for development workflows.

**Action:** Type:
```
Create a simple hello.js file that prints "Hello from Claude Code!"
```

Claude will create the file and show you the content in the diff above the terminal. You do not need to do anything in the diff area. Just select option 1 in the terminal where Claude is waiting.

![Initial file creation](./images/ccode86.png?raw=true "Initial file creation")

---
<br><br>

## 4: View the Created File
**What we're doing:** Verifying the file was created successfully.  
**Why:** Understanding where Claude saves files is important.

**Action:** The file should be created and the diff closed. You can click on the file on the left to see the contents. Or, alternatively, in a new terminal tab (keep Claude running), type:
```bash
ls -la
cat hello.js
```

You should see your new file and its contents.

![Initial file creation](./images/ccode87.png?raw=true "Initial file creation")

---
<br><br>

## 5: Ask Claude to Run the File
**What we're doing:** Having Claude execute the code it created.  
**Why:** Claude can run commands and show output directly.

**Action:** Back in Claude, type the prompt below. You'll see the run started and then you'll be prompted for permission to proceed. Just select option 1.
```
Run the hello.js file we just created
```

![Run file](./images/ccode88.png?raw=true "Run file")

You'll see the output: "Hello from Claude Code!"

![Run file](./images/ccode89.png?raw=true "Run file")

---
<br><br>

## 6: Exit and Resume
**What we're doing:** Learning how to properly exit and resume sessions.  
**Why:** You'll often need to pause and continue work later.

**Action:** 
1. Type `exit` or press `Ctrl+D` to exit Claude
2. Restart with: `claude --resume`
3. You'll see a list with your session. Just hit *Enter* to resume.
4. Claude will restore your previous session context

![Restore](./images/ccode91.png?raw=true "Restore")

---
<br><br>

## 7: Creating a second file
**What we're doing:** Creating a second file for additional context.  
**Why:** We want to learn more about resume.

**Action:** Type the following. When you are prompted to continue, select option 3 to tell Claude to do something different.
```
Create a simple goodbye.js file that prints "Goodbye from Claude Code!"
```

Claude will create the file and show you the content in the diff above the terminal. You do not need to do anything in the diff area. Just select option 3 in the terminal where Claude is waiting.

![Do something different](./images/ccode92.png?raw=true "Do something different")


---
<br><br>

## 8: Redo
**What we're doing:** Redoing our command.  
**Why:** We want to learn how to do redo a request.

**Action:** You'll see the previous rejected operation message above the prompt area. Use the <up arrow> key to bring up the last prompt. Change the name of the file in the prompt from *goodbye.js* to *goodbye.py* to create a Python file instead. Hit *Enter*.
```
Create a simple goodbye.py file that prints "Goodbye from Claude Code!"
```

Claude will create the file and show you the content in the diff above the terminal. Once Claude generates it and prompts whether to continue, select 1 to proceed.

---
<br><br>

## 9: Exit

**Action:** In prep for the next lab and a fresh start, type `exit` to exit Claude Code.

```
exit
```

## Lab Summary
✅ You've successfully:
- Verified Claude Code installation
- Authenticated your account
- Created and executed code with Claude
- Learned basic navigation and commands
- Practiced session management

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 2: Working with Claude Code Modes
## Lab Purpose
Master Claude Code's different operating modes including default mode, plan mode, and auto-accept mode. Learn when and how to use each mode effectively for different development scenarios.

---
<br><br>

## 1: Understand Default Mode and Enable YOLO mode
**What we're doing:** Starting Claude in its standard interactive mode but with support to use YOLO.  
**Why:** Default mode gives you full control with permission prompts for each action.

**Action:** Start Claude with the flag to enable YOLO in the future:
```bash
claude --allow-dangerously-skip-permissions 
```

You're now in default mode where Claude asks permission before file changes.

---
<br><br>

## 2: Test Default Mode Permissions
**What we're doing:** Creating a file to see permission prompts in action.  
**Why:** Understanding permission flow helps you maintain control over changes.

**Action:** Type:
```
Create a config.json file with database connection settings
```

Notice how Claude asks permission before creating the file as we've seen before. Type `1` to accept.


![Creating config.json](./images/ccode24.png?raw=true "Creating config.json")

---
<br><br>

## 3: Activate Plan Mode
**What we're doing:** Switching to Plan Mode for complex task planning.  
**Why:** Plan Mode helps Claude think through multi-step tasks before executing.

**Action:** Press `Shift+Tab` until you see *Plan mode*

![Activating plan mode](./images/ccode96.png?raw=true "Activating plan mode")


---
<br><br>

## 4: Prompt for a complex task
**What we're doing:** Prompting Claude for complex task planning.  
**Why:** Plan Mode helps Claude think through multi-step tasks before executing.

**Action:** Type:

```
Create a basic user profile page with fields for name, email, and profile picture upload. 
```

![Planning](./images/ccode98.png?raw=true "Planning")

Claude will start creating a detailed plan before starting implementation.

---
<br><br>

## 5: Respond to questions
**What we're doing:**  Responding to questions from Claude
**Why:** Claude needs our input on some things before proceeding.

**Action:** Read any questions that come up and select number of answer to proceed if single option for answer. If you can select multiple options, use arrow keys and space/Enter to select options. Then move on to next question using right arrow. Answer all questions and then move to *Submit* and press *Enter*. 

![Responding to questions](./images/ccode99.png?raw=true "Responding to questions")


![Responding to questions](./images/ccode100.png?raw=true "Responding to questions")


---
<br><br>

## 6: Review the Plan
**What we're doing:** Interacting with Claude's proposed plan.  
**Why:** You can review plans before execution to ensure desired outcomes.

**Action:** After Claude presents the plan, you could modify it if you wanted by selecting *CTRL+G*. 
1. Go ahead and select that key sequence to bring the plan up in the editor.
2. After you're done reviewing it, you can close the file.
3. Then select option 1 to proceed and auto-accept edits.

![Reviewing plan](./images/ccode102.png?raw=true "Reviewing plan")

![Approving plan](./images/ccode101.png?raw=true "Approving plan")

**Note that you are now in *accept edits on* mode, but the original task will still run under *plan* mode.**

---
<br><br>

## 7: View to-do list
**What we're doing:** Monitoring the progress through the to-do list.  
**Why:** Helps you understand what is done and what is left to be done.

**Action:** While Claude Code is doing the implementation, hit *CTRL+T* to see the current state of the to-do list.

```
ctrl+t
```

![Viewing to-do list](./images/ccode103.png?raw=true "Viewing to-do list")

---
<br><br>

## 8: When done, clear the Conversation
**What we're doing:** Using /clear to start fresh.  
**Why:** Clearing context helps when switching between unrelated tasks.

After a few minutes, Claude Code will be done and provide you a summary. It may ask if you want it to do additional tasks, but you can just ignore those.

![Plan completed](./images/ccode104.png?raw=true "Plan completed")

Now, let's clear the context.

**Action:** Type:
```
/clear
```

Your conversation history is now cleared, giving you a clean slate.

---
<br><br>

## 9: Try YOLO Mode (Auto-Accept)
**What we're doing:** Running Claude with automatic permission granting.  
**Why:** This speeds up development when you trust Claude's actions.

**Action:** Exit Claude (`exit`), then restart with the command below and use option 2 to accept the risk:

```bash
claude --dangerously-skip-permissions
```
Because we started claude with the option to use YOLO in step 1, when we start it with this flag, it starts up in **bypass permissions on** mode.

We also have an alias for this that you can use in the future `claude-yolo`.

⚠️ **Note:** Use with caution! Claude won't ask before making changes.

![YOLO](./images/ccode123.png?raw=true "YOLO")

---
<br><br>

## 10: Test Auto-Accept Mode
**What we're doing:** Creating multiple files without interruption.  
**Why:** See how much faster development is without permission prompts.

**Action:** Type:
```
Create a simple To-Do list app wtih functionality to add and delete tasks
```

Notice Claude creates all files without asking for permission.

![YOLO](./images/ccode106.png?raw=true "YOLO")

---
<br><br>

## 11: Use Headless Mode for Scripts
**What we're doing:** Running Claude in non-interactive mode.  
**Why:** Headless mode is perfect for automation and CI/CD pipelines.

**Action:** Exit Claude and run:
```bash
claude -p "List all JavaScript files in the current directory"
```

Claude executes and returns results without entering interactive mode.

![headless](./images/ccode107.png?raw=true "headless")

---
<br><br>

## 12: Pipe Data to Claude
**What we're doing:** Sending data directly to Claude via pipes.  
**Why:** This enables powerful command-line integrations.

**Action:** In terminal, type:
```bash
echo "function broken() { return }" | claude -p "Fix any syntax errors in this JavaScript"
```

Claude will analyze and fix the code directly.

![headless](./images/ccode108.png?raw=true "headless")

---
<br><br>

## Lab Summary
✅ You've successfully learned:
- Default mode with permission prompts
- Plan mode for complex task planning
- Auto-accept mode for rapid development
- Headless mode for automation
- How to combine modes effectively

---

<br><br>
---
## END OF LAB
---
<br><br>

---
### NOTE: From here on, you can use the `claude --dangerously-skip-permissions` mode if you want to avoid having to respond to most prompts. For convenience, if working in the codespace, there is a shortcut alias for this setup:  `claude-yolo`.
---
<br><br>

# Lab 3: Built-in Commands and Context Management
## Lab Purpose
Master Claude Code's built-in slash commands for managing conversations, context, and memory. Learn how to effectively manage long coding sessions and optimize token usage.

---
<br><br>

## 1: Start Fresh with Claude
**What we're doing:** Beginning a new Claude session to explore commands.  
**Why:** Starting fresh ensures we have a clean context for learning.

**Action:** Start Claude:
```bash
claude
```

---
<br><br>

## 2: View Available Commands
**What we're doing:** Discovering all built-in slash commands.  
**Why:** Knowing available commands improves your workflow efficiency.

**Action:** Type:
```
/help
```

This will bring up a set of *tabbed* output for help. Use the *tab* key to get to the *commands* section at the top. Then you can use the arrow keys to move up and down to see all the commands.
Review the list including /clear, /compact, /rewind, /model, and others.

![help to see commands](./images/ccode109.png?raw=true "help to see commands")

Use *Esc* to exit when done.

---
<br><br>

## 3: Create Some Context
**What we're doing:** Building up conversation history to practice management.  
**Why:** We need content to demonstrate context management commands.

**Action:** Have a multi-turn conversation. Type each of the following into the prompt area one at a time:
```
1. Create a user.js file with a User class
2. Add methods for getName and setName  
3. Add email validation to the User class
4. Create a test file for the User class
```

Let Claude complete each task to build up context.

---
<br><br>

## 4: Check Context Usage
**What we're doing:** Understanding how much context we're using.  
**Why:** Managing context prevents hitting token limits in long sessions.

**Action:** Type:
```
/context
```

You'll see information about current token usage and remaining capacity.


![context command](./images/ccode33.png?raw=true "context command")

---
<br><br>

## 5: Compact the Conversation
**What we're doing:** Condensing conversation history while preserving key information.  
**Why:** Compacting extends how long you can work without losing context.

**Action:** Type:
```
/compact Keep the User class implementation details and test structure
```

Claude will summarize earlier parts while keeping specified information.


![compact](./images/ccode36.png?raw=true "compact")

---
<br><br>

## 6: Use Rewind Feature
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
<br><br>

## 7: Switch Models
**What we're doing:** Changing between different Claude models.  
**Why:** Different models offer various speed/capability trade-offs.

**Action:** Type:
```
/model
```

Select a different model if you want or just leave it at the default. Opus is not recommended because it will use your rate limits faster.

![model](./images/ccode37.png?raw=true "model")


![model](./images/ccode38.png?raw=true "model")

---
<br><br>

## 8: Create a Project Memory File
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
<br><br>

## 9: Test Memory Persistence
**What we're doing:** Verifying that Claude remembers project context.  
**Why:** Persistent memory improves continuity across sessions.

**Action:**
1. Type `/clear` to clear the conversation
2. Ask: `What's the structure of our User class based on the CLAUDE.md?`

Claude should recall information from the CLAUDE.md file.


![claude.md](./images/ccode42.png?raw=true "claude.md")

---
<br><br>

## 10: Create a Session Summary
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
<br><br>

## 11: (Optional if you have time) Advanced Context Trick
**What we're doing:** Using external files to preserve complex context.  
**Why:** This technique helps with very long projects.

**Action:** Type:
```
Save our complete implementation plan and progress to project-state.md 
```

![project-state.md](./images/ccode45.png?raw=true "project-state.md")

**Action:** Type:
```
/clear
Read project-state.md and continue where we left off
```


![project-state.md](./images/ccode47.png?raw=true "project-state.md")

---
<br><br>

## Lab Summary
✅ You've mastered:
- Using /help to discover commands
- Managing context with /compact
- Undoing changes with /rewind
- Switching models with /model
- Creating persistent memory with CLAUDE.md
- Advanced context preservation techniques


<br><br>
---
## END OF LAB
---
<br><br>

# Lab 4: Creating and Using Custom Commands
## Lab Purpose
Learn how to create custom slash commands to automate repetitive tasks and establish project-specific workflows. Build reusable commands that enhance your development productivity.

---
<br><br>

## 1: Create Commands Directory
**What we're doing:** Setting up the folder structure for global and project-specific custom commands.  
**Why:** Claude looks for custom commands in specific directories.

**Action:** In terminal, create the directory:
```bash
mkdir -p ~/.claude/commands
mkdir -p .claude/commands
```

---
<br><br>

## 2: Create a Command Template
**What we're doing:** Bringing over a template for future commands.  
**Why:** Templates ensure consistency across team commands.

**Action:** In terminal, copy the *extra/commands/test.md* file to ~/*.claude/commands/test.md*. This defines a new command that accepts a test type argument (unit, integration, or e2e) and generates appropriate tests. After copying it with the first command, open it up to review and understand the structure with the second command. You do not need to make any changes. Close when done.

```bash
cp extra/commands/test.md ~/.claude/commands/
code extra/commands/test.md
```

----
<br><br>

## 3: Add a New Global Command with Arguments
**What we're doing:** Creating a command that accepts parameters.  
**Why:** Parameterized commands are more flexible and reusable.

**Action:** In terminal, copy the *extra/commands/test.md* file to *~/.claude/commands/test.md*. This defines a new command that accepts a test type argument (unit, integration, or e2e) and generates appropriate tests. After copying it with the first command, open it up to review and understand the structure with the second command. You do not need to make any changes. Close when done.

```bash
cp extra/commands/test.md ~/.claude/commands/
code extra/commands/test.md
```

---
<br><br>

## 4: Test Your Custom Command
**What we're doing:** Executing the custom command we just created.  
**Why:** Verifying commands work as expected before relying on them.

**Action:** Type:
```
/test
```

![Test command](./images/ccode49.png?raw=true "Test command")

Then try with arguments:
```
/test unit
```


![Test command](./images/ccode111.png?raw=true "Test command")

**This step will take a long time to run. You do NOT need to wait for this to finish to continue. While this is running, you can open another terminal and proceed with the next step.**

---
<br><br>

## 4: Add a Git Workflow Command
**What we're doing:** Building a command for common git operations.  
**Why:** Streamlining git workflows reduces context switching.


**Action:** In terminal, copy the *extra/commands/commit.md* file to *~/.claude/commands/commit.md*. This defines a new command that stages changes, runs tests, and creates a *conventional commits* message for the commit. After copying it with the first command, open it up to review and understand the structure with the second command. You do not need to make any changes. Leave it open.

```bash
cp extra/commands/commit.md ~/.claude/commands/
code extra/commands/commit.md
```

---
<br><br>

## 5: Preview the file for the Git Workflow Command
**What we're doing:** Previewing the command definition.
**Why:** This version can be easier to read and understand.

**Action:** In the tab at the top of the open *extra/commands/test.md*, right-click and select the *Open Preview* option. This will give you a markdown preview of the contents of the file.

![Preview command](./images/ccode110.png?raw=true "Preview command")

![Preview command](./images/ccode112.png?raw=true "Preview command")

---
<br><br>

## 6: Have Claude Code Create a Documentation Command
**What we're doing:** Automating documentation generation.  
**Why:** Consistent documentation improves code maintainability.

**Action:** Start claude (if needed) and tell it to create this command with the following prompt:
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


![Completed command](./images/ccode54.png?raw=true "Completed command")

---
<br><br>

## 7: Add a Project-Specific Refactoring Command
**What we're doing:** Creating a command for code improvement.  
**Why:** Systematic refactoring improves code quality.

**Action:** In terminal, copy the *extra/commands/commit.md* file to *.claude/commands/commit.md*. This defines a new project-specific command that helps with refactoring. After copying it with the first command, open it up to review and understand the structure with the second command. You can close it when done.

```bash
cp extra/commands/refactor.md .claude/commands/
code extra/commands/refactor.md
```

---
<br><br>

## 8: List and Verify Commands
**What we're doing:** Confirming all custom commands are recognized.  
**Why:** Ensures Claude can discover and use your commands.

**Action:** Exit Claude and start it again. Then type:
```
/help
```

Look for your custom commands under the *custom-commands* option in the displayed list. Use *Tab* to get to different sections.


![Showing custom commands](./images/ccode56.png?raw=true "Showing custom commands")

---
<br><br>

## (Optional to do later) Chain Commands Together
**What we're doing:** Using multiple commands in sequence.  
**Why:** Command chaining creates powerful workflows.

**Action:** Try this workflow:
```
1. /refactor user.js
2. /test unit
3. /document user.js
4. /commit
```

---
<br><br>

## Lab Summary
✅ You've learned to:
- Create custom slash commands
- Use arguments in commands
- Build project-specific workflows
- Chain commands for complex tasks
- Organize commands effectively


<br><br>
---
## END OF LAB
---
<br><br>

# Lab 5: Agent Skills and Advanced Features
## Lab Purpose
Learn to create and use Agent Skills - modular capabilities that extend Claude's functionality with specialized knowledge and scripts. Build skills for document processing, API integration, and domain-specific tasks.

---
<br><br>

## 1: Understand Skills vs Commands
**What we're doing:** Learning the key differences between skills and slash commands.  
**Why:** Skills are AI-invoked based on context, while commands are user-invoked.

**Action:** In Claude, ask:
```
Explain the difference between Agent Skills in .claude/skills/ and slash commands in .claude/commands/
```

![Explain difference](./images/ccode58.png?raw=true "Explain difference")

---
<br><br>

## 2: Create Skills Directory
**What we're doing:** Setting up the folder structure for Agent Skills.  
**Why:** Skills need proper organization for Claude to discover them.

**Action:** In a terminal:
```bash
mkdir -p .claude/skills/api-tester/scripts
mkdir -p .claude/skills/database-helper
mkdir -p .claude/skills/code-quality
mkdir -p .claude/agents
```

---
<br><br>

## 3: Add Your First Skill
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

---
<br><br>

## 4: Add Scripts to Your Skill
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
<br><br>

## 5: Test Skill Activation
**What we're doing:** Verifying Claude recognizes and uses the skill.  
**Why:** Skills should activate automatically based on context.

**Action:** Exit Claude and then start it again. Without mentioning the skill directly, ask:
```
I need to test this API endpoint: https://jsonplaceholder.typicode.com/posts/1
```

Claude may automatically use your api-tester skill, or...


![Testing skill activation](./images/ccode62.png?raw=true "Testing skill activation")

... it may ask for approval. If it asks for approval, just use option 2 so it doesn't ask again.

![Testing skill activation](./images/ccode113.png?raw=true "Testing skill activation")

You can observe as it proceeds to use the new skill to test the API.

---
<br><br>

## 6: Have Claude Create a Database Helper Skill
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

**You do not need to wait till this is completed to proceed. You can switch to another terminal and go to step 7.**

---
<br><br>

## 7: Add Subagents
**What we're doing:** Creating specialized subagents for focused tasks.  
**Why:** Subagents handle specific responsibilities with dedicated context.

**Action:** In terminal, copy the *extra/agents/test-runner.md* file to  *.claude/agents/test-runner.md*. This defines a new project-specific agent to help with running and fixing failing tests. 


After copying it with the first command, open it up to review and understand the structure with the second command. You can close it when done.

```bash
cp extra/agents/test-runner.md .claude/agents/
code extra/agents/test-runner.md
```

---
<br><br>

## 8: Configure Hooks
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

![Configuring hooks](./images/ccode64.png?raw=true "Configuring hooks")

---
<br><br>

## Optional (to do when time allows and all other steps have completed): Test the Complete System
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


![Complete system](./images/ccode66.png?raw=true "Complete system")

![Complete system](./images/ccode65.png?raw=true "Complete system")

---
<br><br>

## Lab Summary
✅ You've mastered:
- Creating Agent Skills with SKILL.md
- Adding scripts to skills
- Building specialized subagents
- Configuring hooks for automation
- Combining advanced features


<br><br>
---
## END OF LAB
---
<br><br>


# Lab 6: VS Code Integration and Team Collaboration
## Lab Purpose
Set up Claude Code's VS Code extension, configure team workflows, and establish best practices for collaborative development with Claude Code.

---
<br><br>

## 1: Open VS Code Extension
**What we're doing:** Opening Claude Code directly in your IDE.  
**Why:** The extension provides visual feedback and seamless integration.

**Action:** In the upper right of the main Codespace frame, find the orange Claude symbol and click on it to open the extension view:

![Open view](./images/ccode114.png?raw=true "Open view")

---
<br><br>

## 2: Review Extension Settings
**What we're doing:** Reviewing the extension's settings.  
**Why:** Proper configuration improves the development experience.

**Action:** Open VS Code settings:
1. **Click on** the *gear* icon in the lower left of the Codespace interface and select *Settings* from the menu.
2. In the *Settings* tab in the editor, search for "Claude Code"
3. Review the settings. You don't need to change anything.

![Open Settings](./images/ccode115.png?raw=true "Open Settings")

![Find Settings](./images/ccode116.png?raw=true "Find Settings")

---
<br><br>

## 3: Prompt with Implied Context
**What we're doing:** Prompting Claude within the IDE interface.  
**Why:** IDE integration provides better context awareness.

**Action:** Type: `Hello Claude, what files are in my current workspace?`

![Files in workspace](./images/ccode67.png?raw=true "Files in workspace")


---
<br><br>

## 4: Use Plan Mode in VS Code
**What we're doing:** Activating visual Plan Mode in the extension.  
**Why:** Visual planning helps understand complex changes.

**Action:** In the Claude sidebar:
1. Turn *Thinking* on by clicking on the small icon that looks like a clock in the bottom row of the chat input.
2. Activate *Plan mode* by clicking on the *mode* setting in the lower left of the chat input section.
3. Ask: `Plan a RESTful API for a blog system with posts, comments, and users`
4. Watch Claude's thinking process in real-time

![Plan blog API](./images/ccode119.png?raw=true "Plan blog API")

![Plan blog API](./images/ccode118.png?raw=true "Plan blog API")

This will likely take longer than you want to wait, so you can stop it after it runs for a bit by hitting the (now) square submit button or, if it is prompting you for input, just type "stop".

---
<br><br>

## 5: Enable Auto-Accept Edits
**What we're doing:** Allowing Claude to make changes without prompts.  
**Why:** This speeds up iterative development significantly.

**Action:** 
1. Click on the *mode* setting in the lower left of the chat input section until it gets to "Edit automatically".
2. Ask: `Create a simple Express server in server.js`
3. Watch changes apply automatically in your editor


![Enable auto-accept edits](./images/ccode72.png?raw=true "Enable auto-accept edits")

Even with *Edit automatically* set, Claude may still decide to create a plan first and have you approve it. If it does, and you're good with the plan, you can just click one of the *Yes* options.

![Review plan](./images/ccode120.png?raw=true "Review plan")

---
<br><br>

## 6: Create Team Configuration
**What we're doing:** Setting up shared configuration for team consistency.  
**Why:** Teams need standardized Claude Code settings.

**Action:** Open a new chat session with the "+" sign in the upper right of the VS Code extension area. Then have Claude create:
```
Create .claude/team-config.json with:
{
  "projectName": "Team Training Project",
  "defaultModel": "claude-sonnet-4-5",
  "autoAccept": false,
  "customCommands": ["review", "test", "deploy"],
  "requiredSkills": ["api-tester", "code-quality"],
  "codeStyle": {
    "language": "javascript",
    "formatter": "prettier",
    "linter": "eslint"
  }
}
```

![create team config](./images/ccode121.png?raw=true "Create team config")

You may be prompted to allow some accesses.

![create team config](./images/ccode122.png?raw=true "Create team config")

---
<br><br>

## 7: Create Shared Knowledge Base
**What we're doing:** Building documentation for team-wide Claude use.  
**Why:** Shared knowledge improves team efficiency.

**Action:** Create:
```
Create CLAUDE-TEAM.md with:
1. Project architecture overview
2. API design patterns we follow
3. Testing requirements
4. Deployment process
5. Common troubleshooting steps
6. Links to important documentation
```

---
<br><br>

## 8: Document Team Workflow
**What we're doing:** Creating a guide for team Claude Code usage.  
**Why:** Clear workflows prevent confusion and ensure consistency.

**Action:** Create:
```
Create CLAUDE-WORKFLOW.md documenting:
1. When to use Claude vs manual coding
2. Review process for Claude-generated code
3. Testing requirements
4. Skill creation approval process
5. Best practices for prompting
6. Security considerations
```

---
<br><br>

## Lab Summary
✅ You've accomplished:
- VS Code extension configuration
- Visual Plan Mode and auto-accept features
- Team configuration setup
- Shared knowledge base creation
- Workflow documentation

**Congratulations!** You've completed all labs and are ready to use Claude Code effectively in your development workflow!

## Next Steps
- Practice creating project-specific skills
- Experiment with MCP server integrations
- Build custom workflows for your team
- Explore advanced hook configurations


<br><br>
---
## END OF LAB
---
<br><br>
