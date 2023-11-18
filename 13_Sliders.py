# Author :  Lila

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.iconbitmap('assets/fire.ico')
root.geometry("400x400")
# vertical slider
vertical = Scale(root, from_= 0,to=200)
vertical.pack()

def slide():
    root_label = Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x"+ str(vertical.get()))

# Horizontal slider
horizontal = Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()


root_button = Button(root,text="click me!",command=slide).pack()

root.mainloop()
