class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        return [arr[right] ^ arr[left-1] if left else arr[right] for left, right in queries]
