from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile,askopenfilename
import os
import pygame

#window setup
window = Tk()
window.title("Music player")
window.geometry("300x300")

#initialize the music
pygame.mixer.init()

#Function
def open_foldier():
    global file
    file = askopenfile(mode="r",filetypes=[("Music_file",'*.mp3')])
    if file:
      file_name = os.path.basename(file.name)
      Change.config(text=f"Now playing: {file_name}")

def run_music():
    global file  
    if file:
     pygame.mixer.music.load(file.name)
     pygame.mixer.music.play()
    else:
        messagebox.showerror("Error","No song selected yet!")
def pause():
    pygame.mixer.music.pause()
def unpaused():
    pygame.mixer.music.unpause()
def list_music():
    new_window = Toplevel(window)
    Label(new_window, text="Music List").pack(pady=10)

    # Create a listbox to show added songs
    listbox = Listbox(new_window, width=40, height=10)
    listbox.pack()

    songs = []
    def add_music():
       song_path = askopenfilename(mode="r",filetypes=[("Music file",'*.mp3')])
       if song_path:
          song_name = os.path.basename(song_path.name)
          listbox.insert(END,song_name)
          songs.append(song_path)
    def play_selected():
       global file
       selected = listbox.curselection()
       if selected:
          file = songs[selected[0]]
          pygame.mixer.music.load(file)
          pygame.mixer.music.play(file)
          Change.config(text=f"Now playing : {os.path.basename(file)}")
       else:
          messagebox.showwarning("Warning","No song selected")
    Button(new_window, text="Add Music", command=add_music).pack(pady=5)
    Button(new_window, text="Play Selected", command=play_selected).pack(pady=5)
    Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)


#Basic gui
frame = Frame(window)
frame.pack()
 
mainmenu = Menu(frame)
mainmenu.add_command(label = "Folder", command= open_foldier)  
mainmenu.add_command(label = "List", command=list_music)
window.config(menu = mainmenu)
Change = Label(text="Now playing: None")
Change.pack()
Button(text="play",command=run_music).pack()
Button(text="Pause",command=pause).pack()
Button(text="Continued",command=unpaused).pack()
window.mainloop()