from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import os


window = Tk()
window.title("Rock paper scisor game")
window.geometry("400x400")
big_font = ("Arial", 15, "bold")
lb = Label(text="Welcome to rock paper scicor game",font=big_font)
lb3 = Label(text="Your saide",font=big_font)
lb4 = Label(text="computer",font=big_font) 
ent = Entry()


rock = Image.open(("rock.png")).resize((50,50))
paper = Image.open(("paper.webp")).resize((50,50))
seisor = Image.open(("sscisor.png")).resize((50,50))
rock_show = ImageTk.PhotoImage(rock)
paper_show = ImageTk.PhotoImage(paper)
seisor_show = ImageTk.PhotoImage(seisor)

def process():
    player = ent.get()
    bot = random.choice(choice)
    if player not in choice:
        messagebox.showerror("Error","Enter only rock paper scisor")
    elif player == "seisor" and bot == "paper":
        lbs.config(image=seisor_show)
        lbs2.config(image=paper_show)
        lbr.config(text="You win",font=big_font)
        logs = "win\n"
    elif player == "paper" and bot == "paper":
        lbs.config(image=paper_show)
        lbs2.config(image=paper_show)
        lbr.config(text="draw",font=big_font)
        logs = "draw\n"
    elif player == "paper" and bot == "seisor":
        lbs.config(image=paper_show)
        lbs2.config(image=seisor_show)
        lbr.config(text="You lose",font=big_font)
        logs = "lose\n"
    elif player == "rock" and bot == "rock":
        lbs.config(image=rock_show)
        lbs2.config(image=rock_show)
        lbr.config(text="draw",font=big_font)
        logs = "draw\n"
    elif player == "seisor" and bot == "seisor":
        lbs.config(image=seisor_show)
        lbs2.config(image=seisor_show)
        lbr.config(text="draw",font=big_font)
        logs = "draw\n"
    elif player == "seisor" and bot == "rock":
        lbs.config(image=seisor_show)
        lbs2.config(image=rock_show)
        lbr.config(text="You lose",font=big_font)
        logs = "lose\n"
    elif player == "rock" and bot == "paper":
        lbs.config(image=rock_show)
        lbs2.config(image=paper_show)
        lbr.config(text="You lose",font=big_font)
        logs = "lose\n"
    elif player == "paper" and bot == "rock":
        lbs.config(image=paper_show)
        lbs2.config(image=rock_show)
        lbr.config(text="You win",font=big_font)
        logs = "win\n"
    elif player == "rock" and bot == "seisor":
        lbs.config(image=rock_show)
        lbs2.config(image=seisor_show)
        lbr.config(text="You win",font=big_font)
        logs = "win\n"
    else:
        messagebox.showerror("Error","system error")
    with open("game_log.txt", "a") as f:
        f.write(f"Player: {player} | Computer: {bot} | Result: {logs}\n")

def show_log():
    if not os.path.exists("game_log.txt"):
        messagebox.showinfo("Game Log", "No games played yet!")
        return
    with open("game_log.txt", "r") as f:
        logs = f.read()
btn = Button(text="Play",command=process)
btn2 = Button(text="Show log",command=show_log)

lbs = Label()
lbs2 = Label()
lbr = Label()
choice = ["rock","paper","seisor"]
lb.pack()
ent.pack()
btn.pack()
btn2.pack()
lb3.place(x=53,y=155)
lbs.place(x=90,y=230)
lbr.place(x=197,y=237)
lbs2.place(x=301,y=244)
lb4.place(x=302,y=142)
window.mainloop()