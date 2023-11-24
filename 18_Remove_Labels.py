# Author :  Lila

from tkinter import *

root = Tk()
root.title("Remove labels")
root.iconbitmap("assets/fire.ico")
root.geometry("400x400")

def myDelete():
    # root_Label.pack_forget()
    root_Label.destroy()
    myButton['state'] = NORMAL
    print(myButton.winfo_exists())

def myClick():
    global root_Label
    hello = "Hello " + root_entry.get()
    root_Label = Label(root, text=hello)
    root_entry.delete(0,'end')
    root_Label.pack(pady=10)
    myButton['state'] = DISABLED


root_entry = Entry(root, width=50, font=('Arial',14))
root_entry.pack(padx=10,pady=10)

myButton = Button(root, text="Enter you name: ",command=myClick)
myButton.pack(pady=10)

DeleteButton = Button(root,text="Delete Text",command=myDelete)
DeleteButton.pack(pady=10)

root.mainloop()