def mergeSort(alist):
	print("Splitting ",alist)
	if len(alist) > 1:
		# split the list into 2 parts
		mid = len(alist) // 2
		lefthalf = alist[:mid]  # return a copy of alist
		righthalf = alist[mid:]

		mergeSort(lefthalf) # don't need to return
		mergeSort(righthalf)

		# merge the two halfs
		# i for left half, j for right half, k for the original alist
		i = 0; j = 0; k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j< len(righthalf):
			alist[k]=righthalf[j]
			j += 1
			k += 1


alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
