# Tklib2 Docs
This is the official documentation for Tklib2.
It covers everything as of version 0.2 (the first beta release).

## Installing Tklib2 
Download the source code from the releases page.
Then, decompress the file. Put the unzipped contents in a folder named 'tklib2' and load it into your Python project.
A CDN installation script is coming in the near future (expect it in the 0.5-beta).

## Importing Tklib2
```python
import tklib2 as tklib
```
Feel free to drop the alias if you want.

## Hello, World! in Tklib2
This is an example of a simple Tklib2 implementation for displaying "Hello, World!".
```python
import tklib2 as tklib
tklib.WindowConfig(300, 300, "My first Tklib2 program")
tklib.Label("Hello, World!")
tklib.runApp()
```
Now I'll explain each line of code and it's use.

`tklib.WindowConfig(300, 300, "My first Tklib2 program")`: This line configurates the main window. The first parameter is the x-pixels while the second is y-pixels. The third parameter is the window title. The default settings (without changing the window) are 300x300 and the title "Tklib2 Window".
`tklib.Label("Hello, World!")`: This line creates a simple label. It takes only one parameter.
`tklib.runApp()`: This line starts the main loop.

### Important Notes:
Because of Tklib2's 'building block' style, write your code like the following:
```python
tklib.Label("Do this")
```
and not
```python
myLabel = tklib.Label("Don't do this")
```

## Buttons in Tklib2
Consider the following code:
```python
import tklib2 as tklib
def printHello():
  tklib.Label("You clicked the button.")
tklib.WindowConfig(300, 300, "Buttons in Tklib2")
tklib.Label("v v Press Button v v")
tklib.Button("Say Hello", printHello)
tklib.runApp()
```
Here we're creating a button that creates a new label.
The code we haven't seen yet is the following:
`tklib.Button("Say Hello", printHello)`
This creates a button. The first parameter is the button text, and the second is the **name** of the callback fuction.
Notice there are no parentheses. This stops you from adding parameters, but since a button press is just one boolean, you probably won't be needing these.

## Labels in Tklib2
Labels are pretty straightforward:
```python
import tklib2 as tklib
tklib.Label("Hello Tklib2!")
tklib.Label("This text is blue!", "#56aaff")
```
The first parameter is the text. The second is optional and specifies the color as a string (in hex format).

## Images in Tklib2
Images are easy too!
```python
import tklib2 as tklib
banana = Image('banana.png', 10)
```
The first parameter is the image path. The second is again optional and is the padding as an **integer**. It defaults to 5.

## Textboxes in Tklib2
Now consider this code:
```python
import tklib2 as tklib
def printName():
  myname = tklib.GetText("firstname")
  tklib.Label(myname)
tklib.WindowConfig(300, 300, "Window Title Here")
tklib.Label("v v Press Button v v")
tklib.Textbox("firstname", 30)
tklib.Button("Print Name", printName)
tklib.runApp()
```
This creates a simple input and a button that displays the contents of the input.
Here are the lines we haven't seen yet explained:

`myname = tklib.GetText("firstname")`: The `GetText()` function gets the text value of a textbox based on a 'tag' parameter. The 'tag' parameter is also specified when creating a textbox (the second parameter is the width), so creating a textbox via `tklib.Textbox("NewTag", 30)` will bind the tag `NewTag` to the textbox. Then we can get it's content via `GetTag("NewTag")`. This is an exception to Tklib2's 'building block' grammar, as you **should** set it as the value of a variable and should **not** just write `tklib.GetTag("ExampleTag")` (You're not telling the computer where to store it!).
`tklib.Textbox("firstname", 30)`: Creates a textbox. The first parameter binds the tag (see the line above), the second is the width of the textbox (just like in standard Tkinter).

### Good Job!
You've finished reading the Tklib2 documentation!
Stay tuned for these new features planed for 0.3:
- Change default cursor
- Change text symbol when typing in textboxes (password input!)
- Tkinter Messageboxes in Tklib2


