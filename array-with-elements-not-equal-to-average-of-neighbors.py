class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for k in range(3):
            for i in range(1,len(nums)-1):
                j=i-1
                while (nums[i-1]+nums[i+1])/2 == nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    j+=1
        return nums
