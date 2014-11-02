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
	"""
  	Note that this is a sorted linked list
  	注意 pointer.next 是否为None等等。。。
  	"""
	def deleteDuplicates(self, head):

		if head is None:
			return head

		sentinal = ListNode(0) #在head 前增加一个sentinal结点
		sentinal.next = head
		pointer = head
		pointer2 = sentinal #用两个pointer
		"""
		sentinal -> a -> b -> b-> c
					|       |
			    pointer2  pointer 	 
		"""

		Flag = False #标记是否遇到重复value
		while pointer.next:
		  	if pointer.val == pointer.next.val:
				Flag = True
				if pointer.next.next: 
			  		pointer.next = pointer.next.next
				else:
					"""
					因为可能出现这样的情况：
					sentinal -> a -> b -> b
								|       |
			    			pointer2  pointer 

					"""
					pointer2.next = None
					break

		 	else:
				if Flag == True:
					pointer = pointer.next
					pointer2.next = pointer
					Flag = False
			
				else:
					pointer = pointer.next
					pointer2 = pointer2.next

		return sentinal.next


sol = Solution( )
head = ListNode(2)
p = head
p.next= ListNode(2)
p = p.next
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)

#head.printSinglyLinkedList()

solution = sol.deleteDuplicates(head)

solution.printSinglyLinkedList()