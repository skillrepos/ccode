# AI-Powered Coding with Claude Code
## Learn practical workflows, hands-on coding techniques, and structured interactions
## Session Labs
## Revision 4.9 - 02/24/26

<br><br>

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**Copy and paste may not work as expected if using the mouse. If not, use the keyboard shortcuts - *Ctrl+C/Cmd+C and Ctrl+V/Cmd+V*.**

**If you haven't done so already, set your model to `Sonnet` instead of `Opus`.**

> In Claude Code at the prompt, type:
> ```
> /model
> ```
> In the list that comes up, type "3" or use the arrow keys to move the pointer to "3" and hit *Enter*.
>
> ![set model](./images/ccode181.png?raw=true "set model")
>
> You should see an indicator that the model was set to *claude-sonnet-4-6*.

<br><br>


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

![Initial prompt](./images/ccode180.png?raw=true "Initial prompt")


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

![Initial prompt](./images/ccode182.png?raw=true "Initial prompt")

---
<br><br>

## 3: Create Your First File with Claude
**What we're doing:** Using Claude to generate a simple code file.  
**Why:** File creation is a core feature for development workflows.

**Action:** Type:
```
Create a simple hello.js file that prints "Hello from Claude Code!"
```

Claude will create the file and *may* show you the content in the diff above the terminal. You do not need to do anything in the diff area. Just select option 1 in the terminal where Claude is waiting.

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
1. Type `exit` to exit Claude
2. Restart with: `claude --resume`
3. You'll see a list with your session. Just hit *Enter* to resume.
4. Claude will restore your previous session context

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

**Action:** You'll see the previous rejected operation message above the prompt area. Use the `up arrow` key to bring up the last prompt. Change the name of the file in the prompt from *goodbye.js* to *goodbye.py* to create a Python file instead. Hit *Enter*.
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

## 1: Understand Default Mode 
**What we're doing:** Starting Claude in its standard interactive mode.  
**Why:** Default mode gives you full control with permission prompts for each action.

