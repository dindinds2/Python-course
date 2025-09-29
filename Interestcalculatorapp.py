from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("Interest calculator app")
lb = Label(text="Welcome to text calculator app")
lb2 = Label(text="Enter the Principal")
ent = Entry()
lb3 = Label(text="enter the Rate of Interest")
ent2 = Entry()
lb4 = Label(text="Enter the Time")
ent3 = Entry()
def simple():
    try:
        principal = float(ent.get())
        ROI = float(ent2.get())
        time = float(ent3.get())
        result1 = (principal * ROI * time) / 100
        lb5.config(text=f"Simple Interest = {result1:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Only numbers are allowed")
def compound():
    try:
        principal = float(ent.get())
        ROI = float(ent2.get())
        time = float(ent3.get())
        amount = principal * (1 + ROI/100) ** time
        result2 = amount - principal
        lb5.config(text=f"Compound Interest = {result2:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Only numbers are allowed")
btn1 = Button(text="Simple Interest", command=simple)
btn2 = Button(text="Compound Interest", command=compound)
lb5 = Label()
lb.pack()
lb2.pack()
ent.pack()
lb3.pack()
ent2.pack()
lb4.pack()
ent3.pack()
btn1.pack(pady=5)
btn2.pack(pady=5)
lb5.pack()


window.mainloop()