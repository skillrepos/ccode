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
