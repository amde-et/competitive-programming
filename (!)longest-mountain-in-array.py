class Solution(object):
    def longestMountain(self, arr):
        result, up_len, down_len = 0, 0, 0
        for i in range(1, len(arr)):
            if (down_len and arr[i-1] < arr[i]) or arr[i-1] == arr[i]:
                up_len, down_len = 0, 0
            up_len += arr[i-1] < arr[i]
            down_len += arr[i-1] > arr[i]
            if up_len and down_len:
                result = max(result, up_len+down_len+1)
        return result
