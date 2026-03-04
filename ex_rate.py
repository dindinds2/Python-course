import requests
from tkinter import *
from tkinter import ttk,messagebox

#ใช้ API
api = "https://v6.exchangerate-api.com/v6/c2fb688dd237e4fec0df05ea/latest/"
#เตรียมหน้าจอ ui
window = Tk()
window.geometry("300x300")
window.title("Money exchange rate")
window.configure(bg="black")

frame = Frame(window)
frame.pack()

currency = ["USD","EUR","GBP","CNY","JPY","THB"]
Combo = ttk.Combobox(frame, values=currency)
Combo.set("Pick a currency")
Combo.pack()
ent = Entry()

Combo2= ttk.Combobox(frame, values=currency)
Combo2.set("Pick a currency to convert")
Combo2.pack()
#function ตรวจสอบเงื่อนใข่
def convet_currency():
    base = Combo.get()
    traget = Combo2.get()
    amounth = ent.get()
    if base not in currency or traget not in currency:
        messagebox.showerror("ERROR!","Please chose the both currency!")
        return
    try:
        amounth = float(amounth)
    except:
        messagebox.showerror("Error","Enter the valid number")
        return
    #Check API
    url = api+base
    res = requests.get(url).json()
    if "convertion_rates" not in res:
        messagebox.showerror("Error","API error check your internet")
        return
    rate = res["convertion_rates"][traget]
    resulth = amounth * rate
    Lb.config(f"{amounth} {base} = {resulth:.2f} {traget}")

Lb = Label()
ent.pack()
Button(window, text="Convert", command=convet_currency).pack(pady=15)
Lb.pack(padx=5)
window.mainloop()