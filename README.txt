Mastermind - READ ME

Raven Pillmann

TO RUN: Run mastermind.py in the command line

NOTE: This is my first attempt at creating a game in python. The comments and this README reflect
an attempt to make grading as easy as possible for my prefect. 


Mastermind is a popular game in which one player serves as a guesser and attempts to guess
a random code. The player has eight colors to choose from. He receives a response for every
guess that consists of red and white pegs. Red pegs indicate that the player has the right 
color in the right place, white indicates that he has the right color in the wrong place, and
an absence of peg indicates that he has a wrong color. If the user is correct, a message appears.
If he goes ten guesses without cracking the code, a different message appears.

Mastermind has the following classes:

Board - This class is mainly to help organize the code. I decided to form the board in its
own class, as the code to do so is long and would have made the mastermind program more confusing
than it needs to be.

Button - This class creates buttons. Button is called upon twice in the main program. The buttons
are "backspace" and "guess." This class can also activate and deactivate buttons, allowing the 
program to be selective and eliminate bugs, like backspacing when there are no pegs to be eliminated.

Combination - This class takes in a combination of pegs and checks to see if that combination is correct.
Again, this is simply to free up the program. It allows the programmer to write a cleaner code.

Pegs - Pegs creates colored pegs. The user can also check to see if the pegs are clicked. This could
be done in the main program, but due to the 40 different peg spaces on the board, I thought I would clean
the code up and make it its own class.

Graphics - I do not own graphics. It is used to create the shapes on the screen.





