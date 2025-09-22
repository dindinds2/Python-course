from tkinter import *
from datetime import date

root = Tk()
root.title("Getting start with wiget")
root.geometry("500x500")
lbl = Label(text="Hello",fg="white",bg="black",height=1,width=300)
name_lbl = Label(text="Full name",bg="black")
name_entry = Entry()
def display():
    name = name_entry.get()
    global Message
    Message = "Welcome to the application \n today date is"
    greet = "Hello" + name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date.today())
text_box = Text(height=3)
btn = Button(text="Begin",command=display,height=1,bg="blue",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()