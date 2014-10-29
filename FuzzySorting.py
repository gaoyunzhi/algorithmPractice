"""问题描述： 
 * 考虑这样的一种排序问题，即无法准确地知道待排序的各个数字到底是多少。对于其中的每个数字， 
 * 我们只知道它落在实轴上的某个区间内。亦即，给定的是n个形如[a(i), b(i)]的闭区间（这里小括 
 * 后起下标的作用，后同），其中a(i) <= b(i)。算法的目标是对这些区间进行模糊排序 
 * （fuzzy-sort），亦即，产生各区间的一个排列<i(1), i(2), ..., i(n)>，使得存在一个c(j)属于 
 * 区间[a(i(j)), b(i(j))]，满足c(1) <= c(2) <= c(3) <= ... <= c(n)。 
 * a) 为n个区间的模糊排序设计一个算法。你的算法应该具有算法的一般结构，它可以快速排序左部 
 * 端点（即各a(i)），也要能充分利用重叠区间来改善运行时间。（随着各区间重叠得越来越多， 
 * 对各区间进行模糊排序的问题会变得越来越容易。你的算法应能充分利用这种重叠。） 
 * b) 证明：在一般情况下，你的算法的期望运行时间为Θ(nlgn)，但当所有的区间都重叠时，期望的 
 * 运行时间为Θ(n)（亦即，当存在一个值x，使得对所有的i，都有x∈[a(i), b(i)]）。你的算法 
 * 不应显式地检查这种情况，而是应随着重叠量的增加，性能自然地有所改善。

 http://courses.csail.mit.edu/6.046/spring04/handouts/ps2-sol.pdf 
 """
import random
from util import Interval 


def compareInterval(interval1, interval2):
	"""
	if [interval1] < [interval2] is True, return True
	if [interval1] > [interval2] is True, return False
	if [interval1] and [interval2] has overlap, return None, as they are equal

	In the question, we assume no interval is completely contained in another interval

	"""
	if interval1.end < interval2. start:
		return True
	if interval1.start > interval2.end:
		return False
	if interval1.end >= interval2.start or interval1.start >= interval2.end:
		return None

def merge(interval1, interval2):
	"""
	interval1 and interval2 must have overlap
	"""
	if interval1.start > interval2.end or interval2.start > interval1.end:
		#print('wront intervals, cannot merge')
		return None
	mergedInterval = Interval(min(interval1.start, interval2.start), max(interval1.end, interval2.end))
	return mergedInterval

#testcase:
# merge(Interval(1, 2), Interval(3,4))
# merge(Interval(1,3), Interval(2,4)).printInterval( )
# merge(Interval(2,4), Interval(1,3)).printInterval( )

def swap(intervals, index1, index2):
	intervals[index1], intervals[index2] = intervals[index2], intervals[index1]


def partition(intervals, p, q):
	pivot = random.choice(range(p, q+1))
	swap(intervals, pivot, q)

	pivotInterval = intervals[q]
	print('Chosen pivot')
	pivotInterval.printInterval( )
	print('sort')
	for _ in intervals[p: q+1]:
		_.printInterval( )
	print('********************')

	leftPointer = p - 1
	rightPointer = p
	pivotPointer = q

	while rightPointer < pivotPointer:
		if compareInterval(intervals[rightPointer], pivotInterval) == None:
			pivotPointer -= 1
			swap(intervals, rightPointer, pivotPointer)
			pivotInterval = merge(pivotInterval, intervals[pivotPointer]) # update pivotInterval

		elif compareInterval(intervals[rightPointer], pivotInterval) == True:
			"""
			Becareful of the order of the following three lines
			"""
			leftPointer +=1
			swap(intervals, leftPointer, rightPointer)
			rightPointer += 1

		elif compareInterval(intervals[rightPointer], pivotInterval) == False:
			rightPointer += 1

		for _ in intervals:
			_.printInterval( )
			
		print ("@@@@@@@@@@@@@@@@@")

	# Put the pivots back
	tmpIndex = q
	tmpIndex2 = leftPointer+1

	while tmpIndex >= pivotPointer:
		swap(intervals, tmpIndex, tmpIndex2)
		for _ in intervals:
			_.printInterval( )
		tmpIndex -= 1
		tmpIndex2 += 1


	# tmpIntervals = intervals[pivotPointer : q]
	# tmpIntervals2 = intervals[leftPointer+1: rightPointer]

	# del intervals[leftPointer+1: q]
	# intervals.extend(tmpIntervals)
	# intervals.extend(tmpIntervals2)

	for _ in intervals:
		_.printInterval( )
	print("$$$$$$$$$$$$$$$$")

	return leftPointer + 1, leftPointer + len(intervals) - pivotPointer + 1

#test
#_intervals = [Interval(1,2), Interval(2,3), Interval(6,7), Interval(4,5), Interval(9,10)]
# result = partition(_intervals, 0, len(_intervals)-1)
# print(result)
# for _ in _intervals:
# 	_.printInterval( )


def fuzzySorting(intervals, start, end):
	"""
	At first, I used some sort of intarvals[:leftpointer] in the recursion.
	However, note that this returns a copy of the segment of intervals, it doesn't refer to the
	original intervals. To implement an in-place sort here, I finally changed the recursion 
	function and added two more variables.
	"""
	if start < end:
		pivotLeft, pivotRight = partition(intervals, start, end)
		fuzzySorting(intervals, start, pivotLeft)
		fuzzySorting(intervals, pivotRight, end)

_intervals = [Interval(1,2), Interval(2,3), Interval(6,7), Interval(4,5), Interval(9,10)]		
fuzzySorting(_intervals, 0, len(_intervals) -1)
print("*******end*************")
for _ in _intervals:
	_.printInterval( )

#test





