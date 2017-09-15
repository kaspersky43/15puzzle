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

                Manhattan Distance algorithm is effective as it is admissible, which means it never overestimates the optimal path in a graph or tree.

                M. Distance calculates the distance between two points along the axes, that of each tile tothe tile in the original position.

                This algorithm is effective because this takes into account how far the tile is from where it belongs and thus is more convincing than the number of misplaced tiles algorithm, which takes only the granted fact of the tiles being misplacd regarded

                A* algorithm used in the MySearch perform function serves to expand the search tree by expanding th enode for which the past cost cost and the heuristic value is minimum.
                The heuristic search and past cost make the lower bound on the cost of the path to the goal and the algorithm expands the search traversal only accordingly to the sum of the heuristic and the path cost every child node, meaning the path that A* search would take would always be less in the cost and heuristics together. 
                '''
		distance = 0
		for row in range(4):
                        for col in range(4):
                                if state[row][col] == 0: continue
                                distance += abs(row - state[row][col]/4) + abs(col - state[row][col]%4)
                return distance


                
