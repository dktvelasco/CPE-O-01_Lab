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
