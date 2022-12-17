class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if (len(nums)>=1 and len(nums)<=100) and (target>=1 and target<=100):
            list=sorted(nums)
            result=[]
            for i in range(len(list)):
                if list[i]>=1 and list[i]<=100:
                    if target==list[i]:
                        result.append(i)
            return result

                
