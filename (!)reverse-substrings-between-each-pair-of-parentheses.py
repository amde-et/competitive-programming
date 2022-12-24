class Solution(object):
    def reverseParentheses(self, s):
        tmp,lookup = [],{}
        for i,c in enumerate(s):
            if c == '(':
                tmp.append(i)
            elif c == ')':
                j = tmp.pop()
                lookup[i], lookup[j] = j, i
        result = []
        i, d = 0, 1
        while i < len(s):
            if i in lookup:
                i = lookup[i]
                d *= -1
            else:
                result.append(s[i])
            i += d
        return ''.join(result)
