class Solution(object):
    def topKFrequent(self, nums, k):
        return [key for key, _ in collections.Counter(nums).most_common(k)]
        
