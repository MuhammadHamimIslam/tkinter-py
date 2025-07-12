import tkinter as tk

root = tk.Tk()
root.title("Tkinter pack function")

label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="green")
label3 = tk.Label(root, text="Label 3", bg="blue")

# tkinter pack's side parameter : The side parameter determines the direction of the widgets in the layout
# side has 4 values -> TOP, BOTTOM, RIGJT, LEFT
# fill parameter
label1.pack(side=tk.BOTTOM, fill=tk.X, ipadx=10, ipady=20, padx=10, pady=15) # side set to Bottom, default is Top
label2.pack(side=tk.BOTTOM, fill=tk.Y, ipadx=10, ipady=15, padx=10, pady=15, anchor="ne") # fills the Y axis and position will be top right
label3.pack(side=tk.BOTTOM, fill=tk.BOTH, ipadx=15, ipady=15, padx=10, pady=15) # internal padding x, padding y set to 15, 15 and external padding x, y set to 10, 15

root.mainloop()