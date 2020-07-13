class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols_with_zeros = []
        for i in range(0, len(matrix)):
            if 0 in matrix[i]:
                #make the complete row zero
                for j in range(0, len(matrix[i])):
                    #store columns with zero in them
                    if matrix[i][j] == 0:
                        cols_with_zeros.append(j)
                    matrix[i][j] = 0
                    
        #make the columns zero
        for row in range(0, len(matrix)):
            for col in cols_with_zeros:
                matrix[row][col] = 0
