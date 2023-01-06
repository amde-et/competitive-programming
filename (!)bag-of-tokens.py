class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res, tmp = 0, 0
        L, R = 0, len(tokens)-1
        while L <= R:
            if power >= tokens[L]:
                power -= tokens[L]
                L += 1
                tmp += 1
                res = max(res, tmp)
            elif tmp > 0:
                tmp -= 1
                power += tokens[R]
                R -= 1
            else:
                break
        return res
