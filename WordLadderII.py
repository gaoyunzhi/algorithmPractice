class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return a list of lists of string

	 # This should be a tree and
	def cacheWords(self, start, end, dictionary):
		dictionary.add(start)
		dictionary.add(end)
		cache = {}
		for word in dictionary:
			cache[word] = []
			for i in range(len(word)):
				part1 = word[: i]; part2 = word[i+1: ]
				for j in 'abcdefghijklmnopqrstuvwxyz':
					if word[i] != j:
						nextword = part1 + j + part2
						if nextword in dictionary:
							cache[word].append(nextword)
		return cache


	def newWordList(self, state, cache):
		currentWord = state[0]
		currentPath = state[1]
		wordList = set(cache[currentWord]) - set(currentPath)
		return wordList

	def findLadders(self, start, end, dictionary):
		cache = self.cacheWords(start, end, dictionary)
		print cache
		queue = []
		queue.append((start, [start]))
		result = []
		flag = False
		while queue:
			currentState, currentPath = queue.pop(0)
			#print currentState, currentPath
			if not flag:
				if currentState == end: 
					result.append(currentPath)
					breakLevel = len(currentPath)
					flag = True
				else:
					wordList = self.newWordList((currentState, currentPath), cache)
					for _word in wordList:	
						_path = currentPath[:]
						_path.append(_word)
						queue.append((_word, _path))

			else:
				if currentState == end and len(currentPath) == breakLevel:
					result.append(currentPath)

				elif len(currentPath) < breakLevel:
					wordList = self.newWordList((currentState, currentPath), cache)
					for _word in wordList:	
						_path = currentPath[:]
						_path.append(_word)
						queue.append((_word, _path))
		return result

sol = Solution()
start = "hit"
end  = "cog"
dictionary = set(["hot","dot","dog","lot","log"])

print sol.findLadders(start, end, dictionary)