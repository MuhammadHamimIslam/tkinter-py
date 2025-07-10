import tkinter as tk
from tkinter import ttk

i = 0

def clicked(e):
    global i
    i += 1
    label.config(text=f"Button is clicked: {i}")

root = tk.Tk()
root.config(bg="lightblue")
root.geometry("500x300")
root.title('Tkinter event binding')

# addind event binding to a widget
# widget.bind(event, handler, add=None)
btn = ttk.Button(root, text="Click")
btn.pack()
btn.bind("<Button-1>", clicked) # event listener : clicked function will be called when the event will be fired
btn.bind("<Return>", clicked) # multiple event can be added
btn.unbind("<Return>") # removing an event

label = tk.Label(root, text="")
label.pack()

root.mainloop()