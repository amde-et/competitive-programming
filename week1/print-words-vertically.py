class Solution:
    def printVertically(self, s: str) -> List[str]:
        temp = s.split()
        res = []

        l, k = 0, 0
        for i in temp:
            if (len(i) == l):
                k += 1
            elif (len(i) > l):
                k = 1
                l = len(i)
        for i in range(l):
            new = []
            for j in temp:

                if i < len(j):
                    new.append(j[i])
                    if (i + 1 == l):
                        k -= 1
                if (k == 0):
                    break
                elif (i >= len(j)):
                    new.append(' ')
            res.append("".join(new).rstrip())
            new = []
        return res        