# mastermind.py
# Raven Pillmann
# The game itself. It takes advantage of nested loops to build "guesses" until the user either
# guesses correctly or runs out of guesses.

# graphics.py is not made by me. I do not own the rights.

from graphics import *
from combination import *
from random import randrange
from pegs import *
from board import *
from buttons import *

def main():

	# Creates the window for the game
	win = GraphWin("MasterMind", 300, 760)
	win.setCoords(0, 0, 300, 760) 
	
	# Calls on the Board class to draw an initial game board layout.
	board = Board()
	board.draw(win)
	
	# Calls on the Button class to make the backspace and guess buttons
	button1 = Button("Backspace", Point(60, 190), Point (120, 150), False)
	button1.draw(win)
	button2 = Button("Guess", Point(180, 190), Point(240, 150), False)
	button2.draw(win)
	
	# sets the answer to some random combination
	answer = [randrange(0,7), randrange(0,7), randrange(0,7), randrange(0,7)]
	
	# goes through each guess (ten in total). This loop will stop if the user gets the answer
	# right, or if he runs out of guesses
	for i in range(10):
		guess = []
		count = 0
		
		button1.deactivate()
		button1.draw(win)
		
		button2.deactivate()
		button2.draw(win)
		
		row = 220 + 50*i
		
		
		# goes through each peg for each guess (four in total). 
		while count <= 4:
			
			column = 30 + 60*(count)
			
			
			# Waits for a click
			point = win.getMouse()
			xpoint, ypoint = point.getX(), point.getY()
			
			# These conditionals check to see where the mouse clicked...
			if (40 < ypoint < 80):
				if (40 < xpoint < 80):
					number = 0
				elif (100 < xpoint < 140):
						number = 1
				elif (160 < xpoint < 200):
					number = 2
				elif (220 < xpoint < 260):
					number = 3
				else:
					number = 10
			elif (90 < ypoint < 130):
				if (40 < xpoint < 80):
					number = 4
				elif (100 < xpoint < 140):
					number = 5
				elif (160 < xpoint < 200):
					number = 6
				elif (220 < xpoint < 260):
					number = 7
				else:
					number = 10
			elif (150 < ypoint < 190):
				if (60 < xpoint < 120):
					if button1.active:
						number = 8
						button2.deactivate()
						button2.draw(win)
					else:
						number = 10
				elif (180 < xpoint < 240):
					if button2.active:
						number = 9
					else:
						number = 10
				else:
					number = 10
			else:
				number = 10

			# ...and these turn those clicks into functions.
			# The if places color pegs into the guess slots
			if number in [0, 1, 2, 3, 4, 5, 6, 7]:
				guess.append(number)
				peg = Peg(number, column, row)
				peg.draw(win)
				if (len(guess) != 0):
					button1.activate()
					button1.draw(win)
				if (len(guess) == 4):
					button2.activate()
					button2.draw(win)
				count += 1
			
			# this elif statement backspaces a guess
			elif number == 8:
				guess.pop(count - 1)
				circle = Circle(Point(column-60,row), 20)
				circle.setFill('dark grey')
				circle.draw(win)	
				count -= 1			
				if len(guess) == 0:
					button1.deactivate()
					button1.draw(win) 
			
			# this elif submits the guess
			elif number == 9:
				break
				
			# this elif restarts the loop, just in case the user clicks where he isn't supposed to
			elif number == 10:
				continue
				
			elif count == 4:
				break
				
		# creates a reply, which calls on the combination method isRight(answer)
		attemptedGuess = Combination(guess)
		reply = attemptedGuess.isRight(answer)
		c = 0
		for ind in reply:
			rect = Rectangle(Point(250+10*c, row-20), Point(260+10*c, row+20))
			if (ind == 2):
				rect.setFill("red")
			elif (ind == 1):
				rect.setFill("white")
			elif (ind == 0):
				rect.setFill("dark grey")
			rect.draw(win)
			c += 1
		
		# checks to see if the answer if correct
		if (reply == [2, 2, 2, 2]):
			break
			
	
	# Gives a graphical response to either winning or losing the game. First, it colors in
	# the answer combination. Then, it sets a congratulatory or "better luck next time" message	
	c = 0
	for ind in answer:
		ansPeg = Peg(ind, 60+60*c, 730)
		ansPeg.draw(win)
		c += 1	
	text = Text(Point(150, 325), "Click anywhere to quit")
	text.setTextColor("dark green")
	text.draw(win)
	if (reply == [2, 2, 2, 2]):
		text = Text(Point(150, 375), "You cracked the code!")
		text.setFace('arial')
		text.setSize(25)
		text.setStyle('bold')
		text.setTextColor("dark green")
		text.draw(win)
	elif (i == 9):
		text = Text(Point(150, 375), "Better luck next time")
		text.setFace('arial')
		text.setSize(25)
		text.setStyle('bold')
		text.setTextColor('dark green')
		text.draw(win)
				
	point = win.getMouse()
	win.close()
main()