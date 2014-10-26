class Solution:
    # @return a string
    def countAndSay(self, n):
        # Careful: Mine version is based on recursion
        if n == 1:
            return '1'

        originString = self.countAndSay(n-1)
        newString = ''
        counterName= [originString[0]]
        counterNumber = [1]
        
        for i in range(1, len(originString)):
            if originString[i] == originString[i-1]:
                counterNumber[-1] += 1
            else:
                counterName.append(originString[i])
                counterNumber.append(1)

        for j in range(len(counterName)):
            newString =newString + str(counterNumber[j])
            newString = newString + counterName[j]
        return newString


#########################################################
# Use iteration:
    def count(self, s):
        # initialize:
        t = ''; counter = 0; lastOccur = '#'
        for i in s:
            if i != lastOccur:
                if lastOccur != '#':
                    t +=str(count) + lastOccur
                lastOccur = i
                count = 1
            else:
                count += 1

        t+=str(count)+lastOccur
        return t

    def countAndSay2(self, n):
        s = '1'
        for j in range(2, n+1):
            s = self.count(s)
        return s
        # originString = '1'
        # if n ==1:
        #     return originString

        # for i in range(1:n):
        #     counterName = []
        #     counterNumber = []
        #     for j in range(len(originString)):
        #         if 


if __name__ == '__main__':
    solve = Solution( )
    #solve.countAndSay(5)
    print(solve.countAndSay2(5))