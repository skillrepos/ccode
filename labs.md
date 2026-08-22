# AI-Powered Coding with Claude Code
## Learn practical workflows, hands-on coding techniques, and structured interactions
## Session Labs
## Revision 6.29 - 08/22/26

<br><br>

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**Copy and paste may not work as expected if using the mouse. If not, use the keyboard shortcuts - *Ctrl+C/Cmd+C and Ctrl+V/Cmd+V*.**

**ONLY If you haven't done so already, set your model to `Sonnet` instead of `Opus`.**

> In Claude Code at the prompt, type:
> ```
> /model
> ```
> Arrow to the **Sonnet** entry and hit *Enter*. Select it *by name* — the list also contains Opus 5 and, for some accounts, Fable 5, so Sonnet's position varies. Use the **left/right arrow keys** to set the **effort level** to *medium*.
>
> ![set model](./images/ccode209.png?raw=true "set model")
>
> You should see the model set to a *Sonnet* model (currently *claude-sonnet-5*) with *medium* effort.
>
> **Note:** As of Claude Code 2.1.153, your `/model` selection is saved as the default for new sessions. Press `s` in the model list to set a model for the current session only.
>
> **Why Sonnet?** It is cheaper and the right default for everyday coding; save the heavier models for genuinely hard problems.
>
> **What is "effort"?** The reasoning dial (`low`, `medium`, `high`, `xhigh`, `max`; `high` is the default). Phrases like "think hard" are ordinary words in your prompt; the one keyword Claude still recognizes is `ultrathink`, which asks for deeper reasoning on a single turn without changing your session setting.
>
<br><br>


---
<br><br>

# Lab 1: Introduction to Claude Code and Basic Setup
## Lab Purpose
Get familiar with the Claude Code CLI and its basic commands.

---
<br><br>

## 1: Test Basic Interaction
**What we're doing:** Sending a first prompt.  
**Why:** Confirms the connection works.

**Action:** Type this, then hit `Enter`.
```
Hello Claude, can you tell me what you can help with?
```

![Initial prompt](./images/ccode210.png?raw=true "Initial prompt")

> **Note:** The **left arrow** on an empty input opens **Agent View**, a dashboard for parallel sessions (research preview; also `claude agents`). `Esc` returns.


---
<br><br>

## 2: Ask Claude to Explain a Code Snippet
**What we're doing:** Explaining code.  
**Why:** Code understanding is a core feature.

**Action:** Type:
```
Explain this code: console.log([1,2,3].map(x => x * 2))
```

![Initial prompt](./images/ccode211.png?raw=true "Initial prompt")

---
<br><br>

## 3: Create Your First File with Claude
**What we're doing:** Generating a file.  
**Why:** File creation drives most workflows.

**Action:** Type this. In auto mode Claude creates the file directly; if it does ask, select option 1 (you can ignore the diff above the terminal).
```
Create a simple hello.js file that prints "Hello from Claude Code!"
```

> **NOTE:** Notice the status bar reads `⏵⏵ auto mode on`. In this mode, Claude will create the file without asking. Claude Code starts in **auto mode** (Pro, Max, Team plans), where a background classifier approves routine actions. Lab 2 covers the modes.

![Initial file creation](./images/ccode86.png?raw=true "Initial file creation")

---
<br><br>

## 4: View the Created File
**What we're doing:** Checking the file.  
**Why:** Know where Claude saves things.

**Action:** Click the file on the left, or in a new terminal tab, type:
```bash
ls -la
cat hello.js
```

![Initial file creation](./images/ccode87.png?raw=true "Initial file creation")

---
<br><br>

## 5: Ask Claude to Run the File
**What we're doing:** Running the code.  
**Why:** Claude runs commands and shows output.

**Action:** Type this; if asked, select option 1.
```
Run the hello.js file we just created
```

![Run file](./images/ccode88.png?raw=true "Run file")

Output: "Hello from Claude Code!"

![Run file](./images/ccode89.png?raw=true "Run file")

---
<br><br>

## 6: Exit and Resume
**What we're doing:** Exiting and resuming.  
**Why:** Demonstrate resume of previous session.

