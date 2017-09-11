from random import randint

class Problem:
	"""Abstract class for search problems.  
	
	Create subclasses for specific problem instances."""
	
	def __init__(self, initial=None, goal=None):
		"""Construct a problem instance with the specified initiil
		and goal states."""
		if not initial:
			self._initial = self.randomState()
		else:
			self._initial = initial
		if not goal:
			self._goal = self.getSolved()
		else:
			self._goal = goal
		
	def getSolved(self):
		"""Get the solved state."""		
		raise NotImplementedError
		
	def getInitial(self):
		"""Get the starting state."""		
		return self._initial
		
	def getGoal(self):
		"""Get the goal state."""		
		return self._goal
		
	def actions(self, state):
		"""Return a list of action possible for the given state."""
		raise NotImplementedError
		
	def result(self, state, action):
		"""Find the result of the action applied to the state."""
		raise NotImplementedError
		
	def cost(self, state, action):
		"""Return the cost of applying the action to the state."""
		raise NotImplementedError
		
	def heuristic(self, state):
		"""Return the heurstic value of the state."""
		raise NotImplementedError
		
	def goalReached(self, state):
		"""Test if the state is the goal."""
		return state == self._goal
		
	def randomState(self):
		"""Create a random state of the puzzle."""
		
		state = self.getSolved()
		for i in range(1000):
			a = self.actions(state)
			state = self.result(state, a[randint(0,len(a)-1)])
		return state
		
	def text(self, state):
		"""Return a textual representation of the state."""
		return NotImplementedError

	def initializeDraw(self, state):
		""'Setup a graphical representation of puzzles."""
		raise NotImplementedError
		
	def draw(self, action):
		"""Render the puzzle state graphically"""
		raise NotImplementedError
		
	def closeDraw(self, state):
		"""Close the graphics environments."""
		raise NotImplementedError
