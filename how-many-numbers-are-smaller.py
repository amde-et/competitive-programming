class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if len(nums)>=2 and len(nums)<=500:
            list=nums[:]
            result=[]
            for i in list:
                if i>=0 and i<=100:
                    tmp=0
                    for j in range(len(nums)):
                        if list[j]<i:
                            tmp+=1
                    result.append(tmp)
            return result
