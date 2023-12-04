class Solution:
    def kidsWithCandies(self, c: List[int], eC: int) -> List[bool]:
        return [x+eC >= max(c)for x in c]