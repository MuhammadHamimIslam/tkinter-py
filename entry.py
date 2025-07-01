import tkinter as tk
from tkinter import ttk

def return_value(e): # event function 
    label2.config(text=f"Welcome {e.widget.get()}!")

root = tk.Tk()
root.title("Adding entry field")

label1 = tk.Label(root, text="What's your name?").pack(padx=10, pady=20)

# add entry field 
entry1 = tk.Entry(root) # entry field from tk class 
entry1.insert(0, "Enter your name") # add default text
entry1.bind("<Return>", return_value) # event listener 
entry1.pack(padx=10, pady=30, fill="both")

entry2 = ttk.Entry(root) # entry field from ttk class 
entry2.insert(0, "Enter your name") # add default text
entry2.bind("<Return>", return_value) # event listener 
entry2.pack(padx=10, pady=30, fill="both")

btn = tk.Button(root, text ="Get the value", command=lambda: label2.config(text=entry1.get())).pack() # button to get the value from the entry field 

# add a helper label
label2 = tk.Label(root, text="Welcome ...!")
label2.pack()

root.mainloop()