**Action:** Start Claude:
```bash
claude 
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
**What we're doing:**  Responding to questions from Claude
**Why:** Claude needs our input on some things before proceeding.

**Action:** Read any questions that come up and select number of answer to proceed if single option for answer. (To save time and complexity, it is recommended to use the recommended/simplest option.) If you can select multiple options, use arrow keys and space/Enter to select options. Then move on to next question using right arrow. Answer all questions and then move to *Submit* and press *Enter*. If you want to see more of Claude's *thinking* during this process, press *ctrl+o".

![Responding to questions](./images/ccode99.png?raw=true "Responding to questions")


![Responding to questions](./images/ccode100.png?raw=true "Responding to questions")


---
<br><br>

## 6: Review the Plan
**What we're doing:** Interacting with Claude's proposed plan.  
**Why:** You can review plans before execution to ensure desired outcomes.

**Action:** After Claude presents the plan, you could modify it if you wanted by selecting `ctrl+g`. 
1. Go ahead and select that key sequence to bring the plan up in the editor.
2. (Optional) To see the preview version of the plan (if you're in VS Code, you can right-click and select *Open Preview*).
3. After you're done reviewing it, you can close the file (close the original file if you also opened a preview version).
4. Then **select option 2** to proceed and auto-accept edits. (Re option 1: The amount of context isn't significant yet, so we'll clear it after this.)

![Reviewing plan](./images/ccode102.png?raw=true "Reviewing plan")

![Approving plan](./images/ccode183.png?raw=true "Approving plan")

**Note that you are now in *accept edits on* mode, but the original task will still run under *plan* mode.**

---
<br><br>

## 7: View to-do list
**What we're doing:** Monitoring the progress through the to-do list.  
**Why:** Helps you understand what is done and what is left to be done.

**Action:** While Claude Code is doing the implementation, hit `ctrl+t` to see the current state of the to-do list.

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

**Action:** Exit Claude (`exit`), then restart with the command below and **use option 2** to accept the risk:

```bash
claude --dangerously-skip-permissions
```

![Accepting bypass mode](./images/ccode184.png?raw=true "Accepting bypass mode")

If you don't see the mode as **bypass permissions on** mode, use `Shift+Tab` to change the mode until you see that.

We also have an alias for this that you can use in the future `claude-yolo` if you are in a terminal other than the starting one.

⚠️ **Note:** Use with caution! Claude won't ask before making changes.

![YOLO](./images/ccode123.png?raw=true "YOLO")

---
<br><br>

## 10: Test Auto-Accept Mode
**What we're doing:** Creating multiple files without interruption.  
**Why:** See how much faster development is without permission prompts.

**Action:** Type:
```
Create a simple To-Do list app in javascript wtih functionality to add and delete tasks
```

Notice Claude creates all files without asking for permission.

![YOLO](./images/ccode185.png?raw=true "YOLO")

---
<br><br>

## 11: Exit

**Action:** In prep for the next lab and a fresh start, type `exit` to exit Claude Code.

```
exit
```

## Lab Summary
✅ You've successfully learned:
- Default mode with permission prompts
- Plan mode for complex task planning
- Auto-accept mode for rapid development
- Headless mode for automation


---

<br><br>
---
## END OF LAB
---
<br><br>

**NOTE:** From here on, you can use the `claude --dangerously-skip-permissions` mode if you want to avoid having to respond to most prompts. For convenience, if working in the codespace, there is a shortcut alias for this setup:  `claude-yolo`. You must be in a terminal other than the original one that you started with to use this.

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

Hit *Enter*. This will bring up a set of *tabbed* output for help. Use the *tab* key to get to the *commands* section at the top. Then you can use the arrow keys to move up and down to see all the commands.
Review the list including /clear, /compact, /rewind, /model, and others.

![help to see commands](./images/ccode109.png?raw=true "help to see commands")

Use *Esc* to exit when done.

---
<br><br>

## 3: Create Some Context
**What we're doing:** Building up conversation history to practice management.  
**Why:** We need content to demonstrate context management commands.

**Action:** Have a multi-turn conversation. **Type each of the following into the prompt area one at a time and let each complete before entering the next one**:
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

5. You should see the file and the conversation restored. You can just clear out any commands showing up in Claude.

---
<br><br>


## 7: Create a project context file
**What we're doing:** Setting up a CLAUDE.md file for project context.  
**Why:** CLAUDE.md provides persistent project knowledge across sessions.

**Action:** Type:
```
/init
```

This file will be automatically created and read in future sessions.

![claude.md](./images/ccode188.png?raw=true "claude.md")

Afterwards, you can take a look at the file by opening it up in an editor (you can use 'code' command if in VS Code or Codespace).

You'll probably notice that it identifies custom slash commands, custom agents, and custom skills that we have in the `extra` directory. While it is finding those kind of files there, it is NOT registering them as something usable. It is just describing the file types.

---
<br><br>

## 8: Demonstrate the project context file is used
**What we're doing:** Resetting chat while keeping project guidance.  
**Why:** Persistent memory improves continuity across sessions. Also shows difference between chat context and project files.

**Action:**
1. Type `/clear` to clear the conversation
2. Ask: `What are our project rules and what test command should I run after code edits?`

Claude should recall information from the CLAUDE.md file and display that info.


![claude.md](./images/ccode191.png?raw=true "claude.md")

---
<br><br>

## 9: Exit

**Action:** In prep for the next lab and a fresh start, type `exit` to exit Claude Code.

```
exit
```

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

# Lab 4: Custom Commands
## Lab Purpose
Learn how to create custom slash commands to automate repetitive tasks and establish project-specific workflows. Build reusable commands that enhance your development productivity.

---
<br><br>

## 1: Create Commands Directory
**What we're doing:** Setting up the folder structure for global and project-specific custom commands.  
**Why:** Claude looks for custom commands in specific directories.

> **Terminology note:** Commands are reusable prompts that run inline in the main conversation. Unlike agents (which run in their own context), a command is a predefined workflow anyone on the team can invoke with a single slash.

**Action:** In terminal, create the directory:
```bash
mkdir -p ~/.claude/commands
mkdir -p .claude/commands
```

---
<br><br>

## 2: Add a Global Command from the Repo
**What we're doing:** Installing an example command.
**Why:** See an example of taking a properly formatted file and making it into a commands.

**Action:** In terminal, copy the *extra/commands/test.md* file to ~/*.claude/commands/test.md*. This defines a new command that accepts a test type argument (unit, integration, or e2e) and generates appropriate tests. After copying it with the first os command below, open it up to review and understand the structure with the second os command below. You do not need to make any changes. Close when done.

```bash
cp extra/commands/test.md ~/.claude/commands/
code extra/commands/test.md
```

----
<br><br>

## 3: Add a Project Command (Repo-Shared)
**What we're doing:** Adding a command to the repository.  
**Why:** This is how teams share workflows.

**Action:**
```bash
cp extra/commands/refactor.md .claude/commands/
code .claude/commands/refactor.md
```

---
<br><br>

## 4: Create a New Command: /doc
**What we're doing:** Writing a small command from scratch.  
**Why:** Students learn what a “good command” looks like.

**Action:** Create `.claude/commands/doc.md` with the content below:
```md
---
description: Generate concise module documentation
---
Given a file path in $ARGUMENTS:
1) Add/refresh JSDoc comments
2) Add a short README snippet (3-6 bullets) describing the module
3) Provide a minimal usage example
Keep changes small and do not refactor code.
```

**Make sure to save the file when done.**

---
<br><br>

## 5: Restart Claude
**What we're doing:** Restarting claude  
**Why:** New commands are only picked up on restart.

```
claude
```

## 6: Test Your Custom Command
**What we're doing:** Executing the custom command we just created.  
**Why:** Verifying commands work as expected before relying on them.

**Action:** Type:
```
/test
```

![Test command](./images/ccode49.png?raw=true "Test command")

Hit *Enter*. Claude should prompt you for which type of test (as defined in the command's md file) to run. Select the entry for *unit* from the list.

![Test command](./images/ccode192.png?raw=true "Test command")

**This step will take some time to run. You do NOT need to wait for this to finish to continue. While this is running, you can open another terminal and proceed with the next step.**

---
<br><br>


## 7: Review the /test output
**What we're doing:** Reviewing output  
**Why:** To ensure our new command worked as expected

**Action:** Switch back to the terminal session running the unit testing and review the output. Provide approval if needed. You should see something like below:

![Preview command](./images/ccode193.png?raw=true "Preview command")

---
<br><br>

## 8: Use /doc
**What we're doing:** Running our new command.  
**Why:** Confirms custom commands work end-to-end.

**Action:** In Claude:
```
/doc user.js
```

Approve changes if prompted.

![Doc output](./images/ccode194.png?raw=true "Doc output")

---
<br><br>

## 8: List Custom Commands
**What we're doing:** Confirming command discovery.  
**Why:** Quickly verify what's available.

**Action:**
```
/help
```

Hit Enter. Then find the section that lists custom commands.


![Viewing list of custom commands](./images/ccode195.png?raw=true "Viewing list of custom commands")

---
<br><br>

## 9: Exit
**Action:**
```
exit
```

---
<br><br>

## Lab Summary
✅ You’ve learned to:
- Install global commands and repo commands
- Create your own command with frontmatter + instructions
- Validate discovery via /help

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 5: Skills + Subagents 
## Lab Purpose 
Build one practical skill and two specialist subagents to see how delegation keeps work fast and clean.

---
<br><br>

## 1: Create the Project Structure
**What we're doing:** Creating the folders used by Claude Code for skills and agents.  
**Why:** Skills/subagents are file-system discoverable.

**Action:**
```bash
mkdir -p .claude/skills/api-checker/scripts
mkdir -p .claude/agents
```

---
<br><br>

## 2: Create a Minimal Skill (api-checker)
**What we're doing:** Writing a SKILL.md with a focused purpose.  
**Why:** Skills help Claude apply repeatable expertise automatically.

**Action:** Create `.claude/skills/api-checker/SKILL.md`:

```
code .claude/skills/api-checker/SKILL.md
```

**Action:** Copy/paste the following contents into the file and save it.

```md
---
name: api-checker
description: When the user asks to validate a REST endpoint, generate a curl test, run it, and summarize status + key fields.
---

