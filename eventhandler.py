from tkinter import *

window = Tk()
window.title("Event handler")
window.geometry("300x500")
def handle_keyprees(event):
    print(event.char)
window.bind("<Key>",handle_keyprees)
def handle_click(event):
    print("The button was clicked")
button = Button(text="Click me")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()