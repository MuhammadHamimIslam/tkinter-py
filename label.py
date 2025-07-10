from tkinter import *

root = Tk()
root.geometry("500x150")

# adding text
label = Label(root, text="Hello, Python!", font=("Serif", 20), anchor="center", bg="#000000", fg="#FFFFFF", width=10, height=5) # a label is created under root with the text with font Helvetica, size 20, anchor center to center tje text

label.config(text="Hello Tkinter") # updating text
label.pack(expand=True) # add the label to the window , expand=True means it'll expand when resizing 

# adding image with Label
photo = PhotoImage(file="assets/cat_img.png") # open the .png image 
img = Label(root, image=photo) # set the image as Label 
img.pack(expand=True) # pack it

# showing both image and text
image = Label(root, image=photo, text="Beautiful cat's image", compound=TOP)
image.pack()

root.mainloop()