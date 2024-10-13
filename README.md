[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2VU85VFt)
# CS151 PROGRAMMING ASSIGNMENT #2

### 🔵 Understand the problem and Design before Coding 🔵

#### 🔴 DESIGN DUE: Monday 10/14/24 12:00 PM
#### 🟡 DESIGN Revision DUE: Wednesday 10/16/24
#### 🟢 FINAL DUE: Wednesday 10/23/24

- #### Design grade: MRN
- #### Programming Grade: EMRN    
- #### [Markdown Tutorial-1](https://www.youtube.com/shorts/-aSSrmAXHDg)
- #### [Markdown Tutorial-2](https://www.youtube.com/shorts/0YLTInrkaHg)
- #### Use [markdown_basics file](markdown_cheatsheet.md) to write readable algorithm

## `I. PROBLEM:`

- You are creating a three player game of the Game of Sticks. 
- In this game there is a pile of sticks on the table, and players alternate turns taking 1-3 sticks. 
- The player to take the last stick loses.
- Youtube tutorial 

## `II. PURPOSE OF THE ASSIGNMENT`

The purpose of this assignment is to give you  
1. Practice with protecting against bad user input
2. Practice with decision-making
3. An opportunity to use looping
4. A chance to be creative

## `III. REQUIREMENTS ANALYSIS` 

The first stage in your programming assignment is the requirements analysis stage.  
You need to make sure you understand the game. 

**The rules are as follows**:
1.	The game starts with some number of sticks on the table (between 10 and 100, chosen by the user)
2.	Three players take turns choosing how many sticks to take.
3.	On each player’s turn they must take either 1, 2, or 3 sticks.
4.	The player to take the last stick loses.

**For your game, the following must be true**:

1. **One of your players is the program itself** (e.g. a computer player you play against); 
   1. the other two players are humans sitting at the computer together. 
   2. The computer player chooses a random number of sticks within the valid range (1-3). 
2. After the game ends, you must **ask the user if they want to play again**. 
   1. If so, the game resets. 
   2. However, you still keep track of losses across all games.
3. You must keep track of **how many times** each player loses the game
4. After the user decides they are ready to quit at the end of a game, you must **output how many times each player lost**.
5. You must have **error checking loops** on the types of values the user is inputting. 
   1. What values are the user inputting, and what could make them invalid?
6. You must have good HCI -- the user should know what is happening, even on the computer's turn!

If you want an added level of difficulty, you can make your computer player smarter instead of it having it choose a random number of sticks.
- This is not required, and should be attempted after you've figured out how to make the regular assignment work.

## `IV. DESIGN`

* The second stage is to design your solution based on the requirements. 
* Think about how to break the problem up into different smaller problems that are easier to solve. 
* I recommend thinking through and developing your algorithm using these smaller versions:

1. At first, completely ignore the fact that you get to play again. 
   1. Only after you've figured out the rest do you add that in. 
   2. Instead, first think through a basic game of three human players, with no error checking.
2. After you've figured that out, add in error checking.
3. Now, how do you make it so that one player is the computer? 
   1. What is the computer's steps? 
   2. Incorporate this into your algorithm. 
   3. HINT: choose which of the three players is always the computer. 
   4. The **computer will choose randomly** among the valid stick counts.
4. Now, keep track of how many losses each player has. How do you do that?
5. Now, add in the ability to play again with error checking.
6. If you want to make the extra optional smarter computer player, worry about that only at this point.
----------
* If you work through each part of the algorithm and slowly build it up, in the end you'll have the full program. 
* This is called **_iterative development_**, and is a **_key skill to develop for solving problems_**. 
* Don't stress about how you code it -- an algorithm is a time to think through the logic without stressing about code syntax.
----------

### `DESIGN SUBMISSION: 10/14/24`

- Push and commit to github: 
1. Write the algorithm for your design on `initial_design.md` document. 
2. The document can include aspects of the assignment 
   1. You think you've correctly included 
   2. You are not sure is correct or got stuck on.
   3. Importance of adding description
      1. To make it clear that you understand what you've done, or 
      2. Where you need the most help in getting ready to write the code.

If you decided to design a smarter computer player, note that in your document and why you designed it that way, so that you can get feedback on your design.

Your algorithm should follow the requirements of an algorithm, and contain all of the requirements for this assignment. **There should not be any code.**

## `V. PROGRAMMING REQUIREMENTS`

- After your design is complete and correct, it’s time to start programming and then testing. 
- This is a great time to start practicing iterative development. 
- Instead of writing an entire program and then testing it:
  - Write part of it, test it, then write the next part. 
  - That way if something is broken it will be easier to figure out why. 
  - Use the design guidelines to help you think through the order to implement and test.
- Remember that your game should:
  1. Follow good usability/HCI principles in input and output. 
     1. Be particularly mindful about what type of output is necessary for the user to understand what is going on in the game.
  2. Protect the program against bad user input
  3. State at the start the purpose of the program and how to play the game.

**Hint on random numbers:** To create a random number in Python use the method `randint(a,b)`. 
- It gives you a number randomly chosen in the range a<= number <=b. 
- For instance, if you write:
  ```python
  import random 
  choice = random.randint(10,50)
  ```
- The variable choice now holds a value that is `>=10` and `<=50`. 
- It is called a random number because the value you get will vary within that range if you call it many times in a row 
  - (To use this function you must `import random`).

**Complete a flowchart on your game to submit**.
- But First add `diagrams.net` plugin 
  - File -> Settings -> Plugins -> Marketplace: Then such and install `diagrams.net`
- Update the flowchart of your project using `flowchart.svg`
  - Use the process of drawing the flowchart as a chance to pay attention to if the logic of your game makes sense. 
  - Use the flowchart to help you determine how to test your code, but you do **_not need to submit the test cases_**.

## `VII. ASSIGNMENT REMINDERS`

- Follow the programming assignment requirements document for comments, formatting, etc. 
- Follow the honor code guidelines outlined in the syllabus and at [here](https://www.loyola.edu/academics/computer-science/current-students/honor-code).


## `VIII. FINAL SUBMISSION due 10/23`
### What to Submit in GitHub:

1. Completed `main.py` file  
2. `initial_design.md`
3. `final_design.md`
4. `flowchar.svg`
5. `reflection.md` -> Reflection of the assignment


**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working by yourself?
   
***Remember to commit and push your GitHub project.***