**Action:** 
1. Type `exit` to exit Claude
2. Restart with: `claude --resume`
3. Hit *Enter* on your session at the top of the list
4. Claude restores your previous context

---
<br><br>

## 7: Creating a second file
**What we're doing:** Rejecting a change.  
**Why:** It sets up the redo next.

**Action:** First press `Shift+Tab` once, until the status bar reads `⏸ manual mode on`. Rejecting only exists when Claude asks, and auto mode does not ask.

**Action:** Now type this, then **select option 3 to tell Claude not to create the file.**
```
Create a simple goodbye.js file that prints "Goodbye from Claude Code!"
```

![Do something different](./images/ccode244.png?raw=true "Do something different")


---
<br><br>

## 8: Redo
**What we're doing:** Resubmitting a fixed prompt.  
**Why:** This is how you correct a request.

**Action:** Press `up arrow`, **change *goodbye.`js`* to *goodbye.`py`*,** hit *Enter*, then select option 1 to confirm creating it.
```
Create a simple goodbye.py file that prints "Goodbye from Claude Code!"
```

---
<br><br>

## 9: Use @ Mentions to Pull Context
**What we're doing:** Pulling a file in with @.  
**Why:** @ references files, folders, or URLs directly.

**Action:** Type this; approve the edit (change) when asked (you are still in manual mode from Step 7).
```
What does @hello.js do? Can you add a timestamp to it?
```

If ghost text suggests running the file, hit *Tab*, *Enter*, and approve.

![Ref file by mention](./images/ccode212.png?raw=true "Ref file by mention")

**Also, you can use `@folder/` for directories, `@https://url` for web content.**

---
<br><br>

## 10: Create a Memory and try the Bash ! shortcut
**What we're doing:** Saving a memory; running a shell command inline.  
**Why:** Memories persist; `!` runs shell commands in place.

**Note:** Create memories by asking Claude in plain language.

**Action:** Type this, approving the write when asked (you are still in manual mode):
```
Remember that this project uses JavaScript and Python for demos.
```

Claude stores it persistently (auto-memory files and/or CLAUDE.md); `/memory` shows where.

**Action:** An input starting with `!` runs as a shell command (it turns pink). Type:
```
! cat ~/.claude/projects/-workspaces-ccode/memory/MEMORY.md
```

![Memory file](./images/ccode245.png?raw=true "Memory file")

(If *Enter* does nothing, press `Esc` to clear the suggested-path line, then *Enter*. If the file is missing, ask Claude where the memory went.)


---
<br><br>

## 11: Explore the Codebase with Questions
**What we're doing:** Asking about our files.  
**Why:** Exploration is Claude Code's most common use.

**Action:** Type:
```
What files have we created so far? Summarize the purpose of each one and suggest an improvement.
```

![File info](./images/ccode215.png?raw=true "File info")

---
<br><br>

## 12: Exit

**Action:** Type `exit` to exit Claude Code before the next lab.

```
exit
```

## Lab Summary
✅ You've successfully:
- Verified installation and authentication
- Created and executed code with Claude
- Learned basic navigation and commands
- Practiced session management (`exit`, `--resume`, redo)
- Used @ mentions, persistent memories, and the ! bash shortcut
- Explored a codebase with natural language questions — how you orient in any new project

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 2: Working with Claude Code Modes
## Lab Purpose
Further explore auto, manual, plan, and bypass modes — plus a `/permissions` deny rule no mode overrides.

---
<br><br>

## 1: Start Claude in a specific mode
**What we're doing:** Starting in manual mode  
**Why:** Use command line option to get to a particular mode.

**Action:** Start Claude with non-default mode.
```bash
claude --permission-mode manual
```

**Action:**  Confirm status bar shows `⏸ manual mode on`.

---
<br><br>

## 2: Test Manual Mode Permissions
**What we're doing:** Triggering a prompt.  
**Why:** Permission prompts keep you in control.

**Action:** Type:
```
Create a config.json file with database connection settings for Postgresql
```

Claude asks first whether you want to create it; type `1` to accept.

> Created without asking? Still in auto — `Shift+Tab` to `⏸ manual mode on` and retry.


