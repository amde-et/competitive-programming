class Solution(object):
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        _, max_count = counter.most_common(1)[0]
        return max((max_count-1) * (n+1) + counter.values().count(max_count), len(tasks))
