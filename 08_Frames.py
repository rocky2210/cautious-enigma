# Author :  Lila

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frames")
root.iconbitmap('assets/fire.ico')

# Frame
frame = LabelFrame(root, text="Text is my frame..",padx=50,pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame,text="Click me ")
b2 = Button(frame,text="Click me ")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)


root.mainloop()