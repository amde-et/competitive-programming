class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d=0
        ord=[]
        result=[]
        for point in points:
            d=sqrt(point[0]**2 + point[1]**2)
            point.insert(0,d)
            ord.append(point)
        ord=sorted(ord)
        for i in range(k):
            result.append(ord[i][1:])
        return result
