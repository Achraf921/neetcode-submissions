class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cops = [row[:] for row in matrix] 
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num ==0:
                    # we want to set the whole row and the column to 0s
                    # row:
                    for k in range(len(matrix[0])):
                        cops[i][k]=0
                    # col:
                    for w in range(len(matrix)):
                        cops[w][j]=0
        matrix[:]=cops
        
        # O(n^2) time O(n^2) space
        
        