## Rules

- Ask for the base URL if missing.
- Run `scripts/check.py <url>` to fetch the endpoint and get structured JSON output.
- Parse the output: use `ok` for success/failure, `status` for HTTP code, `json` for the response body.
- Keep output short: status, 3 key fields, and one recommendation.

## Example trigger

User: "Can you validate GET /health on my service?"
```

![Creating the skill](./images/ccode196.png?raw=true "Creating the skill")

---
<br><br>

## 3: Add the referenced script to the Skill
**What we're doing:** Adding a deterministic helper.  
**Why:** Scripts make results more predictable than pure prompting.

**Action:** Create `.claude/skills/api-checker/scripts/check.py`:

```
code .claude/skills/api-checker/scripts/check.py
```

**Action:** Copy/paste the following contents into the file and save it.


```python
#!/usr/bin/env python3
import json, sys, urllib.request

url = sys.argv[1] if len(sys.argv) > 1 else None
if not url:
    print("Usage: check.py <url>")
    sys.exit(2)

req = urllib.request.Request(url, headers={"Accept":"application/json"})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        status = r.status
        body = r.read().decode("utf-8", errors="replace")
except Exception as e:
    print(json.dumps({"ok": False, "error": str(e)}))
    sys.exit(1)

out = {"ok": 200 <= status < 300, "status": status}
try:
    out["json"] = json.loads(body)
