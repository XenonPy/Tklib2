import tkinter as tk
import os
window = tk.Tk()
window.title("Tklib2 Window")
window.resizable(False, False)
window.geometry("300x300")
textboxes = {}
def WindowConfig(winX, winY, Name):
    global window
    window.geometry(str(winX) + 'x' + str(winY))
    window.title(Name)


def Label(textContent, color="#000000"):
    newLabel = tk.Label(window, text=textContent)
    newLabel.pack()
    newLabel.config(fg=color)


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


def Image(path, pd=5):
    try:
        imageRef = tk.PhotoImage(file=path)
        imageLabel = ttk.Label(window, image=imageRef, padding=pd)
        imageLabel.pack()
    except:
        Label('tkilb2: error when creating image tag')

def GetText(name):
    textbox = textboxes.get(name)
    if textbox:
        return textbox.get()
    else:
        print(f"Textbox with name '{name}' does not exist.")
        return ''
def runApp():
    tk.mainloop()
