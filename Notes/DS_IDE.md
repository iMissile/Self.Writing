# VScode

## Common
- COOL! [VSCode Customization: Supercharge Your IDE](https://dev.to/iashin/vscode-customization-supercharge-your-ide-43fn)
- [GitHub and Visual Studio Code](https://vscode.github.com/)
- [REMOTE PAIR PROGRAMMING IN R USING VISUAL STUDIO CODE AND LIVE SHARE](https://ivelasq.rbind.io/blog/vscode-live-share/)
- [janisdd/vscode-edit-csv](https://github.com/janisdd/vscode-edit-csv). vs code extension to edit csv files with an excel like table ui
- [VScode: Changing the Display Language](https://code.visualstudio.com/docs/getstarted/locales). Press Ctrl+Shift+P to bring up the Command Palette then start typing "display" to filter and display the Configure Display Language command.
- [Debugging in VSCode](https://code.visualstudio.com/docs/editor/debugging)

## Julia VScode
- [Julia for VSCode](https://www.julia-vscode.org/)

## Python VScode
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
	- install the Python extension for VS Code from the Visual Studio Marketplace. [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## R VScode
- Analytics Vidhya. [A fresh start for R in VSCode](https://medium.com/analytics-vidhya/a-fresh-start-for-r-in-vscode-ec61ed108cf6). Setting up Visual Studio Code for R development
- [How to integrate Python and R in Visual Studio Code](https://towardsdatascience.com/how-to-integrate-python-and-r-in-visual-studio-code-496a47c90422)
- COOL! [R in 2021 with VSCode](https://datamares.netlify.app/en/post/r-vscode/)
- [Writing R in VSCode: A Fresh Start](https://renkun.me/2019/12/11/writing-r-in-vscode-a-fresh-start/)
	- [VSCode](https://code.visualstudio.com/Download): Visual Studio Code
	- [languageserver](): An implementation of the Language Server Protocol for R. `install.packages("languageserver")`
	- [VSCode R Extension](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r): An implementation of the Language Server Protocol for R by Yuki Ueda
	- [R LSP Client for VSCode](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r-lsp): R LSP Client for Visual Studio Code
	- [Python](https://www.python.org/downloads/)
	- [Radian](https://github.com/randy3k/radian): A 21st century R console.
	- [ManuelHentschel/vscDebugger](https://github.com/ManuelHentschel/vscDebugger/) R Debugger Protocol. Ставим из zip файла 
	`install.packages(path_to_source, repos = NULL, type="source")`
	- In Windows, please go to VSCode settings, and set up the following entries:
```
{
  "r.bracketedPaste": true,
  "r.rterm.windows": "C:\\Users\\<USER>\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\radian.exe",
  "r.rpath.windows": "C:\\Program Files\\R\\R-4.0.5\\bin\\R.exe",
  "r.lsp.debug": true,
  "r.lsp.diagnostics": true,
  "r.rterm.option": [
        "--no-save",
        "--no-restore",
        "--r-binary=C:\\Program Files\\R\\R-4.0.5\\bin\\R.exe"
    ],
}
```
Finally, you need to change your VSCode settings to enable R within the editor. For that press Ctrl + Shift + P and type in “Preferences: Open Settings (JSON)” and press Enter. This will open the settings.json of your editor. Add the following code to the JSON file, adjust the respective path to your setup and save the file.
[Settings File Locations](https://vscode.readthedocs.io/en/latest/getstarted/settings/)
Depending on your platform, the user settings file is located here:

Windows %APPDATA%\Code\User\settings.json
Mac $HOME/Library/Application Support/Code/User/settings.json
Linux $HOME/.config/Code/User/settings.json
The workspace setting file is located under the .vscode folder in your project.

Под виндой не находит R, ищем решение дальше
- [Setting Up Visual Studio code to work with R - “win32 can't use R”](https://stackoverflow.com/questions/65823681/setting-up-visual-studio-code-to-work-with-r-win32-cant-use-r)

```
Extensions > R
In the settings for "R", scroll down to R > Rpath: Windows
```
- Настраиваем контроль длины строки кода (lintr), кладем в корневую директорию проекта. [Here](https://renkun.me/2019/12/11/writing-r-in-vscode-a-fresh-start/). 
You may take a look at https://github.com/jimhester/lintr#project-configuration Briefly, you could create a `~/.lintr` file with the following content:
`linters: with_defaults(line_length_linter(120))`
Remember to leave a new line at the bottom of the file.
- [REditorSupport/vscode-R](https://github.com/REditorSupport/vscode-R/releases/tag/v2.2.0)
- [Debugging R in VSCode](https://renkun.me/2020/09/13/debugging-r-in-vscode/)

