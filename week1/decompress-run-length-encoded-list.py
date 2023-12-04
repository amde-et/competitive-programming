class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
     
        decompressed = []
       
        for i in range(len(nums)//2):
           
            frequency = nums[2*i]
            value = nums[2*i+1]
            
            
            decompressed += [value]*frequency
        
     
        return decompressed