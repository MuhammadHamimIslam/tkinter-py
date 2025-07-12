import tkinter as tk

root = tk.Tk()
root.title("Tkinter grid layout")

label1 = tk.Label(root, text="Label 1", bg="#FF0000")
label2 = tk.Label(root, text="Label 2", bg="#00FF00")
label3 = tk.Label(root, text="Label 3", bg="#0000FF")
label4 = tk.Label(root, text="Label 4", bg="#FF00FF")

# grid follows the row, column value
label1.grid(column=0, row=0, padx=15, pady=10)
label2.grid(column=1, row=0, padx=15, pady=10)
label3.grid(column=2, row=0, padx=15, pady=10)
label4.grid(column=3, row=0, padx=15, pady=10)

root.mainloop()