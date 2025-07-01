import tkinter as tk

root = tk.Tk() # main window
root.title("Tkinter Spinbox")

label1 = tk.Label(root, text="What's your age?").pack(padx=10, pady=20, fill="both")

spn_var = tk.StringVar(value="0")
spin_box = tk.Spinbox(root, from_=4, to=180, textvariable=spn_var) # creates a spin box from value 4 to 180 from tk class
spin_box.pack(padx=15, pady=30, fill="y")

label2 = tk.Label(root, textvariable=spn_var)
label2.pack(expand=True)

root.mainloop()