# Lesson 0: Getting started
In this lesson we'll install everything you need, write your first Python program, and learn how to run Python code in two different ways.

To-do:
- [ ] Install Python
- [ ] Install VS Code
- [ ] Optional: Install VS Code extensions
- [ ] Optional: Install Thonny
- [ ] Optional: Install `uv`
- [ ] Write and run a simple `hello_world.py` program
- [ ] Try out Python's interactive mode

## Installing Python
Python is the programming language you'll be learning with me. It's a powerful language that's fun and easy to learn. To install it on your computer, follow the steps below.
1. Download and install the latest version of Python from [python.org/downloads](https://python.org/downloads) using the installer.
    - **Windows:** on the first screen of the installer, make sure you tick the box that says **"Add python.exe to PATH"**. If you forget to do this, your terminal won't be able to find Python.

2. Check whether it installed correctly by opening your terminal. Instructions on how to do this vary by operating system:
    - **macOS:** Open the Terminal app (press `⌘` + `Space` to open Spotlight, then search "terminal").
    - **Debian-based Linux:** Open the Terminal app (press `Super` + `A` to open the Show Applications menu, then search "Terminal").
    - **Windows:** Open PowerShell (search for "PowerShell" in the start menu).

   Then enter the command `python --version`. If Python is installed, this will print something like `Python 3.14.0` to the terminal. If it prints an error message, then Python was not installed correctly.

> [!NOTE]
> On macOS and Linux, the command is often `python3` rather than `python`. If `python --version` gives you an error, try `python3 --version` instead. Wherever you see `python` in these lessons, just use `python3`.

## Installing VS Code
Visual Studio Code (commonly abbreviated as 'VS Code') is an integrated development environment (IDE) developed by Microsoft for Windows, Linux, macOS and web browsers. It's an application that allows you to write and run your code more easily. While you don't technically _need_ this (you could just write everything in a basic editor and run your code from the command line), it makes life a lot easier when you're getting started. To install it:
1. Download the VS Code installer from [code.visualstudio.com/download](https://code.visualstudio.com/download).
2. Open your Downloads folder and double-click on the installer. It will be called something like `VSCodeUserSetup-x64-1.105.0.exe` on Windows or `VSCode-darwin-universal.zip` on macOS.
3. Follow the default installation options.

When the installation is complete, you can open VS Code by searching "code" in your application launcher (e.g. on macOS, press `⌘` + `Space` to open Spotlight, then search "code"; on Windows, open the start menu and search "code").

## Optional: Installing VS Code extensions
You can customise your experience with VS Code by installing various extensions. To install extensions:
1. Click on the "Extensions" tab on the left (stacked blocks icon). Alternatively, press `Ctrl` + `Shift` + `x` on Windows or `⌘` + `Shift` + `x` on macOS.
2. Search for the name of the extension you'd like to install.
3. Optional: click on it to read about it.
4. Click the "Install" button.

I recommend installing the following:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): a bundle of Python extensions that give you auto-completion, code navigation, syntax checking, and a run button.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): an extension to VS Code's Markdown renderer that allows VS Code to render non-standard markdown like `- [ ]` to-do blocks. I make frequent use of these, so it will make it easier for you to read my documents if you install this.

