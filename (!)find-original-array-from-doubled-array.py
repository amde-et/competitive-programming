class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed)%2!=0:
            return []
        tmp = collections.Counter(changed)
        for x in sorted(tmp.keys()):
            if tmp[x] > tmp[2*x]:
                return []
            tmp[2*x] -= tmp[x] if x else tmp[x]//2
        return list(tmp.elements())
