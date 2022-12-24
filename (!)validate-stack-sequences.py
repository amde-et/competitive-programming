class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,s= 0, []
        for j in pushed:
            s.append(j)
            while s and i < len(popped) and s[-1] == popped[i]:
                s.pop()
                i += 1
        return i == len(popped)
