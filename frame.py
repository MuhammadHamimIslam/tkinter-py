import tkinter as tk

root = tk.Tk()
root.title("Tkinter Frame")
root.config(bg="skyblue")

# adding frame (html <div> tag)
frame1 = tk.Frame(root, width=200, height=200) # adds a frame 
frame1.pack(padx=10, pady=20)


root.mainloop()