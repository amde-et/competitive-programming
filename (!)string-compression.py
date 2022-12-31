class Solution(object):
    def compress(self, chars):
        tmp, res = 0, 0
        for read, c in enumerate(chars):
            if read+1 == len(chars) or chars[read+1] != c:
                chars[res] = chars[tmp]
                res += 1
                if read > tmp:
                    n, left = read-tmp+1, res
                    while n > 0:
                        chars[res] = chr(n%10+ord('0'))
                        res += 1
                        n /= 10
                    right = res-1
                    while left < right:
                        chars[left], chars[right] = chars[right], chars[left]
                        left += 1
                        right -= 1
                tmp = read+1
        return res
