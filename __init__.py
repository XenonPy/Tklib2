import tkinter as tk
window = tk.Tk()
window.title("")
window.resizable(False, False)
window.geometry("300x300")
def WindowConfig(winX, winY, Name):
  global window
  window.geometry(str(winX) + 'x' + str(winY))
  window.title(str(Name))
def Label(textContent):
  newLabel = tk.Label(window, text=textContent)
  newLabel.pack()
def Button(textContent, callbackFunctionName):
  newButton = tk.Button(window, text=textContent, command=callbackFunctionName)
  newButton.pack()
def runApp():
  tk.mainloop()