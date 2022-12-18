class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,first,last=0,0,len(nums)-1
        while i<=last:
            if nums[i]==0:
                nums[first],nums[i]=nums[i],nums[first]
                i+=1
                first+=1
            elif nums[i]==2:
                nums[i],nums[last]=nums[last],nums[i]
                last-=1
            else:
                i+=1
