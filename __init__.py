import tkinter as tk
import os
window = tk.Tk()
window.title("")
window.resizable(False, False)
window.geometry("300x300")
textboxes = {}
def WindowConfig(winX, winY, Name):
    global window
    window.geometry(str(winX) + 'x' + str(winY))
    window.title(Name)


def Label(textContent):
    newLabel = tk.Label(window, text=textContent)
    newLabel.pack()


def Button(textContent, callbackFunctionName):
    newButton = tk.Button(window, text=textContent,
                          command=callbackFunctionName)
    newButton.pack()


def Textbox(name, width):
    newTextBox = tk.Entry(window, width)
    newTextBox.pack()
    # Store reference to the newly created textbox
    textboxes[name] = newTextBox
    newTextBox.bind("<Return>", lambda event: GetText(name))


def GetText(name):
    textbox = textboxes.get(name)
    if textbox:
        return textbox.get()
    else:
        print(f"Textbox with name '{name}' does not exist.")
        return ''

def TaggedLabel(textContent, ID):
    os.system("python3 import tkinter as tk")
    os.system("python3 import os")
    os.system(f"python3 {ID} = tk.Label(window, {textContent})")
    os.system(f"python3 {ID}.pack()")
def DeleteLabel(ID):
    os.system("python3 import tkinter as tk")
    os.system("python3 import os")
    os.system(f"python3 {ID}.destroy()")
def runApp():
    tk.mainloop()
