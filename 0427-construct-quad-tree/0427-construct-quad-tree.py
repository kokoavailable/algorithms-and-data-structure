"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.constructQuadTree(grid, 0, 0, len(grid))

    def constructQuadTree(self,grid, x, y, size):
        if self.isAllSame(grid, x, y, size):
            return Node(grid[x][y] == 1, True)

        newSize = size // 2
        topLeft = self.constructQuadTree(grid, x, y, newSize)
        topRight = self.constructQuadTree(grid, x, y + newSize, newSize)
        bottomLeft = self.constructQuadTree(grid, x + newSize, y, newSize)
        bottomRight = self.constructQuadTree(grid, x + newSize, y + newSize, newSize)

        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

    def isAllSame(self, grid, x, y, size):
        val = grid[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if grid[i][j] != val:
                    return False
        return True
        