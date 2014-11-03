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
	# @param k, an integer
	# @return a ListNode

	# k may be larger than the length, thus need the length of the list
	def lengthList(self, head):
		pointer = head
		length = 0
		while pointer:
			length += 1 
			pointer = pointer.next
		return length

	def rotateRight(self, head, k):
		"""
		Example:
		Given 1->2->3->4->5->NULL and k = 2,
		return 4->5->1->2->3->NULL.
		"""
		length = self.lengthList(head)
		if length == 0:
			return head

		K = k % length

		if head == None or head.next == None or K == 0:
			return head

		restLength = length - K

		pointer = head

		# Let pointer point to 3
		for i in range(restLength - 1):
			pointer = pointer.next
		# set pointer2 to 4 
		pointer2 = pointer.next
		

		# set pointer3 to 4 and let pointer3 goest to the end node
		pointer3 = pointer2
		while pointer3.next:
			pointer3 = pointer3.next
		#print pointer3.val
		# Now pointer3 points to the end node

		pointer.next = None
		pointer3.next = head
		return pointer2


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

new = sol.rotateRight(head, 3)
new.printSinglyLinkedList( )

		
