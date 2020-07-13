class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mirror(matrix)


def mirror(mat):
        n = len(mat)
        #create a mirror image from the diagonal
        for i in range(0, n):
            for j in range(0, n):
                if j > i:
                    swp_1 = mat[i][j]
                    swp_2 = mat[j][i]
                    mat[i][j] = swp_2
                    mat[j][i] = swp_1
        #reverse each array
        for i in range(0, n):
            mat[i].reverse()

        return mat
