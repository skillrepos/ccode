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
Get familiar with Claude Code installation, authentication, and basic command-line interface. You'll learn how to start Claude Code, authenticate your account, and execute your first commands.

<br><br>
---

## Step 1: Verify Claude Code Installation
**What we're doing:** Checking that Claude Code is properly installed in your environment.  
**Why:** We need to ensure the tool is available before proceeding.

**Action:** Open a terminal and type:
```bash
claude --version
```

You should see output like: `Claude Code v2.x.x`

<br><br>
---

## Step 2: Start Claude Code for the First Time
**What we're doing:** Launching Claude Code in interactive mode.  
**Why:** This is the primary way you'll interact with Claude for coding tasks.

**Action:** In the terminal, type:
```bash
claude
```

You'll see a welcome message and an option to pick a color theme. To select a theme, you can type the corresponding number key on your keyboard or use the arrows to move up and down and hit *Enter* when you are on the choice you want.


![startup](./images/ccode13.png?raw=true "Startup")

<br><br>
---

## Step 3: Authenticate Your Account
**What we're doing:** Connecting Claude Code to your Anthropic account.  
**Why:** Authentication enables full features and personalized settings.

**Action:** When prompted, follow the authentication flow:
1. For *Select login method:*, choose option 1 - *Claude account with subscription*

![subscription](./images/ccode14.png?raw=true "Subscription")

<br><br>

2. Claude will display a URL and code. You can click on it to *Open* the URL. 

![url popup](./images/ccode15.png?raw=true "URL popup")

<br><br>

3. On the next screen that is shown, click on the *Authorize* button to give Claude Code authorization to use your Claude chat account.

![auth dialog](./images/ccode16.png?raw=true "auth dialog") 

<br><br>

4. **If you get an error on the next web page displayed** then go back to the codespace and copy the full URL from there.

![backup method](./images/ccode17.png?raw=true "backup method") 

<br><br>

5. Eventually, you should see a screen with an authentication code. Click on the *Copy Code* link at the bottom to copy the authentication code.

![authentication code](./images/ccode18.png?raw=true "authentication code") 

<br><br>

6. Go back to the codespace. In the area in the terminal under the URL, you should see a prompt like *Paste code here if prompted*. Click next to that and paste in the authentication code you copied in the previous step.

![Paste code](./images/ccode19.png?raw=true "Paste code") 

<br><br>

7. After this, you should see an indication that login was successful

![successful login](./images/ccode20.png?raw=true "Successful login") 

<br><br>

8. Answer *yes* to the questions about using the *recommended settings* and *if you trust the files in the folder*.
   
![recommended settings](./images/ccode21.png?raw=true "Recommended settings") 

![trust files](./images/ccode22.png?raw=true "trust files") 

<br><br>

9. After this, you should be ready to use Claude Code!

![ready to go](./images/ccode23.png?raw=true "Ready to go") 

<br><br>
---

## Step 4: Test Basic Interaction
**What we're doing:** Verifying Claude can respond to simple queries.  
**Why:** This confirms the connection is working properly.

**Action:** At the Claude prompt, type:
```
Hello Claude, can you tell me what you can help with?
```

Claude should respond with information about its capabilities.

---

## Step 5: Ask Claude to Explain a Code Snippet
**What we're doing:** Testing Claude's code understanding capabilities.  
**Why:** Understanding code is a fundamental Claude Code feature.

**Action:** Type the following:
```
Explain this code: console.log([1,2,3].map(x => x * 2))
```

Claude will explain the JavaScript array operation.

---

## Step 6: Create Your First File with Claude
**What we're doing:** Using Claude to generate a simple code file.  
**Why:** File creation is a core feature for development workflows.

**Action:** Type:
```
Create a simple hello.js file that prints "Hello from Claude Code!"
```

Claude will create the file and show you the content.

---

## Step 7: View the Created File
**What we're doing:** Verifying the file was created successfully.  
**Why:** Understanding where Claude saves files is important.

**Action:** In a new terminal tab (keep Claude running), type:
```bash
ls -la
cat hello.js
```

You should see your new file and its contents.

---

## Step 8: Ask Claude to Run the File
**What we're doing:** Having Claude execute the code it created.  
**Why:** Claude can run commands and show output directly.

**Action:** Back in Claude, type:
```
Run the hello.js file we just created
```

You'll see the output: "Hello from Claude Code!"

---

## Step 9: Use the Help Command
**What we're doing:** Exploring available slash commands.  
**Why:** Slash commands provide quick access to common operations.

**Action:** Type:
```
/help
```

Review the list of available commands like /clear, /compact, etc.

---

## Step 10: Exit and Resume
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
