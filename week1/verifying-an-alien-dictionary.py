class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapper = {chr(i):-1 for i in range(97,97+26)}
        def map_value():
            nonlocal order
            nonlocal mapper
            for i in range(len(order)):
                mapper[order[i]] = i
        map_value()
        def helper():
            for i in range(len(words)-1):
                if len(words[i+1])<len(words[i]) and mapper[words[i+1][0]] <= mapper[words[i][0]] and words[i+1] in words[i]:
                    return False
                else:
                    for j in range(min(len(words[i]), len(words[i+1]))):
                        if words[i][j] != words[i+1][j]:
                            if mapper[words[i+1][j]] < mapper[words[i][j]]:
                                return False
                            break
            return True
        return helper()