class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if (len(nums)>=1 and len(nums)<=100000) and (k>=1 and k<=1000000000):
            size=0
            tmp=0
            while len(nums)>=1:
                for i in nums:
                    if i>=-100000 and i<=100000:
                        size+=1
                        tmp+=i
                        if tmp!=k:
                            nums=nums[1:]
                        else:
                            break
                        break
            if tmp==k:
                return size
            else:
                return -1
