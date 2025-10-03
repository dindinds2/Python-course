from tkinter import *

window = Tk()
window.title("Password strangth test")
window.geometry("400x400")
lb = Label(text="hello enter the password")
lb2 = Label(text="Enter the password")
ent = Entry()
fram = Frame(master=window,bg="white",width=30,height=30)
def check():
    pas = ent.get()
    length = len(pas)
    if length > 8:
        fram.config(bg="green")
        lb3.config(text="Strong")
    elif length == 5:
        fram.config(bg="yellow")
        lb3.config(text="Medium")
    else:
        fram.config(bg="red")
        lb3.config(text="week")
btn = Button(text="Check",command=check)
lb3 = Label()
lb.pack(pady = 5)
lb2.pack(pady = 5)
ent.pack(pady = 5)
btn.pack(pady = 5)
fram.place(x=260,y=55)
lb3.pack()
window.mainloop()