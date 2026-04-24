class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for rc, cc in directions:
                new_row , new_col = r + rc , c + cc
                dfs(new_row , new_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count