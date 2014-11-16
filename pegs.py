# pegs.py
# Raven Pillmann
# makes colored pegs

from graphics import *

class Peg:

	# initializes a peg, which is pretty much just a colored circle. 
	def __init__(self, number, xpoint, ypoint):
		self.peg = Circle(Point(xpoint, ypoint), 20)
		self.point = (xpoint, ypoint)
		self.xpoint = xpoint
		self.ypoint = ypoint
		self.number = number
		if (number == 0):
			self.peg.setFill("red")
			self.peg.setOutline("red")
		elif (number == 1):
			self.peg.setFill("orange")
			self.peg.setOutline("orange")
		elif (number == 2):
			self.peg.setFill("yellow")
			self.peg.setOutline("yellow")
		elif (number == 3):
			self.peg.setFill("green")
			self.peg.setOutline("green")
		elif (number == 4):
			self.peg.setFill("light blue")
			self.peg.setOutline("light blue")
		elif (number == 5):
			self.peg.setFill("purple")
			self.peg.setOutline("purple")
		elif (number == 6):
			self.peg.setFill("brown")
			self.peg.setFill("brown")
		elif (number == 7):
			self.peg.setFill("white")
			self.peg.setFill("white")	
	
	# draws the peg	
	def draw(self, win):
		return self.peg.draw(win)
	
	# checks to see if the peg has been clicked
	def clickPeg(self, x, y):
		if (x < xpoint + 20) and (x > xpoint - 20) and (y > ypoint - 20) and (y < ypoint + 20):
			return True