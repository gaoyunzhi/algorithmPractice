class BinaryHeap:
	"""
	BinaryHeap() creates a new, empty, binary heap.
	insert(k) adds a new item to the heap.
	findMin() returns the item with the minimum key value, leaving item in the heap.
	delMin() returns the item with the minimum key value, removing the item from the heap.
	isEmpty() returns true if the heap is empty, false otherwise.
	size() returns the number of items in the heap.
	buildHeap(list) builds a new heap from a list of keys.

	Reference: http://interactivepython.org/runestone/static/pythonds/Trees/heap.html
	"""
	# the entire binary heap can be represented by a single list
	def __init__(self, length = 0, size = 0):
		# initialize the list and an attribute currentSize to keep track of the current size of the heap
		self.heapList = [0] # 'Wasted element' so that it can 
		self.currentSize = 0

	def percUp(self, i):
		while i // 2 > 0:
			if self.heapList[i/2] > self.heapList[i]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	def instert(self, k):
		""" Take O(log N)"""
		self.heapList.append(k)
		self.currentSize += 1
		self.percUp(self.currentSize)

	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				# swap won't damage the structure of the complete binary tree
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self,i):
		'return the position of the minimal child'
		if i * 2 > self.currentSize: return i # leaf node
		if i * 2 + 1 > self. currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else: return i * 2 + 1

	def delMin(self):
		"""
		So it will cost O(log N) to delete the root (minimum node)
		"""
		# pop the root node
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,alist):
		"""
		Since you are starting with a list of one item, the list is sorted and you could use binary 
		search to find the right position to insert the next key at a cost of approximately O(logn) 
		operations. However, remember that inserting an item in the middle of the list may 
		require O(n) operations to shift the rest of the list over to make room for the new key. 
		Therefore, to insert n keys into the heap would require a total of O(nlogn) operations. 

		However, if we start with an entire list then we can build the whole heap in O(n) operations. 
		"""
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self. percDown(i)
			i = i - 1


if __name__ == '__main__':
	bh = BinaryHeap( )
	bh.buildHeap([11, 23, 40, 1, 3, 56])
	for i in range(bh.currentSize):
		print bh.delMin( )
