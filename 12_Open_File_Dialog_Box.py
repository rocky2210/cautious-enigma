# Author :  Lila

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open file dialog box")
root.iconbitmap('assets/fire.ico')

# root.filename = filedialog.askopenfilename(initialdir="assets/",title="select a file",filetypes=(("jpeg files","*.jpeg"),("all files","*.*")))
# root_label = Label(root,text=root.filename).pack()
# root_image = ImageTk.PhotoImage(Image.open(root.filename))
# root_image_label = Label(image = root_image).pack()

def open():
    global root_image
    root.filename = filedialog.askopenfilename(initialdir="assets/",title="select a file",filetypes=(("jpeg files","*.jpeg"),("all files","*.*")))
    root_label = Label(root,text=root.filename).pack()
    root_image = ImageTk.PhotoImage(Image.open(root.filename))
    root_image_label = Label(image = root_image).pack()

root_button = Button(root,text="Open file",command=open).pack()

root.mainloop()
