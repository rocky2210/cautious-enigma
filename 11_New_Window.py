# Author :  Lila

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New Window")
root.iconbitmap('assets/fire.ico')

def open():
    global top_image
    # Toplevel to create second window
    top = Toplevel()
    # top_label = Label(top,text="hello from top").pack()
    top.title("Second window")
    top.iconbitmap('assets/fire.ico')
    top_image = ImageTk.PhotoImage(Image.open("assets/asta.jpeg"))
    top_label = Label(top,image=top_image).pack()
    top_button = Button(top,text="close",command=top.destroy).pack()

root_button = Button(root, text="open second window",command=open).pack()

root.mainloop()
