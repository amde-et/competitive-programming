class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        while len(nums)>=1:
            i=0
            size=0
            tmp=0
            while i<(len(nums)):
                size+=1
                tmp+=nums[i]
                if tmp == k:
                    break
                    break
                else:
                    i+=1
            nums=nums[1:]
            if tmp==k:
                return size
        return -1