![Creating config.json](./images/ccode216.png?raw=true "Creating config.json")

---
<br><br>

## 3: Activate Plan Mode
**What we're doing:** Entering Plan Mode.  
**Why:** It thinks through multi-step tasks first.

**Action:** `Shift+Tab` until you see *Plan mode*

![Activating plan mode](./images/ccode96.png?raw=true "Activating plan mode")


---
<br><br>

## 4: Prompt for a complex task
**What we're doing:** Giving Claude a big task.  
**Why:** Plan first, implement second.

**Action:** Type:

```
Create a basic user profile page with fields for name, email, and profile picture upload. 
```

![Planning](./images/ccode98.png?raw=true "Planning")

While this is running, type `Ctrl+o` to see the larger "thinking" process that Claude is using. When done viewing that, type `Ctrl+o` again to get back to the normal view.

![Thinking process](./images/ccode246.png?raw=true "Thinking process")

---
<br><br>

## 5: Respond to questions
**What we're doing:**  Answering Claude's questions
**Why:** It needs input to proceed.

> **May not happen:** Claude often goes straight to the plan. If it does, skip to Step 6 — nothing is wrong.

**Action:** *If Claude asks*, answer each question (simplest option saves time): a number for single answers; arrows plus space/Enter for multi-select, right arrow for the next; finish on *Submit*.

![Responding to questions](./images/ccode217.png?raw=true "Responding to questions")


![Responding to questions](./images/ccode218.png?raw=true "Responding to questions")


---
<br><br>

## 6: Review the Plan
**What we're doing:** Reviewing the plan.  
**Why:** Catch problems before execution.

**Action:** 
1. Press `ctrl+g` to open the plan in the editor. Plans live in `~/.claude/plans/`, outside this folder, so VS Code may ask *"Do you want to allow untrusted files in this workspace?"* — choose **Open**.
2. (Optional) In VS Code if you want to see the source of the markdown: right-click, *Reopen Editor with ... Text Editor*, for markdown.
3. Close the file(s) when done.

> ⚠️ **Known issue:** with the plan file open, don't scroll or click in the Claude Code panel — mouse events spill harmless garbage (`M^[[<35;86;12M`). `Esc` clears stray input; `ctrl+l` redraws.

4. **Select option 1** — **"Yes, and use auto mode"** when auto is available, else **"Yes, auto-accept edits"**.
   
![Reviewing plan](./images/ccode247.png?raw=true "Reviewing plan")


---
<br><br>

## 7: When done, clear the Conversation
**What we're doing:** Clearing context.  
**Why:** Do this before an unrelated task.

Claude finishes with a summary.

![Plan completed](./images/ccode220.png?raw=true "Plan completed")

**Action:** Type:
```
/clear
```

---
<br><br>


## 8: Set a Guardrail with Permissions That Outlives the Conversation
**What we're doing:** Adding a **deny rule**.
**Why:** Normal restrictions typed in chat die with `/compact`, `/clear`, or a new session; But we can add a restriction as a deny rule in Claude's configuration. It will be enforced in *every* mode.

**Action:** Type:
```
/permissions
```

On the screen, you will see categories in the row that starts with `Permissions`. Primary rules are grouped into categories of **Allow**, **Ask**, and **Deny**. We'll add one to the **Deny** list.

**Action:** Use the `Tab` or `arrow` keys to highlight the `Ask` category. Select `1` to Add a new rule. 

![Deny category](./images/ccode250.png?raw=true "Deny category")

On the next screen, let's enter a rule to restrict Git pushes. Enter the text below in the box.

```
Bash(git push *)
```

![Deny category](./images/ccode252.png?raw=true "Deny category")


Hit `Enter` to submit. Claude Code then asks **where to save the rule** — take the default, **1. Project settings (local)**. 

![Entering rule](./images/ccode253.png?raw=true "Entering rule")

Press `Esc` to get out of the rule entry section.

> **Rule syntax:** `Tool` or `Tool(specifier)`; `*` matches anything, spaces included, so `Bash(git push *)` catches `git push origin main` (`Bash(git push:*)` is equivalent). Rules save to `.claude/settings.local.json` at the repo root, covering future sessions.

