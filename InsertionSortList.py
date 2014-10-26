# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None


# Careful: 指针操作
# http://www.cnblogs.com/zuoyuan/p/3700105.html
class Solution:
# @param head, a ListNode
# @return a ListNode
	def insertionSortList(self, head):
		# handle none 
		if not head:
			return head
		dummy = ListNode(0)			#为链表加一个头节点
		dummy.next = head
		curr = head
		#如果链表是升序的，那么curr指针一直往后移动
		#直到一个节点的值小于前面节点的值
		#然后寻找插入的位置
		while curr.next:
			if curr.next.val < curr.val: 
				pre = dummy
				while pre.next.val < curr.next.val:
					pre = pre.next
				tmp = curr.next
				curr.next = tmp.next
				tmp.next = pre.next
				pre.next = tmp
			else:
				curr = curr.next
		return dummy.next



