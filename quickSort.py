import random

def quickSort(alist):
	quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
	# Careful:  at first I misused 'while' instead of 'if'
	if first < last:
		splitPoint = partition(alist, first, last)
		quickSortHelper(alist, first, splitPoint - 1)
		quickSortHelper(alist, splitPoint + 1, last)

def partition(alist, first, last):
	#pivot = int(random.random( ) *(last - first) + first )  # int 是下取整
	pivotValue = alist[last]

	leftmark = first - 1
	rightmark = first

	for rightmark in range(first, last):
		if alist[rightmark] <= pivotValue:
			leftmark = leftmark+ 1 # the first element in the RHS

			tmp = alist[leftmark] 
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = tmp
		#print(alist[first: last])

	tmp = alist[leftmark + 1]
	alist[leftmark + 1] = pivotValue
	alist[last] = tmp
	return leftmark + 1

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)






