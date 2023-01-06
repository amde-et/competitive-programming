class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        result, i = 0, 0
        for j, v in enumerate(fruits):
            count[v] += 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            result = max(result, j-i+1)
        return result
