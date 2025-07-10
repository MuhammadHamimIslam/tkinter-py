import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def btn1_command(): 
    label["text"] = "Button 1 is clicked!"
def btn2_command(): 
    label["text"] = "Button 2 is clicked!"
def click_fn(): 
    showinfo(
        title="Information",
        message='Download button is clicked.But what to download?'
    ) # showing a messagebox

root = tk.Tk() # main window
root.title("Adding button")

label = tk.Label(root, text="Hello World", bg="black", fg="#FA0000")
label.pack()

btn1 = tk.Button(root, text="Click me", bg="#0081ff", fg="#fff", command=btn1_command) # adds a button from tk class text is Click me and tje function will be called after clicked 

# styling ttk button 
btn2_style = ttk.Style() # instantiate the style 
btn2_style.configure("btn2_style.TButton", background="#2b90dc", foreground="#0F0000")

btn2 = ttk.Button(root, text="Click me too", command=btn2_command, style="btn2_style.TButton") # adds a button from ttk class text is Click me and tje function will be called after clicked 

# setting button state
btn2.state(["disabled"]) # disable the button

# displaying image in button
image = tk.PhotoImage(file="assets/download.png") # image
btn_img = tk.Button(root, image=image, text="download", compound=tk.RIGHT, command=click_fn)
btn_img.pack(padx=10, pady=15)

btn1.pack()
btn2.pack()

root.mainloop()