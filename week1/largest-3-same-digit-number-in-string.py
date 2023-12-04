class Solution:
    def largestGoodInteger(self, num: str) -> str:
        target = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if int(num[i] + num[i+1] + num[i+2]) > target:
                    target = int(num[i] + num[i+1] + num[i+2])
        if target != -1:
            if target == 0:
                return str(target) + "00"
            return str(target)
        return ""