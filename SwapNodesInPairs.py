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
	# @param a ListNode
	# @return a ListNode
	def swapPairs(self, head):
		pointer = head
		# need a sentinel
		sentinel = ListNode(0)
		sentinel.next = head
		pointer2 = sentinel

		while pointer:
			# case 1: there are even number of nodes
			"""
			注意pointer的调换顺序
			"""
			if pointer.next:
				nextPoint = pointer.next
				pointer2.next = nextPoint
				pointer.next = nextPoint.next
				nextPoint.next = pointer
				pointer2 = pointer
				pointer = pointer.next
			else:
				break

		return sentinel.next

sol = Solution( )
head = ListNode(1)
p = head
p.next= ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(5)

#head.printSinglyLinkedList()
a = sol.swapPairs(head)
a.printSinglyLinkedList()
