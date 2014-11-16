# board.py
# Raven Pillmann
# Makes the graphical board for the game to be played on

from graphics import *
from pegs import *
from buttons import *

class Board:
	
	# A method which draws the board. It calls on the graphic method draw			
	def draw(self, win):
		win.setBackground("black")
		self.pallete.draw(win)
		for p in self.listOfPegs:
			p.draw(win)
		for c in self.listOfCircles:
			c.draw(win)
		for r in self.listOfRectangles:
			r.draw(win)
		
	# Creates the board by assigning lists of objects, which are drawn by the draw method
	def __init__(self):
			
		# creates the white rectangle on which the eight possible colors are laid out
		# for the user to select
		self.pallete = Rectangle(Point(30, 30), Point(270, 140))
		self.pallete.setFill(color_rgb(233, 225, 240))
		
		#Creates a list of pegs, which will allow users to select their colors
		self.listOfPegs = []
		for num in range(0,4):
			peg = Peg(num, 60 + 60*num, 60)
			self.listOfPegs.append(peg)
		for num in range(4,8):
			peg = Peg(num, 60 + 60*(num-4), 110)
			self.listOfPegs.append(peg)
		
		# Creates a list of circles, which will make up the ten rows of four slots each.
		# this functions as the graphical representations of the guesses. Set at grey for 
		# default
		self.listOfCircles = []
		for i in range(10):
			for j in range(4):
				circ = Circle(Point (30 + 60*j, 220 + 50*i), 20)
				circ.setFill("dark grey")
				self.listOfCircles.append(circ)
		
		# Creates the top four circles, each grey. At the end of the game, these will turn
		# into the right color combination (graphical representation of the answer)		
		for i in range(4):
			circ = Circle(Point(60 + 60*i, 730), 20)
			circ.setFill("light grey")
			self.listOfCircles.append(circ)
		
		# These rectangles will serve as the reply to each guess	
		self.listOfRectangles = []	
		for i in range(10):
			rect = Rectangle(Point(250, 200 + 50*i), Point(290, 240 + 50*i))
			rect.setFill("light grey")
			self.listOfRectangles.append(rect)
			
