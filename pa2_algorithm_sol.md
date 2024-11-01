### Algorithm for the Game of Sticks Program

1. Output a welcome message explaining the purpose and rules of the game.

1. Initialize variables:
    - `player1_losses = 0` (tracks Player 1's losses)
    - `player2_losses = 0` (tracks Player 2's losses)
    - `computer_losses = 0` (tracks Computer's losses)
    - `play_again = 'y'` (to control replay loop)

1. Start a while loop that continues as long as `play_again` is 'y':
    1. Prompt the user to input the number of sticks to start with (between 10 and 100).
    1. While the input is not a digit or not between 10 and 100:
        1. Output an error message 
        1. Prompt the user to input the number of sticks to start with (between 10 and 100).
    1. Store the valid input on to the `sticks` variable.
    1. Create `current_player` variable and set the current player to 1

    1. As long as (or While) `sticks > 0`:
        1. Display the current number of sticks on the table.
        
        1. If `current_player` is 1:
            1. Output "Player 1's turn."
            1. Prompt the user to enter the number of sticks to take (1-3).
            1. While the input is not a digit or not between 1 and 3:
                1. Output an error message 
                1. Prompt the user to enter the number of sticks to take (1-3).
            1. Store the valid input on to the `take` variable.
        1. Otherwise, if `current_player` is 2:
            1. Output "Player 2's turn."
            1. Prompt the user to enter the number of sticks to take (1-3).
            1. While the input is not a digit or not between 1 and 3:
                1. Output an error message
                1. Prompt the user to enter the number of sticks to take (1-3).
            1. Store the valid input on to the `take` variable.
        1. Otherwise (Computer's turn):
            1. Generate a random integer between 1 and 3 for `take`.
            1. Output the number of sticks the computer takes.
        1. Subtract `take` from `sticks` to update the number of sticks remaining.

        1. If `sticks` is less than or equal to 0:
            1. Output "Player X loses!" (where X is the `current_player`).
            1. If `current_player` is 1:
                1. Increment `player1_losses` by one
            1. Otherwise, if `current_player` is 2:
                1. Increment `player2_losses` by one
            1. Otherwise (Computer's turn):
                1. Increment `computer_losses` by one
            
        1. Update `current_player` to the next one in the sequence: `(current_player % 3) + 1`.

        1. Prompt the user to input if they want to play again (y/n):
            - Assign the resul to `play_again`
       
1. Display the total number of losses for Player 1, Player 2, and the Computer.

1. Output a message thanking the user and indicating the program has ended.