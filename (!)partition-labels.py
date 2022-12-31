class Solution(object):
    def partitionLabels(self, s):
        list = {c: i for i, c in enumerate(s)}
        first, last = 0, 0
        res = []
        for i, c in enumerate(s):
            last = max(last, list[c])
            if i == last:
                res.append(i-first+1)
                first = i+1
        return res
