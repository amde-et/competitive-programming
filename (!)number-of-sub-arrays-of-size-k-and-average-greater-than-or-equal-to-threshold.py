class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        result, curr = 0, sum(itertools.islice(arr, 0, k-1))
        for i in range(k-1, len(arr)):
            curr += arr[i]-(arr[i-k] if i-k >= 0 else 0)
            result += int(curr >= threshold*k)
        return result
