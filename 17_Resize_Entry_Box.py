# Author :  Lila

from tkinter import *

root = Tk()
root.title("Resize entry box");
root.iconbitmap("assets/fire.ico")
root.geometry("400x400")

def myClick():
    hello = "Hello " + root_entry.get()
    root_Label = Label(root, text=hello)
    root_entry.delete(0,'end')
    root_Label.pack(pady=10)

root_entry = Entry(root, width=50, font=('Arial',14))
root_entry.pack(padx=10,pady=10)

myButton = Button(root, text="Enter you name: ",command=myClick)
myButton.pack(pady=10)

root.mainloop()