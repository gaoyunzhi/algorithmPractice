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
	# @return a boolean
	def hasCycle(self, head):
		"""
		Somehow tricky
		http://www.cnblogs.com/zuoyuan/p/3701639.html
		http://ostermiller.org/find_loop_singly_linked_list.html
		"""
		if head == None or head.next == None:
			return False

		slow = fast = head
		while slow and  fast.next and fast.next.next:
			if fast.next == slow or fast.next.next == slow:
				return True
			fast = fast.next.next
			slow = slow.next

		return False


