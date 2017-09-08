from FifteenPuzzle import *

class MyFifteenPuzzle(FifteenPuzzle):
	def __init__(self, initial=None):
		FifteenPuzzle.__init__(self, initial)
		
		# Put any initialization code here.
	
	def heuristic(self, state):
		# Redefine this if you are doing best first, A* search, etc.
		return 0
