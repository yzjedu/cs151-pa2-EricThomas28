### Exact Algorithm:

1. **Initialize the Game**:
   - Initialize a dictionary `losses` to track the number of times each player loses:
     - `losses["Player 1"] = 0`
     - `losses["Player 2"] = 0`
     - `losses["Player 3 (Computer)"] = 0`

2. **Game Loop** (repeat for each game):
   1. **Get the Initial Number of Sticks**:
      - Ask the user to input a valid number of sticks (between 10 and 100).
      - Ensure input is a valid integer. If not, re-prompt until a valid number is entered.
   
   2. **Set Initial Player**:
      - Set `current_player = "Player 1"`, indicating that Player 1 goes first.

   3. **Play Until the Game Ends** (while sticks are greater than 0):
      - Display the remaining number of sticks.

      4. **Player Turn**:
         - **For Player 1 or Player 2**:
           - Ask the current player how many sticks they want to take (1, 2, or 3).
           - Validate input. If invalid, re-prompt until valid (i.e., must be an integer and must be 1, 2, or 3).
         - **For Player 3 (Computer)**:
           - The computer randomly selects 1, 2, or 3 sticks.
           - Display how many sticks the computer took.

      5. **Update Total Sticks**:
         - Subtract the number of sticks taken from the total sticks.

      6. **Check for End of Game**:
         - If the number of remaining sticks is 0 or less:
           - The `current_player` loses the game (since they took the last stick).
           - Update the `losses[current_player] += 1` to increment their loss count.
           - Exit the current game loop (i.e., move to step 7).

      7. **Switch Players** (if the game is still ongoing):
         - If `current_player` is "Player 1", change to "Player 2".
         - If `current_player` is "Player 2", change to "Player 3 (Computer)".
         - If `current_player` is "Player 3 (Computer)", change to "Player 1".

3. **After the Game Ends**:
   - Ask the user if they want to play again.
   - If "yes":
     - Restart the game by going back to step 2 (reset sticks and continue tracking losses).
   - If "no":
     - Proceed to step 4.

4. **End the Session**:
   - Display the total number of losses for each player:
     - `print("Player 1:", losses["Player 1"], "losses")`
     - `print("Player 2:", losses["Player 2"], "losses")`
     - `print("Player 3 (Computer):", losses["Player 3 (Computer)"], "losses")`

5. **Terminate the Game**.

### Key Details:
- **Input Validation**: Ensure that all user inputs are valid (e.g., sticks must be between 1 and 3, and the initial number of sticks must be between 10 and 100).
- **Player Turn Rotation**: After each player's turn, rotate to the next player in the order (Player 1 -> Player 2 -> Player 3 -> Player 1).
- **Loss Tracking**: Track the number of losses for each player across multiple rounds and display the results at the end.

### Example Flow:

1. **Initial Setup**:
   - User inputs 20 sticks.
   - Player 1’s turn.
   
2. **Turn 1**:
   - Player 1 takes 2 sticks (remaining sticks: 18).
   - Player 2’s turn.
   
3. **Turn 2**:
   - Player 2 takes 1 stick (remaining sticks: 17).
   - Player 3 (Computer)’s turn.
   
4. **Turn 3**:
   - Computer takes 3 sticks (remaining sticks: 14).
   - Player 1’s turn.

5. **Continue until the last stick is taken**.
6. **Game Ends**, and the player who took the last stick loses.
7. **Ask if they want to play again**.
