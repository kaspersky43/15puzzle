from random import randint
from time import time

from Node import *
from drawTree import *

# Set this to False to speed up search and not show the tree/graphs
visualize = True

class MySearch:	
	def __init__(self):
		pass
	
	def perform(self, problem):
		# Redefine this method for anything you want to do
		
		print 'Performing search'
		startTime = time()
		
		root = Node(problem.getInitial()) 	# Setup the data structure for storing nodes to explore
		queue = [root]						# And put the root in it
		
		found = set()
		found.add(problem.getInitial())
		
		if visualize:
			allNodes = set()
			allNodes.add(root)
			
		expanded = 0
		
		while len(queue) > 0: 
			node = queue.pop(randint(0,len(queue)-1))	# Choose a random unexplored node
			state = node.getState()
			
			if problem.goalReached(state):
				ellapsed = time() - startTime
				print 'Solution found in', ellapsed, 'seconds'
				print 'Expanded', expanded, 'nodes.'
				print 'Evaluation rate =', expanded/nodes, 'nodes/sec.'
				return node.path()  # Return a list of actions to get to solved state
			
			expanded += 1
			if expanded % 10000 == 0:
				print 'Exapnded', expanded, 'nodes.', len(queue), 'on queue'
			
			if visualize:	
				print 'Selected node'
				print problem.text(state)
				print
				
			found.add(state)
			
			if visualize:
				drawTree(problem, allNodes, problem.getInitial(), problem.getGoal(), state)
				drawGraph(problem, allNodes, problem.getInitial(), problem.getGoal(), state)
				raw_input()
			
			for action in problem.actions(state):
				if visualize:
					print 'Expanding with action', action
				
				result = problem.result(state, action)
				
				if result not in found:
					cost = problem.cost(state, action)
					child = Node(result, node, action, cost)
					
					queue.append(child)		# Add the child to the nodes to explore
					found.add(result)
					
					if visualize:
						allNodes.add(child)
						

			if visualize:
				print 'Expanded'
				print
				drawTree(problem, allNodes, problem.getInitial(), problem.getGoal(), state)
				drawGraph(problem, allNodes, problem.getInitial(), problem.getGoal(), state)
				raw_input()
