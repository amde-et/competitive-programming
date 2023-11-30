class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        sm=0
        val=16
        while val>=0:
            tmp=3**val
            if sm+tmp<n:
                sm+=tmp
            elif sm+tmp==n:return True
            val-=1
        return False