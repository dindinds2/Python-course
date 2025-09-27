from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus dectected")
root.geometry("500x500")
def msg():
    messagebox.showwarning("Alert! Stop virus found")
button = Button(root,text="Scan for virus",command=msg)
button.place(x=40,y=80)
root.mainloop()