## Optional: Installing Thonny
If you have to sit an on-screen exam, it's quite likely that you will not be given access to a full batteries-included IDE like VS Code. Many schools instead let students use Thonny, which is a stripped-back Python IDE. It's worth installing now so that it's not unfamiliar if you have to use it later.
1. Download the Thonny installer from [thonny.org](https://thonny.org/).
2. Open your Downloads folder and double-click on the installer. It will be called something like `thonny-4.1.7.pkg` on macOS or `thonny-4.1.7.exe` on Windows.
3. Follow the default installation options.

You cannot customise Thonny in the same way you can customise VS Code, but everything we write in these lessons will run in Thonny too. (See the [exam board notes](../../exam-board-notes) for more about how each exam board assesses programming.)

## Optional: Installing `uv`
[`uv`](https://docs.astral.sh/uv/) is a tool that manages Python versions and Python _packages_ (code that other people have written that you can download and use in your own programs). You don't need it for most of these lessons — for the most part, we'll just run our code with `python` — but we will use it later on when we start using third-party packages like `matplotlib`. It's also what professional Python developers increasingly use, so it's worth getting used to. To install it, run the following command in your terminal:
- **macOS / Linux:**
  ```sh
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Windows (PowerShell):**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

Close and re-open your terminal, then check it installed correctly with `uv --version`.

> [!TIP]
> If you had trouble installing Python earlier, `uv` can install it for you! Just run `uv python install`.

## Writing your first program: `hello_world.py`
Now it's time to write our first Python program! Before we write any code, I recommend creating a folder on your computer that we can use to save our code from now on. To do this, follow the steps below.

**macOS:**
1. Open Finder (icon should appear in the dock, alternatively press `⌘` + `Space` to open Spotlight, then search "finder").
2. Navigate to wherever you would like to put this folder. For example, your `Documents` folder.
3. Right-click then select "New Folder" and call it something sensible, such as `python-lessons`.

**Windows:**
1. Open the File Explorer (just search "file" in the start menu then press the `Enter` key).
2. Scroll down on the left pane until you see "This PC". Click it, then double-click on "Local Disk (C:)". This is your "local" home storage — files stored here are physically stored on your computer, rather than "in the cloud" through OneDrive. In general, it's always better to store and run your code locally so you don't run into synchronisation issues with cloud services.
3. From here, click on "Users" then your username (for me, this is "Bailey"). You should now see lots of folders like "Documents", "Downloads", etc.
4. Create a new folder here by pressing the "New" button (top-left) then clicking "Folder". Alternatively, you can just press `Ctrl` + `Shift` + `n`. Give the folder a sensible name, such as `python-lessons`.

We're now ready to open this folder in VS Code. To do this, follow the steps below.
1. Open VS Code.
2. Click on the "Open..." button (or "File" → "Open Folder...") and navigate to your new folder by following the same steps as before. Once you've found it, press the "Select Folder" (or "Open") button to open that folder.
3. Click on the "New File" button and select "Python File" if prompted for the file type. We're now ready to write our first program!

A rite of passage for all new programmers is to write a "Hello world" program. This is a simple program that displays a "Hello world" message on the screen. We can do this in Python using the following code:
```python
print("Hello world")
```

**Task 1:** Type (or copy & paste) this code into your editor, then save the file as `hello_world.py`. Run the code by pressing the "Run" button (top-right; looks like a triangular 'play' button). You should see a "Hello world" message displayed in the terminal at the bottom of the screen. Try changing the text between the quotation marks to see if the output of the program changes when you next run it. [Solution](solutions/task1_hello_world.py)

> [!TIP]
> Notice that I called the file `hello_world.py` and not `Hello World.py`. It's good practice to name your Python files using lowercase letters with underscores instead of spaces (this is called `snake_case`). Spaces in file names cause all sorts of headaches when you're working in the terminal.

## Running your code from the terminal
The "Run" button is convenient, but all it's really doing is typing a command into the terminal for you. It's useful to know how to do this yourself. Open a terminal in VS Code by clicking on "Terminal" at the top of the screen, then clicking "New Terminal" (or press `Ctrl` + `` ` `` on Windows or `⌃` + `` ` `` on macOS). The terminal will open in the folder you're working in. Then type:
```sh
python hello_world.py
```

and press `Enter`. You should see the same output as before.

## Comments
Any text after a `#` symbol is ignored by Python. These are called _comments_, and we use them to explain what our code is doing to other people (or to ourselves in a few weeks' time, when we've forgotten!). For example:
```python
# This line is ignored by Python
print("This line is not")  # comments can go at the end of a line too
```

**Task 2:** Write a program called `about_me.py` that prints three lines: your name, your favourite food, and one fact about yourself. Add a comment at the top of the file explaining what the program does. [Solution](solutions/task2_about_me.py)

## Running Python in interactive mode
More often than not, you will run Python code as you did above (i.e. save code to a `.py` file then run it). Sometimes though, it's nice to be able to execute code one line at a time. To do this, we can run the Python interpreter in "interactive mode":
1. Open a terminal in VS Code (as above).
2. Type `python` (or `python3`) and press `Enter`. This will open the Python interpreter in interactive mode. You'll know it's worked because you'll see a `>>>` prompt.
3. Enter Python code, for example: `print("I'm alive!")` or `42 + 50`.
4. When you're done, type `exit()` and press `Enter` to go back to the normal terminal.

The output should look something like:
```console
PS C:\Users\bailey\python-lessons> python
Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("I'm alive!")
I'm alive!
>>> 42 + 50
92
>>> x = 9
>>> x * x
81
>>> exit()
```

Interactive mode is very helpful if you just want to figure out how something works or test a short snippet of code. When you're writing more complicated programs though, it's best to save them to a `.py` file (this way you can re-use them!).

**Task 3:** Use interactive mode as a calculator to work out the following. [Solution](solutions/task3_interactive_mode.md)
1. The number of seconds in a day.
2. The number of seconds in a (non-leap) year.
3. $2^{10}$. Hint: in Python, powers are written with `**`, so $3^2$ is `3**2`.
4. What happens if you type `7 / 2`? What about `7 // 2`? Can you guess what `//` does?

**⭐ Task 4:** Write a program called `initials.py` that prints your initials in big letters made out of `#` symbols, like the example below. [Solution](solutions/task4_initials.py)
```
#####   ####
#    # #
#####  #
#    # #
#####   ####
```

---
[Contents](../../README.md) | [Next: Lesson 1 →](../01-variables-and-types)
