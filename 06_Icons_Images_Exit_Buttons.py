# Author :  Lila

from tkinter import *
from PIL import ImageTk,Image # Imaging Library adds image processing capabilities to your Python interpreter.

root = Tk()
root.title("Icons images and Exit")

# Icon (use .ico) 
root.iconbitmap('assets/fire.ico')


# Images
my_image = ImageTk.PhotoImage(Image.open("assets/pythonlogo.png"))
my_label = Label(image=my_image)
my_label.pack()

# Quit button
button_quit = Button(root, text="Quit.." ,command=root.quit)
button_quit.pack()


root.mainloop()