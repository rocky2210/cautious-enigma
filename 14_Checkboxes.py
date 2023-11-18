# Author :  Lila

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Check box')
root.iconbitmap('assets/fire.ico')
root.geometry("500x500")

var = StringVar()
def show():
    root_label= Label(root, text=var.get()).pack()

root_checkbox = Checkbutton(root,text="Check box : food",variable=var,onvalue="Rose milk",offvalue="Cake")
root_checkbox.deselect()
root_checkbox.pack()
root_button = Button(root,text="show selection",command=show).pack()

root.mainloop()