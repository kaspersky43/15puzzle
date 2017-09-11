from FifteenPuzzle import *

class MyFifteenPuzzle(FifteenPuzzle):
	def __init__(self, initial=None):
		"""Do precomputations for puzzle heuristics."""
		
		FifteenPuzzle.__init__(self, initial)
		
		# Put any initialization code here.
	
	def heuristic(self, state):
		"""A heuristic to aid in searching the solution space."""
		
		# Redefine this if you are doing best first, A* search, etc.
		return 0