except Exception:
    out["body_preview"] = body[:200]
print(json.dumps(out))
```

Then make it executable:
```bash
chmod +x .claude/skills/api-checker/scripts/check.py
```

---
<br><br>

## 4: Create the Planner Agent
**What we're doing:** Creating a “plan-first” helper.  
**Why:** This keeps your main chat focused on decisions, not long plans.

> **Terminology note:** The file in `.claude/agents/` defines an *agent configuration*. When Claude delegates to it during a conversation, it runs as a *subagent* — a separate context that does work and returns results to the main conversation.

**Action:** Create `.claude/agents/planner.md`:

```
code .claude/agents/planner.md
```

**Action:** Copy/paste the following contents into the file and save it.

```md
---
name: planner
description: Create a short implementation plan + risks. Do not edit files.
model: sonnet
---

## Instructions
- Ask 1-2 clarifying questions only if required.
- Output a 5-step plan.
- List 3 risks.
- Do not write or modify files.
```

---
<br><br>

## 5: Create the Test-Runner Agent
**What we're doing:** Creating a “run tests, summarize, propose minimal fix” helper.  
**Why:** Subagents reduce context noise and speed up troubleshooting.

**Action:** Create `.claude/agents/test-runner.md`:

```
code .claude/agents/test-runner.md
```

**Action:** Copy/paste the following contents into the file and save it.


```md
---
name: test-runner
description: Run tests, summarize failures, propose minimal fixes.
model: sonnet
---

