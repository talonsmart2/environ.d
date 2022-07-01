# Environment Tools (environ.d)
A collection of various components for setting up your environment, provides a bunch of basic scripts to speed up your workflow. Designed for both Windows, Linux and Mac.

## Features
- Boilerplate: Boilerplate code
- Scripts: Scripts to automate tasks, and a ton of bash aliases made as short as possible.
- Sounds: Some custom sound effects
- Windows: Scripts for Windows, right now for speeding things up a bit with some regedit tweaks and cleaning temp files.

## How to install
1. Install the following packages: ```exa zsh lolcat```
2. Install ohmyzsh and set the theme to "bira".
3. Add this to your zshrc for each account you want to use thos on:

```
export PATH=$PATH:/home/$(whoami)/Documents/Software/environ.d/Scripts
export PATH=$PATH:/home/$(whoami)/Documents/Software/environ.d/Scripts/android-tools
source "/home/$(whoami)/Documents/Software/environ.d/Scripts/aliases"
```
You can of course, change the directories to whichever install location you prefer.

<hr />
&copy Talon Smart
