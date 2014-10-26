class Solution:
    # @return an integer
    # Careful: I am not using the orthogonal way
	def reverse(self, x):
		t = ''; X = str(x); n = len(X)
		if x > 0:
			for i in range(n-1, -1, -1):
				t += X[i]
			return int(t)
		elif x<0:
			for i in range(n-1, 0, -1 ):
				t += X[i]
			return -int(t)
		else:	return 0
	# Careful: should think of the problem in this way
	def reverse2(self, x):
		answer = 0
		sign = 1 if x > 0 else -1
		x = abs(x)
		while x > 0:
			answer = answer * 10 + x % 10
			x /= 10
		return answer * sign

if __name__ == '__main__':
	pr = Solution( )
	print(pr.reverse2(-14))