import tkinter as tk
from tkinter import messagebox
from wordgenerator import generate_random_word

def fade_in():
    fade_label.configure(text="Starting the game...")
    fade_label.update()

    for i in range(0, 11):
        fade_label.configure(bg=f"#{i*2:02x}{i*2:02x}00", fg="black" if i <= 5 else "yellow")
        fade_label.update()
        fade_label.after(200)

    word = generate_random_word()
    fade_label.configure(text=f"Your word is: {word}")
    fade_label.update()
    fade_label.after(2000, fade_out)

    word = generate_random_word()
    fade_label.configure(text=f"Your word is: {word}")
    fade_label.update()
    fade_label.after(2000, fade_out)

def fade_out():
    for i in range(10, -1, -1):
        fade_label.configure(bg=f"#{i*2:02x}{i*2:02x}00", fg="black" if i <= 5 else "yellow")
        fade_label.update()
        fade_label.after(200)

    fade_label.configure(text="")
    fade_label.update()

def show_instructions():
    instructions = "Welcome to Find Wordo!\n\n"
    instructions += "The objective of the game is to find the word you were given.\n"
    instructions += "The time you need to find the word will be recorded and displayed in the highscore menus"
    instructions += "First click the start button.\n"
    instructions += "After that a ranom word will be generated.\n"
    instructions += "Then your screen will fill with words and you will have to find the one you were given.\n"
    instructions += "Have fun and enjoy playing Find Wordo!"
    instructions += "If you want to add or remove words you must go to the wordgenerator file and there you can add or remove words"

    messagebox.showinfo("Instructions", instructions)

def quit_program():
    window.destroy()

window = tk.Tk()
window.title("Find Wordo")
window.geometry("900x600")
window.configure(bg="black")

title_label = tk.Label(window, text="FIND WORDO", font=("Terminus", 32), bg="black", fg="yellow")
title_label.pack(pady=80)

start_button = tk.Button(window, text="Start Game", font=("Terminus", 28), bg="black", fg="yellow", command=fade_in)
start_button.pack(pady=20)

instructions_button = tk.Button(window, text="Instructions", font=("Terminus", 28), bg="black", fg="yellow", command=show_instructions)
instructions_button.pack(pady=20)

quit_button = tk.Button(window, text="Quit", font=("Terminus", 28), bg="black", fg="yellow", command=quit_program)
quit_button.pack(pady=20)

fade_label = tk.Label(window, text="", font=("Terminus", 32), bg="black", fg="yellow")
fade_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

window.mainloop()
