import tkinter as tk

def selection_cng(e): 
    selection = e.widget.curselection()
    if selection: 
        index = selection[0]
    label2.config(text=f"{e.widget.get(index)} selected!", foreground=e.widget.get(index))
    
root = tk.Tk()
root.title("Adding List box")

label1 = tk.Label(root, text="What's your favorite color?").pack(padx=10, pady=20)

list_box = tk.Listbox(root)
for elm in ["blue", "red", "green", "orange", "pink", "indigo", "violet", "yellow", "black"]: 
    list_box.insert(tk.END, elm) # add values to the list box

list_box.bind("<<ListboxSelect>>", selection_cng) # event listener 
list_box.pack(padx=10, pady=30, fill="both")

label2 = tk.Label(root, text="One selected!")
label2.pack(padx=10, pady=20)

root.mainloop()