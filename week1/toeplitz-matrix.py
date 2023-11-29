class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        flag = False
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    flag = True
                    break
        return flag==False