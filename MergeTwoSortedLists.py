class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def printSinglyLinkedList(self):
		p = self
		while p:
			print p.val
			p = p.next


class Solution:
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		
		newList = ListNode(0)
		pointer = newList
		"""
		Careful: 
		newList = l1
		...
		This is wrong!!!!!! It will damage the original list and make the while loop run forever

		"""
		while l1 and l2:
			if l1.val < l2.val:
				pointer.next = l1
				l1 = l1.next
				pointer = pointer.next
			else:
				pointer.next = l2
				l2 = l2.next
				pointer = pointer.next
		
		if l1:
			pointer.next = l1
			return newList.next
		elif l2:
			pointer.next = l2
			return newList.next
		else:
			return newList.next
		
sol = Solution( )
l1= ListNode(1)
p = l1
p.next= ListNode(2)
p = p.next
p.next = ListNode(3)

l2  = ListNode(-1)
p = l2
p.next = ListNode(2.5)
p = p.next
p.next = ListNode(2.7)

new = sol.mergeTwoLists(l1, l2)
new.printSinglyLinkedList()