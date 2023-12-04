class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ee = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) <= ee:
                return False
        return True