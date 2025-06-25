from tkinter import *

root = Tk()
root.title("Tkinter first program") # set title 
root.config(background="#0072f6") # set background color
root.geometry("600x1000+30-60") # set window size to 400x500 and window position will be 30 pixel left from the screen and 60 pixel up from the bottom 
root.resizable(False, True) # window won't be resizable to the x axis and resizable to the y axis 
# setting max and min resizable size
root.minsize(150, 100) # minimum 150 pixel width and 100 pixel height 
root.maxsize(900, 1500) # maximum 900 pixel width and 1500 pixel height 
# setting alpha (transparency )
root.attributes('-alpha',0.9) # alpha=0.9
root.attributes('-topmost', 1) # window appears to the top
root.attributes("-fullscreen", False) # sets if the window will be Fullscreen 

# setting icon of the window 
#root.iconbitmap("./assets/app_icon.ico")
icon = PhotoImage(file="assets/app_icon.png")
root.iconphoto(True, icon) # set icon

root.config(cursor="hand2") # changes mouse pointer 

root.mainloop()