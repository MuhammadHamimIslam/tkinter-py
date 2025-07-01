import tkinter as tk
from tkinter import ttk

def show_state1(): 
    is_checked = var1.get()
    if is_checked: 
        root.config(background="#000")
    else:
        root.config(background="#fff")
def show_state2(): 
    is_checked = var2.get()
    if is_checked: 
        root.config(background="#000")
    else:
        root.config(background="#fff")        
        
root = tk.Tk()
root.title("Adding Check box")
# adding check button
var1 = tk.IntVar()
check_box1 = tk.Checkbutton(root, text="Click me!", variable=var1, command=show_state1) # adds a check button from Tk class
check_box1.select() # select the check btn
check_box1.pack(padx=10, pady=10)

var2 = tk.IntVar()
check_box2 = ttk.Checkbutton(root, text="Click me!", variable=var2, command=show_state2) # adds a check button from ttk class 
 
check_box2.pack(padx=25, pady=30)

root.mainloop()