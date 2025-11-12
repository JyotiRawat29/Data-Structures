"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
#%%
def minPathSum(grid):
    m = len(grid) #rows
    n = len(grid[0]) #columns
    for i in range(1,n):
        grid[0][i] += grid[0][i-1]
    for j in range(1,m):
        grid[j][0] += grid[j-1][0]
    for i in range(1,m):
        for j in range(1,n):
            grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
            print(min(grid[i-1][j],grid[i][j-1]))
            print(f'(i is {i} j is {j} grid is {grid[i][j]})')
    print(grid)
    return grid[m-1][n-1] 

minPathSum([[1,2,3],[4,5,6]])

