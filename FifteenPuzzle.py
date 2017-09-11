# DO NOT EDIT THIS FILE

from Problem import *

from copy import *
from cs1graphics import *
from time import sleep

class FifteenPuzzle(Problem):
	"""A problem representing a 15 tile sliding puzzle.
	
	The representation will be a two-d array of which tile is
	in a given postion.  0 represents the empty space."""
	
	def getSolved(self):
		"""Return the solved state of the puzzle."""
		
		return ((0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15))
	
	def actions(self, state):
		"""Return the possible moves, represented by the integer that
		can be moved into the empty space."""
		
		for i in range(4):
			for j in range(4):
				if state[i][j] == 0:
					position = (i,j)
			
		actions = []		
		if position[0] > 0:
			actions.append( state[position[0]-1][position[1]] )
		if position[0] < 3:
			actions.append( state[position[0]+1][position[1]] )
		if position[1] > 0:
			actions.append( state[position[0]][position[1]-1] )
		if position[1] < 3:
			actions.append( state[position[0]][position[1]+1] )

		return actions
		
	def result(self, state, action):
		"""Apply the action to the state."""
		
		for i in range(4):
			for j in range(4):
				if state[i][j] == 0:
					blank = (i,j)
				if state[i][j] == action:
					position = (i,j)
					
		newState = [ [ x for x in y ] for y in state ]
		newState[blank[0]][blank[1]] = action
		newState[position[0]][position[1]] = 0
		newState = tuple( [ tuple([ x for x in y ]) for y in newState ] )		
		
		return newState
				
	def cost(self, state, action):
		"""Calculate the cost of transitioning from one state to the next."""
		
		return 1
		
	def text(self, state):
		"""Return a textual representation of the puzzle state."""
		
		return '\n'.join( [ ' '.join(["%2s"%y if y>0 else "  " for y in x]) for x in state ] )
		
	def initializeDraw(self):
		"""Setup a graphical representation of puzzles."""
		
		self._canvas = Canvas(200,200)
		self._canvas.setBackgroundColor('gray')
		self._tiles = [None]
		for i in range(1,16):
			t = TextBox(50,50)
			t.setMessage(str(i))
			t.setFontSize(30)
			t.setFillColor('tan')
			t.setBorderColor('black')
			t.setBorderWidth(3)
			t.moveTo(-500,-500)
			self._tiles.append(t)
			self._canvas.add(t)
			
	def draw(self, state):
		"""Render the puzzle state graphically"""
		for i in range(4):
			for j in range(4):
				t = state[i][j]
				if t > 0:
					self._tiles[t].moveTo(50*j+25,50*i+25)
		
	def drawAction(self, state, action):
		"""Animate the puzzle state being transformed by the action."""
		
		self.draw(state)
		for i in range(4):
			for j in range(4):
				if state[i][j] == action:
					y,x = i,j	# Where the tile is
				elif state[i][j] == 0:
					b,a = i,j	# Where the blank spot is
					
		for i in range(50):
			self._tiles[action].move( (a-x), (b-y) )
			sleep(.02)
		
		
	def closeDraw(self, state):
		"""Close the graphics environments."""
		
		self._canvas.close()

