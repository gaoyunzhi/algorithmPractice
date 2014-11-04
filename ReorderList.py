# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		"""
		1. use slow and fast pointer to split the list into two halfs
			-- if length(list) is odd, then length(l1) = length(l2)+1
			-- if length(list ) is even, then length(l1) = length(l2)

		2. reverse l2

		3. merge l1 and l2

		http://www.cnblogs.com/zuoyuan/p/3700846.html
		"""
		if head == None or head.next == None or head.next.next == None:
		 #Careful of the basic case
			return head
	
		slow = fast = head

		# break linked list into two equal length
		# Careful:
		#	while fast.next is not enough
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		
		head1 = head
		head2 = slow.next
		slow.next = None

		# reverse linked list head2
		dummy = ListNode(0); dummy.next = head2
		p = head2.next; head2.next = None
		while p:
			tmp = p.next
			p.next = dummy.next
			dummy.next = p
			p = tmp

		head2 = dummy.next

		# merge two linked list head1 and head2
		p1 = head1; p2 = head2
		while p2:
			tmp1 = p1.next
			tmp2 = p2.next
			p1.next = p2; p2.next = tmp1
			p2 = tmp2; p1 = tmp1
