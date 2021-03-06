import numpy as np
import sys
import queue


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        r = len(grid)
        c = len(grid[0])
        arr = [[sys.maxsize for x in range(c)] for y in range(r)]
        q = queue.Queue()
        q.put([0, 0])
        arr[0][0] = grid[0][0]
        while q.qsize() > 0:
            p = q.get()
            if p[0] > len(grid)-1 and p[1] > len(grid[0])-1:
                break
            visit(grid, arr, q, p[0], p[1]+1, p)

            visit(grid, arr, q, p[0]+1, p[1], p)

        print(arr)
        return arr[r-1][c-1]


def visit(grid, arr, q, x, y, p):
    if x > len(grid)-1 or y > len(grid[0])-1:
        return
    if arr[x][y] > grid[x][y]+arr[p[0]][p[1]]:
        arr[x][y] = grid[x][y]+arr[p[0]][p[1]]
        q.put([x, y])
