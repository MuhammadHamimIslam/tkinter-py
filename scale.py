import tkinter as tk
from tkinter import ttk

def value_cng(e):
    label2.config(text=f"Your age is {e.widget.get()}")

def increment(): 
    "Increment the scale value by 5"
    current = scale_tk.get()
    set_value = min(current + 5, scale_tk["to"])
    scale_tk.set(set_value)

def decrement(): 
    "Decrement the scale value by 5"
    current = scale_tk.get()
    set_value = max(current - 5, scale_tk["from"])
    scale_tk.set(set_value)    

root = tk.Tk()
root.title("Tkinter scale")


label1 = tk.Label(root, text="What's your age?").pack(padx=10, pady=20)


# adding scale (same as html input type range)
scale_tk = tk.Scale(root, from_=4, to=150, orient="horizontal") # adds a horizontal scale from tk class 
scale_tk.bind("<Motion>", value_cng)
scale_tk.pack(padx=15, pady=30, fill="both")


scale_ttk = ttk.Scale(root, from_=4, to=150, orient="horizontal") # adds a horizontal scale from ttk class 
scale_ttk.bind("<B1-Motion>", value_cng)
scale_ttk.pack(padx=15, pady=30, fill="both")

# increment and decrement button 
btn_decrement = ttk.Button(root, text="-", command=decrement).pack(padx=10, pady=15)
btn_increment = ttk.Button(root, text="+", command=increment).pack(padx=10, pady=20)

# adding helper label
label2 = tk.Label(root, text="Your age is ...")
label2.pack(padx=10, pady=20)

root.mainloop()
