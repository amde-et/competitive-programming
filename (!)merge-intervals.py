class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result=[]
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
