import tkinter as tk
import random

def play_game(player_choice):
    # Generate the computer's choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif player_choice == 'rock':
        if computer_choice == 'paper':
            result = "You lose! Paper beats rock."
        else:
            result = "You win! Rock beats scissors."
    elif player_choice == 'paper':
        if computer_choice == 'scissors':
            result = "You lose! Scissors beats paper."
        else:
            result = "You win! Paper beats rock."
    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            result = "You lose! Rock beats scissors."
        else:
            result = "You win! Scissors beats paper."
    else:
        result = "Invalid choice. Please choose either 'rock', 'paper', or 'scissors'."
    
    # Update the result label
    result_label.config(text=result)

def play_button_click():
    player_choice = choice_var.get()
    play_game(player_choice)

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create the choice label
choice_label = tk.Label(window, text="Choose your move:")
choice_label.pack()

# Create the choice radio buttons
choice_var = tk.StringVar()
rock_button = tk.Radiobutton(window, text="Rock", variable=choice_var, value="rock")
paper_button = tk.Radiobutton(window, text="Paper", variable=choice_var, value="paper")
scissors_button = tk.Radiobutton(window, text="Scissors", variable=choice_var, value="scissors")

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create the play button
play_button = tk.Button(window, text="Play", command=play_button_click)
play_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Create the instructions label
instructions_label = tk.Label(window, text="Make your selection and click 'Play'.")
instructions_label.pack()

# Start the main event loop
window.mainloop()
