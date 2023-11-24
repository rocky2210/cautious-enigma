# Author :  Lila

from tkinter import *

root = Tk()
root.title("Remove labels")
root.iconbitmap("assets/fire.ico")
root.geometry("400x400")
'''
def myDelete():
    # root_Label.pack_forget()
    # root_Label.destroy()
    root_Label.grid_forget()
    myButton['state'] = NORMAL
    # print(myButton.winfo_exists())
'''
root_Label = Label(root)

def myClick():
    global root_Label
    root_Label.destroy()
    hello = "Hello " + root_entry.get()
    root_Label = Label(root, text=hello)
    root_entry.delete(0,'end')
    root_Label.grid(row=3,column=0,pady=10)
    # myButton['state'] = DISABLED


root_entry = Entry(root, width=17, font=('Arial',30))
root_entry.grid(row=0,column=0,padx=10,pady=10)

myButton = Button(root, text="Enter you name: ",command=myClick)
myButton.grid(row=1,column=0,pady=10)

# DeleteButton = Button(root,text="Delete Text",command=myDelete)
# DeleteButton.grid(row=2,column=0,pady=10)

root.mainloop()