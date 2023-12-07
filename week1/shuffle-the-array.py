class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1, l2= nums[:n], nums[n:]
        ls= []
        for i in range(n):
            ls.append(l1[i])
            ls.append(l2[i])
        return ls