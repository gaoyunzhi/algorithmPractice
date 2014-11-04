# Definition for singly-linked list.
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
	# @param head, a ListNode
	# @return a list node
	def detectCycle(self, head):
		""" 
		First, compute the length of the loop
		Then set two pointers (p1 and p2), starting from head, but p1 is length steps ahead
		p1 and p2 moves at the same speed
		When p1 and p2 meet again, this where the loop starts.

		"""
		if head == None or head.next == None:
			return None

		slow = fast = head
		hasCycleFlag = False
		while slow and  fast.next and fast.next.next:
			if fast.next == slow or fast.next.next == slow:
				hasCycleFlag = True
				break
			fast = fast.next.next
			slow = slow.next
		# now slow = fast.next
		if hasCycleFlag:
			length = 1
			p1 = slow
			while p1.next != slow:
				p1 = p1.next
				length += 1

			p1 = p2 = head
			for i in range(length):
				p1 = p1.next
			while p1 != p2:
				p1 = p1.next
				p2 = p2.next
			return p2
		else:
			return None

sol = Solution( )
head = ListNode(1)
p = head
p.next= ListNode(1)
p = p.next
p2 = p
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(3)
#p.next = p2

print sol.detectCycle(head).val