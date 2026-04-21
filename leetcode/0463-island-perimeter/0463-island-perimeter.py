class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(0,1), (0,-1),(1,0), (-1,0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row , col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row,col):
            if not  inbound(row,col):
                return 1
            if grid[row][col] ==0:
                return 1
            if visited[row][col]:
                return 0
            visited[row][col] = True
            perimeter = 0 
            for r_c , c_c in direction:
                new_row = row + r_c
                new_col = col + c_c
                perimeter += dfs(new_row,new_col)
            return perimeter
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)