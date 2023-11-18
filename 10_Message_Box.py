# Author :  Lila

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('assets/fire.ico')

# Message box
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.showinfo ("This is my popup!","Hello world!") # (title,message)
    Label(root, text=response).pack()
    if response == 1:
        Label(root,text="You clicked yes").pack()
    else:
        Label(root,text="You clicked yes").pack()

Button(root,text="popup",command=popup).pack()

root.mainloop()
