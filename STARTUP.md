## Step 1: Start Claude Code
**What we're doing:** Launching Claude Code in interactive mode.  
**Why:** This is the primary way you'll interact with Claude for coding tasks.

**Action:** In the terminal, type:
```bash
claude
```

You may see a welcome message and some update information.


![startup](./images/cc1.png?raw=true "Startup")

<br><br>
---

## Step 2: Login
**What we're doing:** Running the */login* command in Claude Code.  
**Why:** We haven't authenticated yet.

**Action:** Hit *Enter* to dismiss the welcome message if needed. In Claude Code at the prompt, type:
```
/login
```

![login](./images/cc2.png?raw=true "login")

<br><br>


## Step 3: Authenticate Your Account
**What we're doing:** Connecting Claude Code to your Anthropic account.  
**Why:** Authentication enables full features and personalized settings.

**Action:** When prompted, follow the authentication flow:

### a. For *Select login method:*, choose option 1 (either type "1" or select the line and hit "Enter") - *Claude account with subscription*
<br>

![subscription](./images/ccode80.png?raw=true "Subscription")

<br><br>

### b. Claude will display a URL and code. We won't be able to open this, so just click on *Cancel*. 
<br>

![url popup](./images/ccode81.png?raw=true "URL popup")

<br><br>

### c. Back in the codespace screen, open the full URL displayed there - either by *Ctrl/Cmd+click* or by copying and pasting the URL into a browser tab.
<br>

![backup method](./images/ccode82.png?raw=true "backup method") 

<br><br>


### d. You *may* have to sign in with your userid again and get a verification code to use before going to the next steps. If so, just follow the prompts and make sure to authenticate in the SAME browser as the one where you opened the URL.

![login](./images/cc3.png?raw=true "login") 

<br><br>

### e. On the next screen that is shown, click on the *Authorize* button to give Claude Code authorization to use your Claude chat account.
<br>

![auth dialog](./images/ccode16.png?raw=true "auth dialog") 

<br><br>

### f. Next, you should see a screen with an authentication code. Click on the *Copy Code* link at the bottom to copy the authentication code.
<br>

![authentication code](./images/ccode18.png?raw=true "authentication code") 

<br><br>

### g. Go back to the codespace. In the area in the terminal under the URL, you should see a prompt like *Paste code here if prompted*. Click next to that and paste in the authentication code you copied in the previous step.
<br>

![Paste code](./images/ccode19.png?raw=true "Paste code") 

<br><br>

### h. After this, you should see an indication that login was successful, press *Enter* and you are ready to use Claude Code!
<br>

![successful login](./images/ccode83.png?raw=true "Successful login") 

<br><br>

## Step 4: Ensure the Sonnet model is selected
**What we're doing:** Running the */model* command in Claude Code.  
**Why:** Use a cheaper model since we're doing simple tasks.

**Action:** In Claude Code at the prompt, type:
```
/model
```
In the list that comes up, if the default doesn't already have Sonnet selected, use the arrow keys to move the pointer to the *Sonnet* entry (usually "4") and hit *Enter*. 

Separately, use the left/right arrow keys to change the effort to *Medium effort*. (The exact model versions listed may differ from the screenshot — pick the current Sonnet model.)

![model selection](./images/ccode243.png?raw=true "model selection")

You should see an indicator that the model was set to *Sonnet* with *medium* effort. Note: your `/model` selection is saved as the default for new sessions; hit `Enter` in the model list to set it as your default.

<br><br>

### You're now ready for the labs!

<br><br>