## 9: Test the rule
**What we're doing:** Testing the **deny rule**.
**Why:** To prove that it works.

**Action:** In a **separate terminal**, run:
```bash
git add -A && git commit -m "lab work"
```

**Action:** Back in Claude, test the rule. Type:
```
Push our changes to origin.
```

Claude is blocked before it can try.

![Entering rule](./images/ccode254.png?raw=true "Entering rule")

> **If the dialog misbehaves**, add the rule to `.claude/settings.local.json` under `permissions.deny`; it applies on the next request, no restart.

---
<br><br>

## 10: Try YOLO Mode
**What we're doing:** Trying out the bypass-permissions mode.
**Why:** Understanding the value and risk of bypass-permissions.

**Action:** Exit Claude (`exit`), then restart it as below. Make sure to pick **option 2** when prompted to accept the risk:

```bash
claude --dangerously-skip-permissions
```

![Accepting bypass mode](./images/ccode255.png?raw=true "Accepting bypass mode")

If you don't see **bypass permissions on**, `Shift+Tab` until you do. (The `claude-yolo` alias does the same, from a second terminal.)

⚠️ **Note:** Use with caution — Claude won't ask before changing anything. Save it for throwaway sandboxes like this Codespace.

![YOLO](./images/ccode123.png?raw=true "YOLO")

**Action:** Type:
```
Create a simple To-Do list app in javascript with functionality to add and delete tasks
```

Claude creates every file without asking.

![YOLO](./images/ccode221.png?raw=true "YOLO")

<br><br>


## 11: Compare how deny rules function in YOLO mode
**What we're doing:** Re-testing the guardrail in YOLO mode.
**Why:** Bypass removes even the classifier — the deny rule still wins.

**Action:** Now retry the denied command:
```
Push our changes to origin.
```

You'll be prompted to push — that prompt is **Claude's own** judgment about a consequential action, not the guardrail; bypass silences the permission system's questions, not Claude's. A deny rule never offers you a **Yes**, so go ahead and choose it: the push is still blocked. The point is that **deny rules apply in every mode, including bypass.** Modes decide how much Claude asks; deny rules decide what is off-limits.

![Push denied](./images/ccode256.png?raw=true "Push denied")

---
<br><br>



## 12: Exit

**Action:** Type `exit` to exit Claude Code before the next lab.

```
exit
```

## Lab Summary
✅ You've successfully learned:
- Auto mode (default since August 14, 2026) and its classifier
- Manual mode (config value `default`), prompting every action
- Plan mode, accept-edits, and bypass
- **Deny rules beat modes:** chat boundaries compact away; a deny rule is configuration and holds everywhere, bypass included
- Why headless (`claude -p`) starts manual


---

<br><br>
---
## END OF LAB
---
<br><br>

**NOTE:** Auto mode handles most prompts from here; `claude --dangerously-skip-permissions` (or the codespace `claude-yolo` alias, second terminal) removes all interruptions.

<br><br>

# Lab 3: Built-in Commands and Context Management
## Lab Purpose
Master the slash commands for conversation, context, and memory.

---
<br><br>

## 1: Start Fresh with Claude
**What we're doing:** Starting a new session.  
**Why:** A clean context.

**Action:** Start Claude:
```bash
claude
```

---
<br><br>

## 2: View Available Commands
**What we're doing:** Listing slash commands.  
**Why:** Knowing what exists speeds you up.

**Action:** Type:
```
/help
```

*Tab* to the *commands* section, arrow through the list — note /clear, /compact, /rewind, /model. Use *Esc* to exit from the help section.

![help to see commands](./images/ccode222.png?raw=true "help to see commands")

---
<br><br>

## 3: Create Some Context
**What we're doing:** Building conversation history.  
**Why:** We need content to manage.

**Action:** Enter these one at a time, accepting edits:
```
Create a user.js file with a User class
```

Then...

```
Add methods for getName and setName  
```

Then...

```
Add email validation to the User class
```

Then...

```
Create a test file for the User class
```

![help to see commands](./images/ccode223.png?raw=true "help to see commands")

---
<br><br>

