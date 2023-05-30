import tkinter as tk
window = tk.Tk()
window.title("")
window.resizable(False, False)
window.geometry("300x300")
# New global dictionary to store created textboxes
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


def Textbox(name):
    newTextBox = tk.Entry(window, width=30)
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


def runApp():
    tk.mainloop()
