from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Lenght convertor app")
window.geometry("500x500")
lbl = Label(text="Welcome to lenght convertor app")
lb = Label(text="Enter lenght(inc)")
ent = Entry()
def con():
    try:
     num = float(ent.get())
     result = num * 2.54
     messagebox.showinfo("Result",f"{result}cm")
    except ValueError:
       messagebox.showerror("Error","Enter the number")
btn = Button(text="Convert",command=con)
lbl.pack()
lb.pack()
ent.pack()
btn.pack()
window.mainloop()