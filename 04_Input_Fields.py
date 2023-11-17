# Author :  Lila

from tkinter import *

root = Tk()

#Creating a Input field (entry widget)
e1 = Entry(root,width=50)
# e2 = Entry(root,width=50,fg="white",bg="black",borderwidth=5,show="*")
# e3 = Entry(root,width=50,fg="white",bg="black",borderwidth=5,relief="raised")
e1.pack()
# e2.pack()
# e3.pack()
e1.insert(0,"Enter your name: ") #Insert default text 


#Click function
def myClick():
	msg= "Hello " + e1.get()
	myLabel = Label(root,text = msg)
	myLabel.pack()

#Creating a Button Widget
myButton1 = Button(root, text="Submit", command=myClick,)
myButton1.pack()

#loops untill exits
root.mainloop()