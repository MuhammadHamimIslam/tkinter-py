import tkinter as tk
from tkinter import ttk

def btn1_command(): 
    label["text"] = "Button 1 is clicked!"
def btn2_command(): 
    label["text"] = "Button 2 is clicked!"

root = tk.Tk() # main window
root.title("Adding button")

label = tk.Label(root, text="Hello World", bg="black", fg="#FA0000")
label.pack()

btn1 = tk.Button(root, text="Click me", bg="#0081ff", fg="#fff", command=btn1_command) # adds a button from tk class text is Click me and tje function will be called after clicked 

# styling ttk button 
btn2_style = ttk.Style() # instantiate the style 
btn2_style.configure("btn2_style.TButton", background="#2b90dc", foreground="#0F0000")


btn2 = ttk.Button(root, text="Click me too", command=btn2_command, style="btn2_style.TButton") # adds a button from ttk class text is Click me and tje function will be called after clicked 


btn1.pack()
btn2.pack()

root.mainloop()