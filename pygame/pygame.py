import tkinter as tk
from tkinter import messagebox

def start_game():
    fade_window = tk.Toplevel(window)
    fade_window.title("Fading Screen")
    fade_window.geometry("900x600")
    fade_window.configure(bg="black")
    fade_label = tk.Label(fade_window, text="Starting the game...", font=("Terminus", 32), bg="black", fg="yellow")
    fade_label.pack(expand=True)
    fade_window.attributes('-alpha', 0.0)

    def fade_in():
        alpha = fade_window.attributes('-alpha')
        if alpha < 1.0:
            alpha += 0.1
            fade_window.attributes('-alpha', alpha)
            fade_window.after(100, fade_in)
        else:
            fade_label.configure(text="Your word is: Wordo")
            fade_window.after(2000, fade_out)

    def fade_out():
        alpha = fade_window.attributes('-alpha')
        if alpha > 0.0:
            alpha -= 0.1
            fade_window.attributes('-alpha', alpha)
            fade_window.after(100, fade_out)
        else:
            fade_window.destroy()

    fade_in()

def quit_program():
    window.destroy()

window = tk.Tk()
window.title("Find Wordo")
window.geometry("900x600")
window.configure(bg="black")

title_label = tk.Label(window, text="FIND WORDO", font=("Terminus", 32), bg="black", fg="yellow")
title_label.pack(pady=80)

start_button = tk.Button(window, text="Start Game", font=("Terminus", 28), bg="black", fg="yellow", command=start_game)
start_button.pack(pady=20)

quit_button = tk.Button(window, text="Quit", font=("Terminus", 28), bg="black", fg="yellow", command=quit_program)
quit_button.pack(pady=20)

window.mainloop()
