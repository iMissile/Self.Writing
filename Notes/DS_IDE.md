# ZED
- [Zed](https://zed.dev/) is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. It's also open source.

# AI IDE
- [Windsurf AI IDE](https://codeium.com/windsurf)

# C++
- [15 лучших бесплатных IDE C++ (редактор и компилятор) для Windows (2024 г.)](https://www.guru99.com/ru/best-cpp-ide-editor-free.html)
- Онлайн компилятор (какой найдете), например: https://www.onlinegdb.com/

# RStudio

## RStudio fonts
- COOL! [Ligature fonts for R](https://benjaminlmoore.wordpress.com/2017/07/19/ligature-fonts-for-r/)
	- [Monospaced Programming Fonts with Ligatures](https://www.hanselman.com/blog/MonospacedProgrammingFontsWithLigatures.aspx)
	- [Hasklig - a code font with monospaced ligatures](https://github.com/i-tu/Hasklig) (in my opinion a nicer base font) which is more conservative with the ligatures it introduces.
	- [tonsky/FiraCode. Monospaced font with programming ligatures](https://github.com/tonsky/FiraCode)
	- [FiraCode RStudio instructions](https://github.com/tonsky/FiraCode/wiki/RStudio-instructions)
	- [Add editor font support to RStudio Server #2534 {Closed}](https://github.com/rstudio/rstudio/issues/2534)
- [JetBrains Mono. A typeface for developers_](https://www.jetbrains.com/lp/mono/)
- [JetBrains Mono — a new typeface made for developers](https://blog.jetbrains.com/blog/2020/01/15/jetbrains-mono-a-new-font-made-for-developers/)


## Other
- [How to get unsaved script tabs](https://stackoverflow.com/questions/35223435/how-to-get-unsaved-script-tabs)

# AI IDE
- [Windsurf](https://windsurf.com/editor)
- [Cursor]()

# VScode

## Common
- COOL! [VSCode Customization: Supercharge Your IDE](https://dev.to/iashin/vscode-customization-supercharge-your-ide-43fn)
- [GitHub and Visual Studio Code](https://vscode.github.com/)
- [REMOTE PAIR PROGRAMMING IN R USING VISUAL STUDIO CODE AND LIVE SHARE](https://ivelasq.rbind.io/blog/vscode-live-share/)
- [janisdd/vscode-edit-csv](https://github.com/janisdd/vscode-edit-csv). vs code extension to edit csv files with an excel like table ui
- [VScode: Changing the Display Language](https://code.visualstudio.com/docs/getstarted/locales). Press Ctrl+Shift+P to bring up the Command Palette then start typing "display" to filter and display the Configure Display Language command.
- [Debugging in VSCode](https://code.visualstudio.com/docs/editor/debugging)
- [How to separate changed files from untracked files in vscode?](https://stackoverflow.com/questions/52410100/how-to-separate-changed-files-from-untracked-files-in-vscode). Git: Improved untracked files management
You can now manage untracked files separately by using the Git: Untracked Changes setting.
Choose the `separate` option, if you'd like to see untracked files in a separate group in the Source Control view.
Choose `hidden` if you'd like to never see them.
- [How can I see local history changes in Visual Studio Code?](https://stackoverflow.com/questions/46446901/how-can-i-see-local-history-changes-in-visual-studio-code)
- [How do I turn on text wrapping by default in VS Code](https://stackoverflow.com/questions/38561881/how-do-i-turn-on-text-wrapping-by-default-in-vs-code)
For version 1.81.1, the path is `File -> Preferences -> Settings`. Search for word wrap on the search bar and select On from the dropdown.
- [Send code selection to debug console #14494 {Closed}](https://github.com/microsoft/vscode-python/issues/14494).
You can actually customize your own shortcut to send selection to the debug console! Open the command palette (View > Command Palette...) and run "Preferences: Open Keyboard Shortcuts". Then look for "Evaluate in Debug Console" and add a short cut for it. For example, I added `Alt + D` for mine:
- [How to Remove Trailing Whitespace in VS Code](https://www.codexcafe.com/blog/remove-trailing-whitespace/)

## Terminal issues
Изучая вывод json в консоль VsCode под Windows выяснилось, что консолька PowerShell то работает под кодировкой cp866.
Выяснил командой `[Console]::OutputEncoding`
Вывод можно переключить на Unicode командой `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8`.
В Windows Terminal это проходит, в VsCode имеем проблему, не вводятся заглавные буквы.
[Uppercase console issue #100067 {Closed}](https://github.com/microsoft/vscode/issues/100067)

Как решил проблему
1. Configure VS Code to Use an External Terminal
	- Open VS Code.
	- Go to File > Preferences > Settings (or press Ctrl + ,).
	- Search for `terminal.integrated.defaultProfile.windows`.
	- Set the default terminal to one of the following:
		* Windows Terminal (if installed)
		* PowerShell
		* Command Prompt
2. Make the Change Encoding Permanent
	- Open Your PowerShell Profile `notepad $PROFILE`
	- Add the Encoding Command `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8`
	- Save and Restart

## Themes
- Решаем проблему невидимости курсора мыши при светлых темах. Путем настройки windows. [How to fix mouse cursor disappearing in Visual Studio & Visual Studio Code](https://camerondwyer.com/2017/09/19/how-to-fix-mouse-cursor-disappearing-in-visual-studio-visual-studio-code/)

## Remote sesson
- [Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh)
- [Remote - SSH. Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

## Fonts
- [Fira code. VS Code Instructions](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions)
- [Iosevka](https://github.com/be5invis/Iosevka). Versatile typeface for code, from code.

## Extensions
- [Data Wrangler](https://code.visualstudio.com/docs/datascience/data-wrangler) is a code-centric data viewing and cleaning tool that is integrated into VS Code and VS Code Jupyter Notebooks.

## Julia VScode
- [Julia for VSCode](https://www.julia-vscode.org/)
- [Using GDB & VSCode to debug Julia code on Windows](https://vchuravy.dev/notes/2021/09/vscode-gdb/)

## Python VScode
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
	- install the Python extension for VS Code from the Visual Studio Marketplace. [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## R VScode & Positron
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)
- [Positron has experimental support for Remote SSH sessions.](https://positron.posit.co/remote-ssh.html)

## Kun Ren
- Base. [R Extension for Visual Studio Code](https://github.com/REditorSupport/vscode-R)
	- [Option to lunch a Shiny app in the browser by default #1195 {Closed}](https://github.com/REditorSupport/vscode-R/issues/1195)
	- [R Session Watcher: Shiny apps in webviewer without local storage #154 {Closed}](https://github.com/REditorSupport/vscode-R/issues/154)
- [Kun Ren - Using R in VS Code](https://www.youtube.com/watch?v=9xXBDU2z_8Y)
- [My recommendations of VS Code extensions for R](https://renkun.me/2022/03/06/my-recommendations-of-vs-code-extensions-for-r/). 2022-03-06
- [Writing R in VSCode: A Fresh Start](https://renkun.me/2019/12/11/writing-r-in-vscode-a-fresh-start/). 2019-12-11. This article will be updated to reflect the latest languageserver features.

Настраиваем просто по инструкциям к плагинам:
- [R Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)
- [R Debugger](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger)
- [Changing R version in VS Code](https://stackoverflow.com/questions/72707869/changing-r-version-in-vs-code)
- [Quarto](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)

## Другие
- [VSCode vs RStudio — Worth the Switch?](https://towardsdatascience.com/vscode-vs-rstudio-worth-the-switch-7a4415fc3275)
- [Using R in VS Code](https://schiff.co.nz/blog/r-and-vscode/). Some things I learned while trying out R in VS Code
- [VSCode Snippets for R and R Markdown](https://github.com/SidhuK/r-snippets)
- [YAML Intelligence](https://quarto.org/docs/tools/vscode.html#yaml-intelligence)
- [VS Code setup for R](https://gist.github.com/strengejacke/82e8d7b869bd9f961d12b4091c145b88) gist различных настроек и пояснения.
- Analytics Vidhya. [A fresh start for R in VSCode](https://medium.com/analytics-vidhya/a-fresh-start-for-r-in-vscode-ec61ed108cf6). Setting up Visual Studio Code for R development
- [How to integrate Python and R in Visual Studio Code](https://towardsdatascience.com/how-to-integrate-python-and-r-in-visual-studio-code-496a47c90422)
- COOL! [R in 2021 with VSCode](https://datamares.netlify.app/en/post/r-vscode/)
- [Writing R in VSCode: A Fresh Start](https://renkun.me/2019/12/11/writing-r-in-vscode-a-fresh-start/)
	- [VSCode](https://code.visualstudio.com/Download): Visual Studio Code
	- [languageserver](): An implementation of the Language Server Protocol for R. `install.packages("languageserver")`
	- [VSCode R Extension](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r): An implementation of the Language Server Protocol for R by Yuki Ueda. 
	Правая кнопка на extension позволяет перейти в режим редактирования настроек.
	- [R LSP Client for VSCode](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r-lsp): R LSP Client for Visual Studio Code
	- [Python](https://www.python.org/downloads/)
	- [Radian](https://github.com/randy3k/radian): A 21st century R console.
		- [Add support for Windows UTF-8 version of R #269 {Closed}](https://github.com/randy3k/radian/issues/269)
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
Finally, you need to change your VSCode settings to enable R within the editor. For that press Ctrl + Shift + P and type in **“Preferences: Open Settings (JSON)” and press Enter. This will open the settings.json of your editor**. Add the following code to the JSON file, adjust the respective path to your setup and save the file.
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

- [GitHub and Visual Studio Code](https://vscode.github.com/)
- [Visual Studio Code Docs](https://code.visualstudio.com/docs)
- [REMOTE PAIR PROGRAMMING IN R USING VISUAL STUDIO CODE AND LIVE SHARE](https://ivelasq.rbind.io/blog/vscode-live-share/)
- [REditorSupport/vscode-R v2.3.0](https://github.com/REditorSupport/vscode-R/releases/tag/v2.3.0)

## Настройка под RMarkdown
- [R Markdown Notebook in VS code](https://yingqijing.medium.com/r-markdown-notebook-in-vs-code-3adb5a61417a)

# Positron
- COOL! [Fun with Positron](https://www.andrewheiss.com/blog/2024/07/08/fun-with-positron/)
Combine the best of RStudio and Visual Studio Code in Posit’s new Positron IDE
- [Positron](https://github.com/posit-dev/positron), a next-generation data science IDE
- [R code formatting #5534 {Closed}](https://github.com/posit-dev/positron/issues/5534)


## extensions
- Расширение [pastum](https://marketplace.visualstudio.com/items?itemName=atsyplenkov.pastum). Pastum: paste as ... dataframe
	- [Сайт разработчика](https://pastum.anatolii.nz/). This VS Code extension allows you to quickly transform any text table from your clipboard into a dataframe object in your favorite language — R , Python , Julia  or JavaScript
	- [HTML Table to DataFrame Tool](https://web-apps.thecoatlessprofessor.com/data/html-table-to-dataframe-tool.html)
- [Visual Studio Code - is there a Compare feature like that plugin for Notepad ++?](https://stackoverflow.com/questions/30139597/visual-studio-code-is-there-a-compare-feature-like-that-plugin-for-notepad)
- COOL! [Quarto Wizard](https://github.com/mcanouil/quarto-wizard) is a Visual Studio Code extension that assists you in managing Quarto projects.
- [Use agent mode in VS Code](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- Это оказалось для мака! [How to install the Work with Apps Visual Studio Code extension](https://help.openai.com/en/articles/10128592-how-to-install-the-work-with-apps-visual-studio-code-extension)

## 20.09.2021
- Проблема с юникодными строками в Windows. Возможно, надо задавать явно параметр `encoding` в `source` в `setting.json`
```
// R path for Linux
"r.rterm.linux": "/mnt/Storage/home/xx/miniconda3/envs/tools/bin/radian“,

// R command line options (i.e: --vanilla)
"r.rterm.option": [--no-save --no-restore],

// An optional encoding to pass to R when executing the file, i.e. 'source(FILE, encoding=ENCODING)'
"r.source.encoding": "UTF-8",
```
Для поиска по настройкам жмем `Ctrl+Shift+P`.

## 19.10.2021
- [How not to be lost with VSCode when coming from RStudio?](https://statnmap.com/2021-10-09-how-not-to-be-lost-with-vscode-when-coming-from-rstudio/)

## 13.09.2021
- Получил такое сообщение при запуске VScode: "The R language server extension has been integrated into vscode-R. You need to disable or uninstall REditorSupport.r-lsp and reload window to use the new version.". Видимо, надо отключить [https://github.com/REditorSupport/vscode-r-lsp](R LSP Client for Visual Studio Code)

# JetBrains DataSpell
- Настройка окружения для R. [Setup your environment](https://www.jetbrains.com/help/dataspell/setup-r-environment.html).
Сначала надо поставить плагин для R. [Manage plugins](https://www.jetbrains.com/help/dataspell/managing-plugins.html)
- [R plugin support](https://www.jetbrains.com/help/dataspell/r-plugin-support.html)