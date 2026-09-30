# Lesson 1: Installing Python, writing a hello world program, and interactive mode
To-do:
- [ ] Install Python
- [ ] Install VS Code
- [ ] Optional: Install Pylance extension
- [ ] Optional: Install Markdown All in One extension
- [ ] Write a simple `hello-world.py` program

## Installing Python
Python is the programming language you'll be learning with me. It's a powerful language that's fun and easy to learn. To install it on your computer, follow the steps below.
1. Download and install the latest version of Python from [python.org/downloads](https://python.org/downloads) using the installer.

2. Check whether it installed correctly by opening your terminal. Instructions on how to do this vary by operating system:
    - **macOS:** Open the Terminal app (press `⌘` + `Space` to open Spotlight, then search "terminal").
    - **Debian-based Linux:** Open the Terminal app (press `Super` + `A` to open the Show Applications menu, then search "Terminal").
    - **Windows:** Open PowerShell (search for "PowerShell" in the start menu).
Then enter the command `python --version`. If Python is installed, this will print something like `Python 3.12.4` to the terminal. If it returns nothing or prints an error message, then Python was not installed correctly.

## Installing VS Code
Visual Studio Code (commonly abbreviated as 'VS Code') is an integrated development environment (IDE) developed by Microsoft for Windows, Linux, macOS and web browsers. It's an application that allows you to write and run your code more easily. While you don't technically _need_ this (you could just write everything in a basic editor and run your code from the command line), it makes life a lot easier when you're getting started. To install it:
1. Download the VS Code installer from [code.visualstudio.com/download](https://code.visualstudio.com/download).
2. Open your Downloads folder and double-click on the installer. It will be called something like `VSCodeUserSetup-x64-1.93.1` on Windows or `VSCode-darwin-arm64.dmg` on macOS.
3. Follow the default installation options

When the installation is complete, you can open VS Code by searching "code" in your application launcher (e.g. on macOS, press `⌘` + `Space` to open Spotlight, then search "code"; on Windows, open the start menu and search "code").

## Optional: Installing VS Code Extensions
You can customise your experience with VS Code by installing various extensions. To install extensions:
1. Click on the "Extensions" tab on the left (stacked blocks icon). Alternatively, or press `Ctrl` + `Shift` + `x` on Windows or `⌘`+ `Shift` + `x` on macOS
2. Search for the name of the extension you'd like to install
3. Optional: click on it to read about it.
4. Click the "Install" button.

I recommend installing the following:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): a bundle of Python extensions that give you auto-completion, code navigation, syntax checking, and a run button.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): an extension to VS Code's Markdown renderer that allows VS Code to render non-standard markdown like `- [ ]` to-do blocks. I make frequent use of these, so it will make it easier for you to read my documents if you install this.

## Installing Thonny
If you have to sit an on-screen exam as part of your GCSE, it's quite likely that you will not be given access to a full batteries-included IDE like VS Code. Most schools instead allow students to use Thonny, which is a stripped-back Python IDE. I'd recommend installing this now in case we have to use it later.
1. Download the Thonny installer from [thonny.org/](https://thonny.org/).
2. Open your Downloads folder and double-click on the installer. It will be called something like `thonny-5.0.0-arm64.pkg` on macos or `thonny-5.0.0-x64.exe` on Windows.
3. Follow the default installation options

You cannot customise Thonny in the same way you can customise VS Code.

I recommend installing the following:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): a bundle of Python extensions that give you auto-completion, code navigation, syntax checking, and a run button.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): an extension to VS Code's Markdown renderer that allows VS Code to render non-standard markdown like `- [ ]` to-do blocks. I make frequent use of these, so it will make it easier for you to read my documents if you install this.

## Writing your first program: `hello-world.py`
Now it's time to write our first Python program! Before we write any code, I recommend creating a folder on your computer that we can use to save our code from now on. To do this, follow the steps below.
**macOS**:
1. Open Finder (icon should appear in the dock, alternatively press `⌘` + `Space` to open Spotlight, then search "finder")
2. Navigate to wherever you would like to put this folder. For example, your `Documents` folder.
3. Right-click then click select "New Folder" and call it something sensible, such as `python-lessons`

**Windows**:
1. Open the File Explorer (just search "file" in the start menu then press the `Enter` key)
2. Scroll down on the left pane until you see "This PC". Click it, then double-click on "Local Disk (C:)". This is your "local" home storage -- files stored here are physically stored on your computer, rather than "in the cloud" through OneDrive. In general, it's always better to store and run your code locally so you don't run into synchronisation issues with cloud services.
3. From here, click on then "Users" then your username (for me, this is "Bailey"). You should now see lots of folders like "Documents", "Downloads", etc.
4. Create a new folder here by pressing the "New" button (top-left) then clicking "Folder". Alternatively, you can just press `Ctrl + Shift + n`. Give the folder a name, such as `Tutoring` or `Programming`.

We're now ready to open this folder in VS Code. To do this, follow the steps below.
1. Open VS Code by searching "code" in your application launcher (e.g. on macOS, press `⌘` + `Space` to open Spotlight, then search "code"; on Windows, open the start menu and search "code")
2. Click on the "Open..." button and navigate to your new folder by following the same steps as before. Once you've found it, press the "Select Folder" button to open that folder.
3. Click on the "New File" button and select "Python File" if prompted for the file type. We're now ready to write our first program!

A right of passage for all new programmers is to write a "Hello world" program. This is a simple program that displays a "Hello world" message on the screen. We can do this in Python using the following code:
```python
print("Hello world")
```

1. Type (or copy & paste) this code into your editor, then save the file as `hello-world.py`.
2. Run the code by pressing the "Run" button (top-right; looks like a triangular 'play' button). You should see a "Hello world" message displayed in the terminal. 
2. Try changing the text between the quotation marks to see if the text output of the program changes when you next run it.

## Running Python in interactive mode
More often than not, you will run Python code as you did above (i.e. save code to a `.py` file then run the code). Sometimes though, it's nice to be able to execute code one line at a time. To do this, we can run the Python interpretter in "interactive mode". To do this, follow the instructions below.
1. Open a terminal in VS Code by clicking on the "Terminal" button at the top of the screen, then clicking "New Terminal" (or just press `Ctrl` + `Shift` + `\`` on Windows, or `⌘` + `Shift` + `\`` on macOS)
2. Type `python` (or `python3`) and press `Enter`. This will open the Python interpretter in interactive mode
3. Enter Python code, for example: `print("I'm alive!")` or `42 + 50`
   
The output should look something like:
```python
PS C:\Users\bailey\Tutoring\python> python
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("I'm alive!")
I'm alive!
>>> 42 + 50
92
>>> x = 9
>>> x * x
81
```

Interactive mode is very helpful if you just want to figure out how something works or test a short snippet of code. When you're writing more complicated programs though, it's often best to save them to a `.py` file (this way you can re-use them!).
