# combination.py
# Raven Pillmann
# Creates a guess

class Combination:
	
	def __init__(self, guess):
		self.but1 = int(guess[0])
		self.but2 = int(guess[1])
		self.but3 = int(guess[2])
		self.but4 = int(guess[3])
		self.guess = [self.but1, self.but2, self.but3, self.but4]

	def isRight(self, answer):
	
		answerCopy = []
		reply = []
		
		for ans in answer:
			answerCopy.append(ans)
		
		for count in range(4):
			if (self.guess[count] == answerCopy[count]):
				reply.append(2)
				self.guess[count] = -2
				answerCopy[count] = -1
		
		for peg in range(4):
			for ans in range(4):
				if (self.guess[peg] == answerCopy[ans]):
					self.guess[peg] = -2
					answerCopy[ans] = -1
					reply.append(1)
					break
		
		if (len(reply) != 4):
			for i in range(len(reply), 4):
				reply.append(0)

		return reply