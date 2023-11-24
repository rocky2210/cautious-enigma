# Author :  Lila

from tkinter import *

root = Tk()
root.title("Remove labels")
root.iconbitmap("assets/fire.ico")
root.geometry("400x400")

class Rocky:
    def __init__(self, main):
        myFrame = Frame(main)
        myFrame.pack()

        self.myButton = Button(main, text="Click", command=self.click)
        self.myButton.pack(pady=20)

    def click(self):
        print("Look at you")


name = Rocky(root)
root.mainloop()