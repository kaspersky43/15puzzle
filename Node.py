class Node:
	"""A node of a search tree."""
	
	def __init__(self, state, parent=None, action=None, cost=0):
		"""Create a search tree node that is obtained by performing
		an action to the parent of a given cost."""
		
		self._state = state
		self._parent = parent
		self._action = action
		self._cost = cost
			
	def getState(self):
		"""Return the current state of the node."""
		return self._state
			
	def path(self):
		"""Return the sequence of actions from the root to this node."""
		upwardPath = []
		node = self
		while node:
			upwardPath.append(node)
			node = node._parent
		return [ n._action for n in reversed(upwardPath[:-1]) ]
		
	def pathCost(self):
		"""Return the cost of the path from the root to this node."""
		upwardPath = []
		node = self
		while node:
			upwardPath.append(node)
			node = node._parent
		return sum([ n._cost for n in reversed(upwardPath[:-1]) ])

	# Note nodes with the same state should be consider the same,
	# so we use a nodes state for comparison.
	def __lt__(self, other):
		return self._state < other._state
		
	def __eq__(self, other):
		return self._state == other._state
		
	def __hash__(self):
		return hash(self._state)
