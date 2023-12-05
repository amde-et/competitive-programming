class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        b = 0
        count = -1
        for indd, d in enumerate(num1):
            while str(count) != d:
                count += 1
            a += count*10**(len(num1)-1-indd)
            count = -1
        for indz, z in enumerate(num2):
            while str(count) != z:
                count += 1
            b += count*10**(len(num2)-1-indz)
            count = -1
        return str(a*b)