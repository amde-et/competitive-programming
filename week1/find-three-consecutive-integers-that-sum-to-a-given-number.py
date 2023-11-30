class Solution(object):
    def sumOfThree(self, num):
       
        if num%3==0:
            l=num//3
            return [l-1,l,l+1]
        return []
        
        