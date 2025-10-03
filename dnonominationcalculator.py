from tkinter import  *
from tkinter import messagebox
from PIL import Image,ImageTk
def open_calculator():
    welcome_win.destroy()
    root = Tk()
    root.title("Denomination calculator")
    root.geometry("400x400")
    root.configure(bg='light grey')
    def calculate():
        try:
            amount = int(Entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("Error","Please a valid number")
    def reset():
        Entry.delete(0,END)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
    def exit_app():
        root.destroy()
    Label(root,text="Enter total amount",bg='light grey',font=('arial',11)).place(x=120,y=30)
    entry = Entry(root)
    entry.place(x=120,y=60)
    Label(root,text="$2000 note",bg='light grey').place(x=50,y=110)
    Label(root,text="$500 note",bg='light grey').place(x=50,y=140)
    Label(root,text="$100 note",bg='light grey').place(x=50,y=170)
    t1 = Entry(root)
    t1.place(x=150,y=110)
    t2 = Entry(root)
    t2.place(x=150,y=140)
    t3 = Entry(root)
    t3.place(x=150,y=170)
    Button(root,text="Calculate",command=calculate,bg='brown',fg='white').place(x=50,y=230)
    Button(root,text="reset",command=reset,bg='orange',fg='white').place(x=150,y=230)
    Button(root,text="exit",command=exit_app,bg='red',fg='white').place(x=250,y=230)
    root.mainloop()
welcome_win = Tk()
welcome_win.title("WELCOME")
welcome_win.geometry("400x400")
welcome_win.configure(bg='white')
try:
    img = Image.open("background2.jpg")
    img = img.resize((300,200))
    welcome_photo = ImageTk.PhotoImage(img)
    Label(welcome_win,image=welcome_photo,bg='white').pack(pady=30)
except:
    Label(welcome_win,text="Welcome to denomination calculator",font=('arial',14),bg="white",fg="black").pack(pady=80)
Button(welcome_win,text="Let's get started",command=open_calculator,font=('arial',12),bg="green",fg="white").pack(pady=20)
welcome_win.mainloop()


