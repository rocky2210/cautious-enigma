from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text="Hello World").grid(row=0,column=0)
myLabel2 = Label(root, text="My name is rocky")

#grid
# myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

#loops untill exits
root.mainloop() 