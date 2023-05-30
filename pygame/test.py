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

    fade_label.configure(text="")
    fade_label.update()

    show_difficulty_menu()  # Show the difficulty menu after the word menu disappears

def show_instructions():
    instructions = "Welcome to Find Wordo!\n\n"
    instructions += "The objective of the game is to find the word you were given.\n"
    instructions += "The time you need to find the word will be recorded and displayed in the highscore menus.\n"
    instructions += "First, click the start button.\n"
    instructions += "After that, a random word will be generated.\n"
    instructions += "Then, your screen will fill with words and you will have to find the one you were given.\n"
    instructions += "Have fun and enjoy playing Find Wordo!\n"
    instructions += "If you want to add or remove words, you must go to the wordgenerator file where you can modify the word list."

    messagebox.showinfo("Instructions", instructions)

def show_difficulty_menu():
    # Hide the start button and instructions button
    start_button.pack_forget()
    instructions_button.pack_forget()

    # Create a new label for the difficulty menu
    difficulty_label = tk.Label(window, text="Select Difficulty:", font=("Terminus", 28), bg="black", fg="yellow")
    difficulty_label.pack(pady=80)

    # Create buttons for each difficulty level
    easy_button = tk.Button(window, text="Easy", font=("Terminus", 24), bg="black", fg="yellow", command=start_game_easy)
    easy_button.pack(pady=20)

    medium_button = tk.Button(window, text="Medium", font=("Terminus", 24), bg="black", fg="yellow", command=start_game_medium)
    medium_button.pack(pady=20)

    hard_button = tk.Button(window, text="Hard", font=("Terminus", 24), bg="black", fg="yellow", command=start_game_hard)
    hard_button.pack(pady=20)

    extreme_button = tk.Button(window, text="Extreme", font=("Terminus", 24), bg="black", fg="yellow", command=start_game_extreme)
    extreme_button.pack(pady=20)

    monster_button = tk.Button(window, text="Monster", font=("Terminus", 24), bg="black", fg="yellow", command=start_game_monster)
    monster_button.pack(pady=20)

def generate_word_list(num_words):
    word_list = [generate_random_word() for _ in range(num_words)]
    return word_list

def fill_screen_with_words(word_list):
    # Set the background color of the window to black
    window.configure(bg="black")

    # Clear the previous labels
    for label in word_labels:
        label.destroy()
    word_labels.clear()

    # Create labels for each word and place them on the screen
    for i, word in enumerate(word_list):
        label = tk.Label(window, text=word, font=("Terminus", 16), bg="black", fg="white")
        label.place(relx=(i % 10) * 0.1, rely=(i // 10) * 0.1)
        label.bind("<Button-1>", word_clicked)  # Bind the click event to the label
        word_labels.append(label)

def word_clicked(event):
    clicked_word = event.widget.cget("text")
    print("Clicked word:", clicked_word)  # Replace with your logic for handling the clicked word

def start_game_easy():
    num_words = 20
    word_list = generate_word_list(num_words)
    fill_screen_with_words(word_list)

def start_game_medium():
    num_words = 50
    word_list = generate_word_list(num_words)
    fill_screen_with_words(word_list)

def start_game_hard():
    num_words = 100
    word_list = generate_word_list(num_words)
    fill_screen_with_words(word_list)

def start_game_extreme():
    num_words = 200
    word_list = generate_word_list(num_words)
    fill_screen_with_words(word_list)

def start_game_monster():
    num_words = 1000
    word_list = generate_word_list(num_words)
    fill_screen_with_words(word_list)

def quit_program():
    window.destroy()

window = tk.Tk()
window.title("Find Wordo")
window.geometry("900x600")  # Set the initial size of the window
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

word_labels = []  # Store the labels for the words on the screen

window.mainloop()
