class BIT(object): 
    def __init__(self, n):
        self.__bit = [0]*(n+1) 

    def add(self, i, val):
        i += 1 
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        bit = BIT(len(arr))
        result = []
        for i in range(len(arr)):
            n = bit.query((arr[i]-1)-1)
            bit.add(arr[i]-1, 1)
            if n == i: 
                continue
            if n == 0:            
                if i > 1:
                    result.append(i) 
                result.append(i+1)    
            else:                     
                if n > 1:
                    result.append(n)  
                result.append(i)      
                result.append(i+1)    
                result.append(n+1)    
        return result
