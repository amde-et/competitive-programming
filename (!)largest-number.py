class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        temp = [str(i) for i in nums]
        temp.sort(key=cmp_to_key(lambda x, y: 1 if x+y < y+x else -1))
        result = "".join(temp)
        if result[0] == "0":    
            return "0"
        else:                   
            return result
