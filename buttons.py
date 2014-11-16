# buttons.py
# Raven Pillmann
# Makes buttons for the game 

from graphics import *

# Creates buttons. 
class Button:

	# Creates a button with text, upper right coordinate, lower left coordinate, and an active 
	# boolean
	def __init__(self, text, upperright, lowerleft, active):
		self.text = text
		self.xur = upperright.getX()
		self.yur = upperright.getY()
		self.xll = lowerleft.getX()
		self.yll = lowerleft.getY()
		self.active = active
		if (self.active):
			self.color = "light grey"
		else:
			self.color = "dark grey"
	
	# makes the button active	
	def activate(self):
		self.active = True
		self.color = "light grey"
		
	#makes the button inactive
	def deactivate(self):
		self.active = False
		self.color = "dark grey"
	
	# draws the button based on the instance variables
	def draw(self, win):
		rect = Rectangle(Point(self.xur, self.yur), Point(self.xll, self.yll))
		rect.setFill(self.color)
		rect.draw(win)
		text = Text(Point((self.xur + self.xll)/2, (self.yur + self.yll)/2), self.text)
		text.draw(win)
		