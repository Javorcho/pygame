import tkinter as tk
from tkinter import messagebox
from wordgenerator import generate_random_word

DIFFICULTIES = {
    "Easy": 20,
    "Medium": 50,
    "Hard": 100
}

target_word = ""

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

def fade_out():
    for i in range(10, -1, -1):
        fade_label.configure(bg=f"#{i*2:02x}{i*2:02x}00", fg="black" if i <= 5 else "yellow")
        fade_label.update()
        fade_label.after(200)

    fade_label.configure(text="")
    fade_label.update()
    show_difficulty_menu()

def show_instructions():
    instructions = "Welcome to Find Wordo!\n\n"
    instructions += "The objective of the game is to find the word you were given.\n"
    instructions += "First click the start button.\n"
    instructions += "After that, a random word will be generated.\n"
    instructions += "Then your screen will fill with words and you will have to find the one you were given.\n"
    instructions += "There are 3 levels of difficulty:"
    instructions += "Easy = 20 words"
    instructions += "Medium = 50 words"
    instructions += "Hard = 100 words"
    instructions += "Have fun and enjoy playing Find Wordo!\n"
    instructions += "If you want to add or remove words, you must go to the wordgenerator file and modify the word list."

    messagebox.showinfo("Instructions", instructions)

def show_difficulty_menu():
    
    start_button.pack_forget()
    instructions_button.pack_forget()

   
    difficulty_label = tk.Label(window, text="Select Difficulty:", font=("Terminus", 28), bg="black", fg="yellow")
    difficulty_label.pack(pady=60)

    
    for difficulty, num_words in DIFFICULTIES.items():
        button = tk.Button(window, text=difficulty, font=("Terminus", 24), bg="black", fg="yellow",
                           command=lambda n=num_words: start_game(n))
        button.pack(pady=10)

def start_game(num_words):
    difficulty_label.pack_forget() 
    title_label.pack_forget()
    for button in difficulty_buttons:  
        button.pack_forget()

    word_list = generate_word_list(num_words)
    target_word = generate_random_word()
    fade_label.configure(text=f"Find: {target_word}")
    fade_label.update()
    fade_label.after(2000, lambda: fill_screen_with_words(word_list))
    fade_label.configure(bg="black", fg="black")  

def show_difficulty_menu():
    start_button.pack_forget()
    instructions_button.pack_forget()

    global difficulty_label, difficulty_buttons
    difficulty_label = tk.Label(window, text="Select Difficulty:", font=("Terminus", 28), bg="black", fg="yellow")
    difficulty_label.pack(pady=60)

    difficulty_buttons = []
    for difficulty, num_words in DIFFICULTIES.items():
        button = tk.Button(window, text=difficulty, font=("Terminus", 24), bg="black", fg="yellow",
                           command=lambda n=num_words: start_game(n))
        button.pack(pady=10)
        difficulty_buttons.append(button)

def generate_word_list(num_words):
    word_list = [generate_random_word() for _ in range(num_words)]
    return word_list

def fill_screen_with_words(word_list):
    window.configure(bg="black")

    for label in word_labels:
        label.destroy()
    word_labels.clear()

    for i, word in enumerate(word_list):
        label = tk.Label(window, text=word, font=("Terminus", 16), bg="black", fg="white")
        label.place(relx=(i % 10) * 0.1, rely=(i // 10) * 0.1)
        label.bind("<Button-1>", word_clicked)
        word_labels.append(label)

def word_clicked(event):
    clicked_word = event.widget.cget("text")
    if clicked_word == target_word:
        messagebox.showinfo("Congratulations!", "You found the word!")
    else:
        print("Clicked word:", clicked_word)

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

word_labels = []  

window.mainloop()
