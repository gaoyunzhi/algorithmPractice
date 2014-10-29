# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	# @param intervals, a list of Intervals
	# @param newInterval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		if intervals == [ ]:
			return [newInterval]
		intervals.append(newInterval)
		intervals.sort(key = lambda x: x.start)
		rec = [ ]
		rec.append(intervals[0])

		for i in range(1, len(intervals)):
			currentInterval = rec.pop( )
			if currentInterval.end >= intervals[i].start:
				_start = currentInterval.start
				_end = max(currentInterval.end, intervals[i].end)
				rec.append(Interval(_start, _end))
			else:
				rec.append(currentInterval)
				rec.append(intervals[i])

		return rec

