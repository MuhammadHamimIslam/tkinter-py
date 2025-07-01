import tkinter as tk
from tkinter import ttk

def change_selected(event):
    label2.config(text=f"{event.widget.get()} selected!")
    label2.config(foreground=event.widget.get())

root = tk.Tk()
root.title("Adding Combo box")

label1 = tk.Label(root, text="What's your favorite color?").pack(padx=10, pady=20)

# adding combo box (html select tag)
combo_box = ttk.Combobox(root, values=["blue", "red", "green", "orange", "pink", "indigo", "violet", "yellow", "black"]) # adds a combo box from ttk class
combo_box.set("Blue") # initially set one value 
combo_box.bind("<<ComboboxSelected>>", change_selected) # event listener 
combo_box.pack(padx=10, pady=20, fill="both")


label2 = tk.Label(root, text="Blue selected!")
label2.pack(padx=20, pady=30) # helper label 

root.mainloop()