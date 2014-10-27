# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# http://www.cnblogs.com/zuoyuan/p/3699508.html

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def merge(self, head1, head2):
		if head1 == None: return head2
		if head2 == None: return head1

		# Careful: build a new node for the return list
		dummy = ListNode(0)
		cursor = dummy
		while head1 and head2:
			if head1.val < head2.val:
				cursor.next = head1
				head1 = head1.next
				cursor = cursor.next
			else:
				cursor.next = head2
				head2 = head2.next
				cursor = cursor.next
		if head1 == None:
			cursor.next = head2
		if head2 == None:
			cursor.next = head1
		return dummy.next

	def sortList(self, head):
		if head == None  or head.next == None:
			return head
		# Careful: slow pointer and fast pointer
		#			in order to cut the linked list into half
		slowPointer = head; fastPointer = head
		#while fastPointer and fastPointer.next:
		while fastPointer.next and fastPointer.next.next:
			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

		"""
		注意递归传递的head1所在的链表是必须截断的，所以当slow.next传递给head2保存后，
		需要将slow.next 变为None
		"""
		head1 = head
		head2 = slowPointer.next
		slowPointer.next = None

		head1 = self.sortList(head1)
		head2 = self.sortList(head2)
		head = self.merge(head1, head2)
		return head




