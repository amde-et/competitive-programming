class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list=[]
        for num in nums:
            list.append(int(num))
        list.sort(); list.reverse()
        return str(list[k-1])
