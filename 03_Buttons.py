# Author :  Lila

from tkinter import *

root = Tk()

#Click function
def myClick():
	myLabel = Label(root, text="Clicked button 😋")
	myLabel.pack()

#Creating a Button Widget
myButton1 = Button(root, text="Click me", command=myClick, fg="blue", bg="black")
# myButton2 = Button(root, text="Click me",state=DISABLED)
# myButton3 = Button(root, text="Click me",padx=50,pady=50)

#pack
myButton1.pack()
# myButton2.pack()
# myButton3.pack()

#loops untill exits
root.mainloop()