## Instructions
- Run the project test command (ask if unknown).
- Summarize failures in 3 bullets.
- Propose the smallest fix, then implement only if approved.
```

---
<br><br>

## 6: Start Claude Code
**Action:**
```bash
claude
```

---
<br><br>

## 7: Trigger the skill (Without Naming It)
**What we're doing:** Letting Claude choose the skill automatically.  
**Why:** Skills are intended to be invoked based on context.

**Action:** In Claude, type:
```
Please validate https://jsonplaceholder.typicode.com/posts/1 and summarize what you find.
```

If Claude asks for approval to run scripts, approve it.

(Optional: You can open the .claude/skills/api-checker/SKILL.md file to remember what it specifies.)

What you should see in the output is that the skill was selected and loaded, then, per the skill instructions:

- The supporting script was run
- The status was reported
- Key fields were listed
- A recommendation was provided

![Using the skill](./images/ccode197.png?raw=true "Using the skill")


---
<br><br>

## 8: Use the Planner Subagent
**What we're doing:** Delegating planning to a subagent that cannot edit files.  
**Why:** This is a safe and scalable “team” pattern.

**Action:** In Claude, type:
```
Use the planner subagent.
We need to add input validation to the User class without changing public behavior.
Return only the plan + risks.
```
(Optional: You can open the .claude/agents/planner.md file to remember what it specifies.)

What you should see after this runs is a plan produced by the agent that, per the planning agent spec:

- Outputs a 5 step plan
- Lists 3 risks


![Using the planning subagent](./images/ccode198.png?raw=true "Using the planning subagent")


---
<br><br>

## 9: Use the Test-Runner Subagent
**What we're doing:** Delegating test execution + fix suggestion.  
**Why:** This is the most common “AI teammate” workflow.

**Action:** In Claude, type:
```
Use the test-runner subagent.
Create one minimal failing test for invalid email handling in user.js, then propose the smallest fix.
Stop after proposing the fix (do not implement yet).
```

(Optional: You can open the .claude/agents/test-runner.md file to remember what it specifies.)

What you should see after this runs is a failing email test added to user.test.js and a proposed fix.


![Using the test-runner subagent](./images/ccode198.png?raw=true "Using the testrunner subagent")

---
<br><br>

## 10: Exit
**Action:**
```
exit
```

---
<br><br>

## Lab Summary
✅ You’ve built and used:
- A project Skill (SKILL.md + script)
- Two subagents (planner + test-runner)
- A safe delegation workflow (plan-first, test-first)

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 6: Supervised Subagent Workflow + Plugin Packaging + VS Code
## Lab Purpose
Turn your commands + agents + skills into a shareable "team kit," and practice a supervised delegation workflow where you orchestrate specialist subagents step by step.

---
<br><br>
## 1: Add a Team Command: /ship
**What we're doing:** Creating a standardized "ready to ship" checklist command.  
**Why:** To have a reusable standardized command that encompasses multiple functions.

**Action:** Create `.claude/commands/ship.md`:

```
code .claude/commands/ship.md
```

**Action:** Copy/paste the following contents into the file and save it.

```md
---
description: Ship checklist: review, tests, and summary
---
Do the following in order:
1) Summarize what changed (3 bullets) using git status/diff
2) Run tests (ask for the command if unknown)
3) List 3 risks and 3 follow-ups
Do not edit files unless asked.
```
---
<br><br>

## 2: Add the Reviewer Agent
**What we're doing:** Adding a "review-only" specialist agent definition.  
**Why:** We want a reviewer as part of our workflow.

> **Tooling note:** This agent is structurally restricted from editing files — not just told not to, but actually blocked from using Write and Edit tools. This is the difference between a prompt-level constraint (which Claude can override) and a tool-level constraint (which it cannot).

**Action:** Create `.claude/agents/reviewer.md`:

```
code .claude/agents/reviewer.md
```

**Action:** Copy/paste the following contents into the file and save it.

```md
---
name: reviewer
description: Review code changes for correctness, tests, and security. Do not edit files.
model: sonnet
disallowedTools: Write, Edit
---
## Instructions
- Review the diff and changed files.
- Output: 3 risks, 3 tests to add, 3 patch suggestions.
- Do not modify files.
```

> **What changed from Lab 5's agents?** Compare this to the planner agent you created in Lab 5. The planner says "Do not write or modify files" in its instructions — a prompt-level constraint. This reviewer goes further with `disallowedTools: Write, Edit`, which *enforces* the restriction at the tool level. Both approaches have their place: prompt constraints are flexible, tool constraints are guaranteed.

---
<br><br>

## 3: Create the Plugin Manifest Folder
**What we're doing:** Preparing a shareable plugin bundle.  
**Why:** Plugins are the packaging mechanism for distributing team assets (commands, agents, skills) so teammates can install them with a single command rather than copying files around.

**Action:**
```bash
mkdir -p .claude-plugin
```
---
<br><br>

## 4: Create plugin.json
**What we're doing:** Defining the plugin metadata and component paths.  
**Why:** Claude Code uses this manifest to discover and load plugin components. When someone installs your plugin, these paths tell Claude Code where to find the commands, agents, and skills you've bundled.

**Action:** Create `.claude-plugin/plugin.json`:

```
code .claude-plugin/plugin.json
```

**Action:** Copy/paste the following contents into the file and save it.

```json
{
  "name": "intro-claude-code-team-kit",
  "version": "0.1.0",
  "description": "Intro workshop team kit: commands, agents, and a skill.",
  "commands": ["../.claude/commands"],
  "agents": ["../.claude/agents"],
  "skills": "../.claude/skills"
}
```

> **Key detail:** The `commands`, `agents`, and `skills` fields are top-level in `plugin.json` — there is no wrapper object around them. Paths are relative to the `plugin.json` file location.

---
<br><br>

## 5: Start Claude Code and Verify Discovery
**What we're doing:** Validating the repo has the expected structure.  
**Why:** Before running any workflows, confirm that Claude Code discovers all your assets — the new `/ship` command, the reviewer agent from this lab, plus the planner agent, test-runner agent, and api-checker skill from Lab 5.

**Action:** Start Claude Code

```bash
claude
```

Then run:

```
/help
```

Confirm you see `/ship` listed in the `custom-commands` section.

![The /ship command is present](./images/ccode200.png?raw=true "The /ship command is present")


Hit *Esc" to get out of that output. Then run: 

```
/agents
```

Confirm the `reviewer`, `planner`, and `test-runner` agents are shown.

![Agents are present](./images/ccode201.png?raw=true "Agents are present")


Hit *Esc" to get out of that output. Then run: 

```
/skills
```

Confirm the `api-checker` skill is shown in the `Project Skills` section.

![Skill is  present](./images/ccode202.png?raw=true "Skill is present")

---
<br><br>


## 6: Practice the Supervised Delegation Pattern (Plan → Implement → Review)
**What we're doing:** Running a realistic delegation flow where *you* act as the supervisor, directing Claude to use the right subagent at each step.  
**Why:** This is how most people use subagents in practice — you decide what happens next, and subagents are your specialists. You control the workflow; they do the focused work.

**Action:** In Claude, type:
```
Use the planner subagent to propose a plan to add phoneNumber to User (optional field).
```
Review the plan. When you're satisfied, tell Claude to proceed:
```
The plan looks good. Now implement the change minimally. Do not run tests yet.
```

![Initial plan](./images/ccode203.png?raw=true "Initial plan")


![Approved plan](./images/ccode204.png?raw=true "Approved plan")

> **What's happening here:** You explicitly delegated the planning step to the planner subagent. Claude ran it in a separate context and returned the result to you. Then you — the supervisor — approved the plan and gave the next instruction. This is the "supervised delegation" pattern: the human decides the workflow, subagents do the specialized work.
---
<br><br>

## 7: Delegate Review (Reviewer Subagent)
**What we're doing:** Getting a review from the reviewer subagent, which is structurally unable to edit files.  
**Why:** Because the reviewer has `disallowedTools: Write, Edit` in its definition, you can trust that it will only analyze — never modify — your code. This keeps the review honest and the main conversation focused on your decisions about what to change.

**Action:** In Claude, type:
```
Use the reviewer subagent to review the change we just made.
Return 3 risks, 3 tests to add, and 3 concrete patch suggestions.
```

You should see in the results the 3 risks, 3 tests to add, and 3 patch suggestions we told the reviewer agent to output.

![Start of reviewer output](./images/ccode205.png?raw=true "Start of reviewer output")

> **What's happening here:** Claude delegates to the reviewer subagent, which runs with its own instructions and tool restrictions in a separate context. It returns structured output to the main conversation. You then decide which suggestions to act on.

 
---
<br><br>

## 8: Run the Ship Checklist Command
**What we're doing:** Running the `/ship` command you created in Step 1.  
**Why:** Execute the overall workflow.

> **Note:** Notice the difference from Steps 6–7. The `/ship` command runs *inline* in the main conversation — it doesn't spawn a separate subagent context. It's a reusable prompt template, not a specialist. Commands and agents serve different purposes: commands standardize *what to do*, agents specialize *who does it*.

**Action:** In Claude, run:

```
/ship
```

What you should see is the git info being gathered and the testing running. Then in the summary, you'll see what changed, the test results (1 will be failing), the "Risks" list and the suggested "Follow-ups".

![Partial output of ship command](./images/ccode206.png?raw=true "Partial output of ship command")

---
<br><br>


## 9: (OPTIONAL) Open the VS Code Extension
**What we're doing:** Switching to IDE workflow.  
**Why:** Many learners prefer IDE-first interaction.

**Action:** Open the Claude Code VS Code extension (sidebar or toolbar icon).

If you are prompted to log in, choose the "Claude.ai Subcription" option and follow the steps to authenticate.

---
<br><br>

## 10: (OPTIONAL) Run /ship from the Extension
**What we're doing:** Using the same team kit inside the IDE.  
**Why:** Reinforces that repo-level assets (commands, agents, skills) work the same way whether you're in the terminal or VS Code. The extension automatically discovers everything in `.claude/`.

**Action:** In the extension chat, run:
```
/ship
```

![/ship in extension](./images/ccode207.png?raw=true "/ship in extension")

---
<br><br>
## 11: Exit
**Action:** End any running sessions and close Claude Code.
---
<br><br>
## Lab Summary
You've learned:
- **Supervised delegation pattern:** You act as the orchestrator, directing Claude to use specialist subagents (planner, reviewer) at each step and making decisions between them.
- **Prompt constraints vs. tool constraints:** The planner uses prompt instructions ("do not edit files") while the reviewer uses `disallowedTools: Write, Edit` for structural enforcement. Both are valid; tool constraints are stronger.
- **Commands vs. agents:** Commands (`/ship`) are reusable prompts that run inline. Agents are specialists that run in their own subagent context and return results.
- **Plugin packaging:** How to bundle commands, agents, and skills into a `plugin.json` manifest that teammates can install.
- **Cross-environment consistency:** The same repo-level assets work in both the terminal and VS Code.

> **Going further:** Claude Code also has an experimental **Agent Teams** feature for fully autonomous multi-agent coordination. With Agent Teams, a "team lead" agent spawns independent teammates that coordinate through shared task lists and direct messaging — no human orchestration needed between steps. Agent Teams require setting `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and are architecturally different from the subagent delegation shown here: each teammate gets its own context window, and they can message each other directly. That's beyond the scope of this workshop, but worth exploring once you're comfortable with supervised delegation. See the [Agent Teams documentation](https://docs.anthropic.com/en/docs/claude-code/agent-teams) for details.
<br><br>
---
## END OF LAB
---
<br><br>





