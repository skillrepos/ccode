# AI Powered Coding with Claude Code - lab setup

## 1. Set codespace timeout

While logged in to GitHub, go to https://github.com/settings/codespaces.

Scroll down and find the section on the page labeled *Default idle timeout*. 

Increase the default timeout value to 90 minutes and then select the *Save* button.

![Increasing default timeout](./images/k8sdev33.png?raw=true "Increasing default timeout")

(**NOTE**: If your codespace does time out at some point in the course, there should be a button to restart it. In that case, you will need to run the *minikube start* command again.)

<br><br>

## 2. Create your own codespace to run the labs by clicking on the button below.
<br/><br/>

Click here ------> [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/skillrepos/ccode?quickstart=1)

<br/><br/>

Then click on the option to create a new codespace.

![Creating new codespace from button](./images/advk8s0.png?raw=true "Creating new codespace from button")

**This will run for several minutes while it gets everything ready.**

<br/><br/>

##

## 4. Open the labs doc. 

You can open the labs doc either in a separate browser tab/window via [Open Labs Document in Browser](https://github.com/skillrepos/adv-k8s-v2/blob/main/codespace-labs.md) and/or you can open the labs in the codespace itself. To open it in the codespace, follow the instructions below.

After the codespace has started, you can close the *Welcome* doc by clicking on the X in its tab. Then open the labs document by going to the file tree on the left, find the file named **codespace-labs.md**, right-click on it, and open it with the **Preview** option.)

![Labs doc preview in codespace](./images/advk8s7.png?raw=true "Labs doc preview in codespace")

This will open it up in a tab above your terminal. Then you can follow along with the steps in the labs. 
Any command in the gray boxes is either code intended to be run in the console or code to be updated in a file.

Labs doc: [Advanced Kubernetes Labs](codespace-labs.md)


