# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	# @param intervals, a list of Interval
	# @return a list of Interval
	def printIntervals(self, intervals):
		for i in range(len(intervals)):
			print('[', intervals[i].start, ',', intervals[i].end,']', )

	def merge(self, intervals):
		"""
		先将区间按照每个start的值来排序，排好序以后判断一个
		区间的start值是否处在前一个区间中，如果在前一个区间中，
		那么合并；如果不在，就将新区间添加。
		http://www.cnblogs.com/zuoyuan/p/3782028.html
		"""
		print('initial intervals')
		self.printIntervals(intervals)
		if len(intervals) == 1 or len(intervals) == 0:
			return intervals
		"""
		Careful: sort() method! 还有这里先按照start进行排序
		"""
		intervals.sort(key = lambda x: x.start)
		length = len(intervals)
		res = [intervals[0]]
		for i in range(1, length):
			currentInterval = res.pop( )
			"""
			Careful: 注意判断条件的完整性
			"""
			if currentInterval.end >= intervals[i].start:
				tmpInterval = Interval(currentInterval.start, max(currentInterval.end, intervals[i].end))
				res.append(tmpInterval)

			else:
				res.append(currentInterval)
				res.append(intervals[i])
		#print('length of res', len(res))
		return res


I = [Interval(1,4), Interval(2, 6)]
sol = Solution( )
intervals = sol.merge(I)
print("solution")
sol.printIntervals(intervals)