## 4: Check Context Usage
**What we're doing:** Checking context use.  
**Why:** Avoid token limits mid-session.

**Action:** Type:
```
/context
```

Scroll up for token usage and remaining capacity.

![context command](./images/ccode224.png?raw=true "context command")


**Action:** Try `/usage` too. Type the command below. Use `Esc` to exit the usage screen.

```
/usage
```


![context command](./images/ccode257.png?raw=true "context command")


> **Note:** `/context` shows what is in the context window now; **`/usage`** (`/cost` is an alias) shows what you have spent — session tokens, cost, and share of your plan's limit.

---
<br><br>

## 5: Compact the Conversation
**What we're doing:** Condensing history.  
**Why:** It extends how long you can work.

**Action:** Type:
```
/compact Keep the User class implementation details and test structure
```

Claude summarizes earlier turns, keeping what you named. (This may take awhile to run.)

![compact](./images/ccode225.png?raw=true "compact")

---
<br><br>

## 6: Use Rewind Feature
**What we're doing:** Rolling back.  
**Why:** Undo mistakes safely.

**Action:** 
a. Ask Claude to make a change we'll want to undo: 

```
Remove the email validation from the User class in user.js
```

![Remove email validation](./images/ccode258.png?raw=true "Remove email validation")

b. Then type `/rewind`. (`Esc` twice also works on an empty prompt.)
c. **Select the *Remove the email validation...* entry** and press `Enter` — entries restore to the point *before* that message. Skip */compact* entries: code can't be restored there.

![rewind](./images/ccode259.png?raw=true "rewind")

d. Choose **Restore code and conversation**.

![rewind](./images/ccode260.png?raw=true "rewind")

e. This will put you back to the point before you ran the command to remove the validation. Open user.js to confirm the validation is back.

![restored content](./images/ccode261.png?raw=true "restored content")

> Only file-tool edits are checkpointed — bash changes (`rm`, `mv`) show *No code changes*. Use git for real version history.

---
<br><br>


## 7: Create a project context file
**What we're doing:** Generating a CLAUDE.md.  
**Why:** It carries project knowledge forward.

**Action:** Type:
```
/init
```

Claude creates CLAUDE.md and reads it in future sessions; open it in an editor. (You can select it from the file list or use the `code CLAUDE.md` command from a terminal if in VS Code).

![claude.md](./images/ccode262.png?raw=true "claude.md")


---
<br><br>

## 8: Demonstrate the project context file is used
**What we're doing:** Clearing chat, keeping project guidance.  
**Why:** Project files outlive conversation context.

**Action:**
1. Type `/clear` to clear the conversation
2. Ask: `What are our project rules and what test command should I run after code edits?`

Claude answers from CLAUDE.md.

![claude.md](./images/ccode263.png?raw=true "claude.md")

---
<br><br>

## 9: View the Memory Hierarchy with /memory
**What we're doing:** Viewing memory scopes.  
**Why:** The hierarchy decides where knowledge goes.

**Action:** Type:
```
/memory
```

Memory layers enterprise (if applicable) → user → project, your new CLAUDE.md at project level. Nested CLAUDE.md files load automatically; CLAUDE.local.md holds uncommitted personal overrides.

![claude.md](./images/ccode264.png?raw=true "claude.md")

---
<br><br>

## 10: Explore Git History with Claude
**What we're doing:** Analyzing repo changes.  
**Why:** Faster than reading git logs.

**Action:** Type:
```
What changes have been made in this repo recently? Summarize the git log.
```

![claude.md](./images/ccode229.png?raw=true "claude.md")

---
<br><br>

## 11: Try Headless Mode with Pipe Input
**What we're doing:** Piping input in.  
**Why:** It chains Claude into scripts and CI.

**Action:** Exit Claude, then run this in your terminal:
```bash
echo "What files are in this directory?" | claude -p
```

`-p` is print (headless) mode: stdin in, result out, no session.

**Note:** headless runs start in **manual** mode, not auto. Nobody is there to answer prompts, so pre-approve with `--allowedTools`, or lock down with `--permission-mode dontAsk` — which never prompts at all and denies anything you did not pre-approve. Try it:
```bash
claude -p "run the test suite and summarize failures" --permission-mode dontAsk --allowedTools "Bash(node --test *)" "Read"
```

