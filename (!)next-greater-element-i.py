class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk, lookup = [], {}
        for num in nums2:
            while stk and num > stk[-1]:
                lookup[stk.pop()] = num
            stk.append(num)
        while stk:
            lookup[stk.pop()] = -1
        return map(lambda x : lookup[x], nums1)
