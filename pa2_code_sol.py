# Programmers:  [your name here]
# Course:  CS151, [Instructors name here]
# Due Date: [date assignment is due]
# Programming Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program

import random

# Introduction about the game
print('-' * 73)
print("| \tWelcome to the Game of Sticks!\t\t\t\t\t|")
print("| \tIn this game, there is a pile of sticks on the table, \t\t|")
print("|\tand players take turns picking 1-3 sticks.\t\t\t|")
print("| \tThe player who takes the last stick loses.\t\t\t|")
print('-' * 73)
print()

# Initialize variables for losses
player1_losses = 0
player2_losses = 0
computer_losses = 0

# Main game loop to allow replay
play_again = 'y'
while play_again == 'y':
    # Ask the user to choose the number of sticks (between 10 and 100)
    sticks = input("Enter the number of sticks to start with (between 10 and 100): ")
    while not sticks.isdigit() or not (10 <= int(sticks) <= 100):
        print("Invalid input. Please enter a valid number between 10 and 100.")
        sticks = input("Enter the number of sticks to start with (between 10 and 100): ")
    sticks = int(sticks)

    # Game loop
    current_player = 1  # Start with player 1
    while sticks > 0:
        # Display the current number of sticks
        print(f"\nThere are {sticks} sticks on the table.")
        
        # Determine the player's turn
        if current_player == 1:
            print("Player 1's turn.")
            take_input = input("Enter the number of sticks to take (1-3): ")
            
            # Check if the input is a digit and is between 1 and 3
            while not (take_input.isdigit() and 1 <= int(take_input) <= 3):
                print("Invalid input. You must take 1, 2, or 3 sticks.")
                take_input = input("Enter the number of sticks to take (1-3): ")
            take = int(take_input)

        elif current_player == 2:
            print("Player 2's turn.")
            take_input = input("Enter the number of sticks to take (1-3): ")
            
            # Check if the input is a digit and is between 1 and 3
            while not (take_input.isdigit() and 1 <= int(take_input) <= 3):
                print("Invalid input. You must take 1, 2, or 3 sticks.")
                take_input = input("Enter the number of sticks to take (1-3): ")
            take = int(take_input)

        else:
            # Computer's turn
            take = random.randint(1, 3)
            print(f"The computer takes {take} sticks.")

        # Update the number of sticks
        sticks -= take

        # Check if the game has ended
        if sticks <= 0:
            print(f"\nPlayer {current_player} loses!")
            if current_player == 1:
                player1_losses += 1
            elif current_player == 2:
                player2_losses += 1
            else:
                computer_losses += 1

        # Switch to the next player
        current_player = (current_player % 3) + 1

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower().strip()

print('\n')
# Display total losses
print('-' * 43)
print("| Total losses:                           |")
print(f"|     Player 1: {player1_losses} losses                  |")
print(f"|     Player 2: {player2_losses} losses                  |")
print(f"|     Computer: {computer_losses} losses                  |")
print("| Thank you for playing!                  |")
print('-' * 43)