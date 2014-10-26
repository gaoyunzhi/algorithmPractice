# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# ListNode_1 -> ListNode_2 -> ListNode_3 ->... This is a singly-linked list, 
# Need to return the first node ListNode_1

class Solution:
		# @param a list of ListNode
		# @return a ListNode
	def mergeKLists(self, lists):
		heap = []
		for node in lists:
			if node: # Can easily miss this line
				heap.append((node.val, node))
		heapq.heapify(heap) # Create the min binary heap

		head = ListNode(0); curr = head # head is the head ListNode
		while heap:
			pop = heapq.heappop(heap)
			curr.next = ListNode(pop[0])
			curr = curr.next
			if pop[1].next: 
				heapq.heappush(heap, (pop[1].next.val, pop[1].next))
		return head.next





