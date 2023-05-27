import tkinter as tk
from tkinter import messagebox

def start_game():
    messagebox.showinfo("Find Wordo", "Starting the game...")
  

def quit_program():
    window.destroy()


window = tk.Tk()
window.title("Find Wordo")
window.geometry("900x600")
window.configure(bg="black")


title_label = tk.Label(window, text="FIND WORDO", font=("Terminus", 16), bg="black", fg="yellow")
title_label.pack(pady=40)


start_button = tk.Button(window, text="Start Game", font=("Terminus", 14), bg="black", fg="yellow", command=start_game)
start_button.pack(pady=20)

quit_button = tk.Button(window, text="Quit", font=("Terminus", 14), bg="black", fg="yellow", command=quit_program)
quit_button.pack(pady=20)


window.mainloop()
