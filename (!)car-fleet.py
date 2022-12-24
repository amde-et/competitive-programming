class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        result, tmp = 0, 0
        for t in reversed(times):
            if t > tmp:
                result += 1
                tmp = t
        return result
