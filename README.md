# C/C++ Code Snippets
Vscode extension for C/C++, for easy to program.

## Usage
Type a part of the keywords in snippet e.g., "for" and press enter.

```c
for // Creates a for loop snippet
```
If the snippet does not appear, you can also just press <kbd>Ctrl</kbd> + <kbd>Space</kbd> (works on Windows, Linux, or Mac) to access the available snippets in the editor.


## Installation
You can  find this extension VScode extension market,  but now it's not upload in that.

1. Install Visual Studio Code
2. Launch VS Code
3. From the command palette `Ctrl`+`Shift`+`P` (Windows, Linux) or `Cmd`+`Shift`+`P` (OSX)
4. Type `ext install` or just simply select `Install Extension`
5. Choose the extension - CodeAssist Snippets
6. Relaunch VS Code

Also,
you can use vsix  to install this extension:
npm install -g @vscode/vsce
$ cd myExtension
$ vsce package

## Develop
If you want develop this extension, please also add Chinese express in snippets.
e.g: "Algo": {
        "prefix": "算法",
        "body": [
            " 算法"，
        ],
        "description": "Code snippet for 算法 statement"
}




