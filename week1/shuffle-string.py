class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string=[""] *len(indices)
        for i in range(len(s)):
                new_string[indices[i]]=s[i]
        ans="".join(new_string)
        return ans


