import tkinter as tk
from tkinter import messagebox
from wordgenerator import generate_random_word
import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# Set colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Find Wordo")

# Create the font
font = pygame.font.Font(None, 32)

# Game states
STATE_MENU = 0
STATE_GAME = 1

# Current game state
current_state = STATE_MENU

def fade_in():
    fade_label.set_text("Starting the game...")
    fade_label.update()

    for i in range(0, 11):
        fade_label.set_color((i * 2, i * 2, 0))
        fade_label.update()
        pygame.time.wait(200)

    word = generate_random_word()
    fade_label.set_text(f"Your word is: {word}")
    fade_label.update()
    pygame.time.wait(2000)
    fade_out()

def fade_out():
    for i in range(10, -1, -1):
        fade_label.set_color((i * 2, i * 2, 0))
        fade_label.update()
        pygame.time.wait(200)

    fade_label.set_text("")
    fade_label.update()

def show_instructions():
    instructions = "Welcome to Find Wordo!\n\n"
    instructions += "The objective of the game is to find the word you were given.\n"
    instructions += "The time you need to find the word will be recorded and displayed in the highscore menus.\n"
    instructions += "First click the Start button.\n"
    instructions += "After that, a random word will be generated.\n"
    instructions += "Then, your screen will fill with words and you will have to find the one you were given.\n"
    instructions += "Have fun and enjoy playing Find Wordo!\n"
    instructions += "If you want to add or remove words, you must go to the wordgenerator file and make changes."

    messagebox.showinfo("Instructions", instructions)

def quit_program():
    pygame.quit()

# Create the title label
title_label = font.render("FIND WORDO", True, YELLOW)

# Create the start button
start_button = pygame.Rect(350, 250, 200, 50)
start_text = font.render("Start Game", True, YELLOW)

# Create the instructions button
instructions_button = pygame.Rect(325, 320, 250, 50)
instructions_text = font.render("Instructions", True, YELLOW)

# Create the quit button
quit_button = pygame.Rect(375, 390, 150, 50)
quit_text = font.render("Quit", True, YELLOW)

# Create the fade label
fade_label = pygame.sprite.Sprite()
fade_label.image = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
fade_label.rect = fade_label.image.get_rect()
fade_label.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Create the sprite group
sprites = pygame.sprite.Group(fade_label)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == STATE_MENU:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    current_state = STATE_GAME
                    fade_in()
                elif instructions_button.collidepoint(mouse_pos):
                    show_instructions()
                elif quit_button.collidepoint(mouse_pos):
                    running = False

    # Clear the window
    window.fill(BLACK)

    if current_state == STATE_MENU:
        # Draw the menu elements
        window.blit(title_label, (350, 200))
        pygame.draw.rect(window, YELLOW, start_button)
        window.blit(start_text, (start_button.x + 30, start_button.y + 10))
        pygame.draw.rect(window, YELLOW, instructions_button)
        window.blit(instructions_text, (instructions_button.x + 30, instructions_button.y + 10))
        pygame.draw.rect(window, YELLOW, quit_button)
        window.blit(quit_text, (quit_button.x + 60, quit_button.y + 10))
    elif current_state == STATE_GAME:
        # Draw the game elements
        sprites.draw(window)

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()
