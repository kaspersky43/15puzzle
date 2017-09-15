from FifteenPuzzle import *

class MyFifteenPuzzle(FifteenPuzzle):
	def __init__(self, initial=None):
		"""Do precomputations for puzzle heuristics."""
		
		FifteenPuzzle.__init__(self, initial)
		# Put any initialization code here.

	
	def heuristic(self, state):
		"""A heuristic to aid in searching the solution space."""

		'''
                Using the heuristic to count the misplacement sums using the A* algorithm
                Manhattan Distance algorithm 
                '''
		distance = 0
		for row in range(4):
                        for col in range(4):
                                if state[row][col] == 0: continue
                                distance += abs(row - state[row][col]/4) + abs(col - state[row][col]%4)
                return distance
