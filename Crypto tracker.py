import requests
from tkinter import *
from tkinter import ttk, messagebox
window = Tk()
window.title("Crypto Tracker")
window.geometry("300x300")

Main_fonts = ("arial", 12, "bold")
base_url = "https://api.coingecko.com/api/v3/"

Label(text="Welcome to Crypto Tracker", font=Main_fonts).pack()
Label(text="Enter the crypto name:").pack()

frame = Frame(window)
frame.pack()

vlist = ["USD", "THB", "GBP"]
Combo = ttk.Combobox(frame, values=vlist)
Combo.set("Pick a currency")
Combo.pack()

ent = Entry()
ent.pack()

lb1 = Label(text="", font=("arial", 11))
lb1.pack(pady=10)

def get_price():
    Bitcoil = ["bitcoin", "ethereum", "dogecoin"]
    user = ent.get().lower()
    currency = Combo.get().lower()

    if user not in Bitcoil:
        messagebox.showerror("Error", "Enter a valid coin (bitcoin, ethereum, dogecoin)")
        return
    
    url = f"{base_url}simple/price?ids={user}&vs_currencies={currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data[user][currency]
        lb1.config(text=f"{user.capitalize()} price: {price} {currency.upper()}")
    else:
        messagebox.showerror("Error", "Failed to fetch data. Try again later.")

Button(text="Check price", command=get_price).pack(pady=5)

window.mainloop()
