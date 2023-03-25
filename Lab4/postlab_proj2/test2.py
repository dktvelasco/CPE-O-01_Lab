# Explore the Tkinter.filedialog module to get the name of a text file 

from tkinter import *
from tkinter import filedialog

def browseFiles():
    fileName = filedialog.askopenfilename(
        title = "Select text file",
        filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    label.configure(text="File Opened: "+fileName)
      
window = Tk()
window.title('Text File Explorer')
window.geometry("500x150")
window.config(background = "white")

label = Label(window, text = "Text file explorer with Tkinter", fg = "blue")
button_explore = Button(window, text = "Browse Files", command = browseFiles)
button_quit = Button(window, text = "Quit", command = exit)
  
label.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_quit.grid(column = 1,row = 3)

window.mainloop()