> Add `--output-format json` for scripts that parse the result.

![claude.md](./images/ccode266.png?raw=true "claude.md")

---
<br><br>


## Lab Summary
✅ You've mastered:
- /help to discover commands
- /compact to manage context
- /rewind to undo changes
- /context and /usage to check spend
- CLAUDE.md for persistent memory
- /memory for the hierarchy
- Git history in natural language
- Headless pipe mode for automation


<br><br>
---
## END OF LAB
---
<br><br>
# Lab 4: Skills + Subagents 
## Lab Purpose 
Build a skill and two specialist subagents, and see how delegation keeps work fast and clean.

**NOTE: If using the codespace setup, you can use the `code` command to create/edit a file.**

---
<br><br>

## 1: Create the Project Structure
**What we're doing:** Creating the skill and agent folders.  
**Why:** Both are discovered from the file system.

**Action:**
```bash
mkdir -p .claude/skills/api-checker/scripts
mkdir -p .claude/agents
```

---
<br><br>

## 2: Create a Minimal Skill (api-checker)
**What we're doing:** Writing a SKILL.md.  
**Why:** Skills apply repeatable expertise automatically.

**Action:** Create `.claude/skills/api-checker/SKILL.md` with the contents below. Save it when done. (**NOTE:** If you are working in the codespace, you can use the `code` command to open an a new file. And use 'Cmd+S` or `Ctrl+S` to save it.)

```md
---
name: api-checker
description: Use whenever the user asks to validate, check, or test a REST endpoint or API URL. Always run scripts/check.py (instead of fetching directly) to get structured results, and summarize status + key fields.
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
**What we're doing:** Adding a helper script.  
**Why:** Scripts are more predictable than prompting.

**Action:** Create `.claude/skills/api-checker/scripts/check.py` with these contents:


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

Make it executable:
```bash
chmod +x .claude/skills/api-checker/scripts/check.py
```

---
<br><br>

## 4: Create the Planner Agent
**What we're doing:** Creating a “plan-first” helper.  
**Why:** It keeps your main chat on decisions, not long plans.

> **Terminology:** the file in `.claude/agents/` is an *agent configuration*; when Claude delegates to it, it runs as a *subagent* — a separate context that returns results to the main conversation.

> **The `model:` field** takes a family alias (`sonnet`, `opus`, `haiku`, `fable`), a full name like `claude-sonnet-5`, or `inherit` (follow the main conversation). Aliases are safer: they track the current version. Only `name` and `description` are required.

**Action:** Create `.claude/agents/planner.md` with these contents:

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
**What we're doing:** Creating a test-runner helper.  
**Why:** Subagents cut context noise and speed troubleshooting.

**Action:** Create `.claude/agents/test-runner.md` with these contents:


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
**What we're doing:** Letting Claude pick the skill.  
**Why:** Skills are invoked from context.

**Action:** Type:
```
Please validate https://jsonplaceholder.typicode.com/posts/1 and summarize what you find.
```

Approve script execution if asked. You should see the skill load and, per its instructions:

- The script run (`scripts/check.py` in the output — not a plain `Fetch(...)` call)
- The status reported
- Key fields listed
- A recommendation

![Using the skill](./images/ccode231.png?raw=true "Using the skill")

> **If you see `Fetch(https://...)` instead:** skills are *model-invoked* — Claude matches your request against skill descriptions, so on simple requests it may use built-in fetch. Description wording matters. To force it, name the skill: `Use the api-checker skill to validate https://jsonplaceholder.typicode.com/posts/1`.


---
<br><br>

## 8: Use the Planner Subagent
**What we're doing:** Delegating planning to a subagent that can't edit files.  
**Why:** A safe, scalable “team” pattern.

**Action:** Type:
```
Use the planner subagent.
We need to add input validation to the User class without changing public behavior.
Return only the plan + risks.
```
You should get a step-by-step plan plus risks, per the agent spec.


![Using the planning subagent](./images/ccode198.png?raw=true "Using the planning subagent")


---
<br><br>

## 9: Use the Test-Runner Subagent
**What we're doing:** Delegating test execution and a fix suggestion.  
**Why:** The most common “AI teammate” workflow.

**Action:** Type:
```
Use the test-runner subagent.
Create one minimal failing test for invalid email handling in user.js, then propose the smallest fix.
Stop after proposing the fix (do not implement yet).
```

![Using the test-runner subagent](./images/ccode232.png?raw=true "Using the testrunner subagent")

This will take a while to complete. But, once the background processing finishes, you should get a failing email test in user.test.js and a proposed fix.

![Using the test-runner subagent](./images/ccode233.png?raw=true "Using the testrunner subagent")

Accept the fix or not, your call.

---
<br><br>

## 10: Exit Claude Code
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


# Lab 5: Supervised Subagent Workflow + Plugin Packaging + VS Code
## Lab Purpose
Package your commands, agents, and skills as a shareable "team kit," and orchestrate specialist subagents step by step.

---
<br><br>
## 1: Add a Team Command: /ship
**What we're doing:** Creating a ship checklist command.  
**Why:** One reusable command covering several steps.

**Action:** Create `.claude/commands/ship.md` with these contents:

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
**What we're doing:** Adding a review-only specialist agent.  
**Why:** The workflow needs a reviewer.

**Action:** Create `.claude/agents/reviewer.md` with these contents:

```md
---
name: reviewer
description: Review code changes for correctness, tests, and security. Do not edit files.
model: sonnet
disallowedTools: Write, Edit
---
## Instructions
- Review the diff and changed files.
- Do not modify files.
- Return your results in EXACTLY this format so they can be relayed verbatim:
  RISKS: (3 bullets)
  TESTS TO ADD: (3 bullets)
  PATCH SUGGESTIONS: (3 bullets)
```

> **Prompt vs. tool constraint:** Lab 4's planner is *told* not to edit; this reviewer is *blocked* from Write and Edit by `disallowedTools`. Claude can override a prompt constraint, never a tool one.

---
<br><br>

## 3: Create the Plugin Manifest Folder
**What we're doing:** Preparing a shareable plugin bundle.  
**Why:** Plugins let teammates install your commands, agents, and skills in one command.

**Action:**
```bash
mkdir -p .claude-plugin
```
---
<br><br>

## 4: Create plugin.json
**What we're doing:** Defining plugin metadata and component paths.  
**Why:** The manifest says where the bundled components live.

**Action:** Create `.claude-plugin/plugin.json` with these contents:

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

> **Key detail:** `commands`, `agents`, and `skills` are top-level fields (no wrapper object); paths are relative to `plugin.json`.

> **Shortcut (v2.1.157+):** `claude plugin init <name>` scaffolds a plugin; plugins in `.claude/skills` auto-load with no marketplace. `/plugin list` shows installed plugins with projected per-session token cost; `defaultEnabled: false` ships one disabled.

---
<br><br>

## 5: Start Claude Code and (optional) Verify Discovery
**What we're doing:** Checking asset discovery.  
**Why:** `/ship`, the reviewer, and Lab 4's assets should all appear.

**Action:** Start Claude Code:

```bash
claude
```

Then run:

```
/help
```

Confirm `/ship` appears under `custom-commands`.

![The /ship command is present](./images/ccode267.png?raw=true "The /ship command is present")


*Esc* exits. Next, let's look at the agents: you can either list them with the `!` shortcut from Lab 1:

```
! ls .claude/agents/*
```

(The trailing `/*` matters: a partial path shows a subtle suggested-path line, and **while it shows, *Enter* is ignored**. A complete path ends it, as does `Esc`.)

Confirm `planner.md`, `test-runner.md`, and `reviewer.md` appear. 

Or, you can ask Claude:

```
What subagents are available in this project?
```

![Listing out agents](./images/ccode268.png?raw=true "Listing out agents")



Next, let's look at the skills. Run: 

```
/skills
```

Confirm `api-checker` is listed. (No `/skills` in your build? `/context` lists loaded skills, and `! ls .claude/skills/*` works too.)

![Skill is  present](./images/ccode269.png?raw=true "Skill is present")

*Esc* exits.

---
<br><br>


## 6: Practice the Supervised Delegation Pattern (Plan → Implement → Review)
**What we're doing:** Delegating with you as supervisor.  
**Why:** You drive the workflow; subagents do focused work.

**Action:** Type:
```
Use the planner subagent to propose a plan to add phoneNumber to User (optional field).
```

![Initial plan](./images/ccode237.png?raw=true "Initial plan")

Review the plan, then tell Claude to proceed:

```
The plan looks good. Now implement the change minimally. Do not run tests yet.
```
![Executing plan plan](./images/ccode270.png?raw=true "Executing plan")


> **Supervised delegation:** the planner ran in its own context and returned a result; you approved and gave the next instruction.
---
<br><br>

## 7: Delegate Review (Reviewer Subagent)
**What we're doing:** Getting a review from the reviewer.  
**Why:** `disallowedTools: Write, Edit` means it can only analyze, never modify.

**Action:** Type:
```
Use the reviewer subagent to review the change we just made. Show me its RISKS, TESTS TO ADD, and PATCH SUGGESTIONS sections verbatim.
```

The reviewer may run as a **backgrounded agent** (*"Backgrounded agent (↓ to manage · ctrl+o to expand)"*), then the main agent reports.

Expect the RISKS / TESTS TO ADD / PATCH SUGGESTIONS sections. The main agent *interprets* subagent output — without "verbatim" it summarizes in its own words. For the subagent's transcript, press *ctrl+o* and scroll up (or ↓ for the agent manager).

![Start of reviewer output](./images/ccode239.png?raw=true "Start of reviewer output")

You decide which suggestions to act on.
 
---
<br><br>

## 8: Run the Ship Checklist Command
**What we're doing:** Running the `/ship` command from Step 1.  
**Why:** Execute the whole checklist at once.

> **Note:** unlike Steps 6–7, `/ship` runs *inline* — a reusable prompt template, not a specialist. Commands standardize *what to do*; agents specialize *who does it*.

**Action:** Run:

```
/ship
```

Shell commands appear **collapsed** (`ctrl+o` expands them), then a numbered summary: changes, test results (a failure may appear), risks, follow-ups.

![Partial output of ship command](./images/ccode240.png?raw=true "Partial output of ship command")

---
<br><br>


## 9: (OPTIONAL) Open the VS Code Extension
**What we're doing:** Switching to the IDE.  
**Why:** Many people prefer working IDE-first.

**Action:** Open the Claude Code VS Code extension (sidebar or toolbar).

If prompted to log in, choose "Claude.ai Subcription" and authenticate.

![Opening extension](./images/ccode272.png?raw=true "Opening extension")

---
<br><br>

## 10: (OPTIONAL) Run /ship from the Extension
**What we're doing:** Using the team kit in the IDE.  
**Why:** The extension discovers everything in `.claude/`.

**Action:** In the extension chat, run:
```
/ship
```

![/ship in extension](./images/ccode207.png?raw=true "/ship in extension")

---
<br><br>

## 11: Exit
**Action:** End running sessions and close Claude Code.

---
<br><br>

## Lab Summary
You've learned:
- **Supervised delegation:** you orchestrate specialist subagents step by step.
- **Prompt vs. tool constraints:** telling an agent not to edit is weaker than `disallowedTools`.
- **Commands vs. agents:** `/ship` runs inline; agents run in their own context.
- **Plugin packaging:** bundling commands, agents, and skills in `plugin.json`.
- **Cross-environment consistency:** the same repo assets work in terminal and VS Code.

> **Going further:** experimental **Agent Teams** let a "team lead" spawn teammates that coordinate through shared task lists and direct messages, each with its own context and no human between steps; disabled by default (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`). Subagents can spawn subagents too — since v2.1.219, **3 levels** deep (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`; `1` disables nesting). See the [Agent Teams docs](https://code.claude.com/docs/en/agent-teams).
<br><br>
---
## END OF LAB
---
<br><br>

<p align="center">
<b>For educational use only by the attendees of our workshops.</b>
</p>
<p align="center">
<b>(c) 2026 Tech Skills Transformations and Brent C. Laster. All rights reserved.</b>
</p>





