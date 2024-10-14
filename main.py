import random


def get_valid_stick_input(player_name):
    while True:
        try:
            sticks = int(input(f"{player_name}, how many sticks do you want to take (1, 2, or 3)? "))
            if sticks in [1, 2, 3]:
                return sticks
            else:
                print("Invalid input. You can only take 1, 2, or 3 sticks.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_initial_sticks():
    while True:
        try:
            total_sticks = int(input("Enter the number of sticks to start with (between 10 and 100): "))
            if 10 <= total_sticks <= 100:
                return total_sticks
            else:
                print("Invalid input. Please enter a number between 10 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_move():
    return random.choice([1, 2, 3])


def play_game():
    # Losses count for each player
    losses = {"Player 1": 0, "Player 2": 0, "Computer": 0}

    while True:
        total_sticks = get_initial_sticks()
        current_player = "Player 1"

        while total_sticks > 0:
            print(f"\nSticks remaining: {total_sticks}")

            if current_player == "Player 1" or current_player == "Player 2":
                sticks_taken = get_valid_stick_input(current_player)
            else:
                sticks_taken = computer_move()
                print(f"The computer takes {sticks_taken} sticks.")

            total_sticks -= sticks_taken

            if total_sticks <= 0:
                print(f"\n{current_player} took the last stick and loses!")
                losses[current_player] += 1
                break

            # Switch to the next player
            if current_player == "Player 1":
                current_player = "Player 2"
            elif current_player == "Player 2":
                current_player = "Computer"
            else:
                current_player = "Player 1"

        # After the game ends, ask if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    # Final report of losses
    print("\nGame Over! Here are the final loss counts:")
    for player, count in losses.items():
        print(f"{player}: {count} losses")


# Start the game
play_game()
