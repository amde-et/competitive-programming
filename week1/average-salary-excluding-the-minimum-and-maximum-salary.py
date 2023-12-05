class Solution:
    def average(self, salary: List[int]) -> float:
        avg,mn,mx,n = 0,salary[0],salary[0],len(salary)

        for i,sal in enumerate(salary):
            avg += (sal - avg)/(i+1)
            mn = min(mn,sal)
            mx = max(mx,sal)

        # print(avg)
        avg += (avg - mx)/(n-1)
        avg += (avg - mn)/(n-2)
        return avg