# Author :  Lila

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple Image Viewer")
root.iconbitmap('assets/fire.ico')

# Images
my_img1 = ImageTk.PhotoImage(Image.open("assets/goku.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("assets/vegeta.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("assets/asta.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("assets/naruto.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("assets/luffy.jpeg"))

# List of images
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

image_number = 1


def forward():
    global image_number
    global my_label
    global button_forward
    global button_back

    if image_number < len(image_list):
        my_label.grid_forget()
        image_number += 1
        my_label = Label(image=image_list[image_number - 1])
        my_label.grid(row=0, column=0, columnspan=3)

        # Updating status bar
        status = Label(root,text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief="sunken",anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    else:
        button_forward['state'] = 'disabled'

    button_back['state'] = 'normal'


def back():
    global image_number
    global my_label
    global button_forward
    global button_back

    if image_number > 1:
        my_label.grid_forget()
        image_number -= 1
        my_label = Label(image=image_list[image_number - 1])
        my_label.grid(row=0, column=0, columnspan=3)

        # Updating status bar
        status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief="sunken",anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    else:
        button_back['state'] = 'disabled'

    button_forward['state'] = 'normal'


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Quit", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)  # Added indentation


# Status Bar
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief="sunken", anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
