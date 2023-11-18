# Author :  Lila

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Button")
root.iconbitmap('assets/fire.ico')

# Radio Button
r = IntVar()
r.set(2)

SHOP = [
    ("Rosemilk", "Rosemilk"),
    ("Ice cream", "Ice cream"),
    ("Cake", "Cake"),
    ("Milk shake", "Milk shake"),
]

food = StringVar()
food.set("Rosemilk")

for text, mode in SHOP:
    Radiobutton(root, text=text, variable=food, value=mode).pack(anchor=W)

def click():
    my_label = Label(root, text=food.get())
    my_label.pack()

Mybutton = Button(root, text="click me", command=click)
Mybutton.pack()

# my_label = Label(root, text=food.get())
# my_label.pack()

root.mainloop()
