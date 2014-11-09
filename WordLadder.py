# This can be seen as a search problem
# state = (string of current word, colorFlag)
# startState = (the start word,  0)
# Endstate = (the end word, *)
# Action(state) = (change some alphabet restricted by the dictionary)
# Cost(state, action) = 1

class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return an integer
	# def isEnd(self, state, end):
	# 	return True if state[0] == end else False

	# def getNewState(self, state, dictionary):
	# 	pass
	# 	return newStateList

	# def search(self, start, dictionary):
	# 	stack = []
	# 	stack.append([start, 0])
	# 	while stack:
	# 		currentState = stack[0]
	# 		currentState[1] = 1

	# 		stack.remove(stack[0])

	# 		actionList = self.getAction(currentState, dictionary)
	# 		for newState in newStateList:
	# 			if self.isEnd(newState, end):
	# 				return some level number?
	# 			else: stack.append(newState)

	def ladderLength(self, start, end, dictionary):
		dictionary.add(end)
		q = []
		q.append((start, 1))
		while q :
			curr = q.pop(0)
			currword = curr[0]; currlen = curr[1]
			if currword == end: return currlen
			for i in range(len(start)):
				part1 = currword[: i]; part2 = currword[i+1: ]
				for j in 'abcdefghijklmnopqrstuvwxyz':
					if currword[i] != j:
						nextword = part1 + j + part2
						if nextword in dictionary:
							q.append((nextword, currlen + 1))
							dictionary.remove(nextword)

		return 0

