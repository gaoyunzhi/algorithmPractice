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
	# @return a ListNode
	def deleteDuplicates(self, head):
		pointer = head
		#1->1->2->3->3, return 1->2->3
		if head is None:
			return head
         		
		while pointer.next:
			if pointer.val == pointer.next.val:
				pointer.next = pointer.next.next
			else:
				pointer = pointer.next

		return head

sol = Solution( )
head = ListNode(1)
p = head
p.next= ListNode(1)
p = p.next
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(3)

#head.printSinglyLinkedList()

sol.deleteDuplicates(head)

#head.printSinglyLinkedList()





