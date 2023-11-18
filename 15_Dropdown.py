# Author :  Lila

from tkinter import *

root = Tk()
root.title('Drop down')
root.iconbitmap('assets/fire.ico')
root.geometry("500x500")

def show():
    root_label = Label(root,text=clicked.get()).pack()

fav_foods = ["Rose milk","Cake","Milk shake"]

clicked = StringVar()
clicked.set(fav_foods[0])
root_drop = OptionMenu(root,clicked,*fav_foods)
root_drop.pack()

root_button = Button(root,text="show selection",command=show).pack()
root.mainloop()