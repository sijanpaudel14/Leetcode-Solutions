class Solution(object):
    def numIslands(self, grid):
        """
        Count the number of islands in the given 2D grid.
        
        :param grid: List[List[str]] - 2D grid where '1' represents land and '0' represents water
        :return: int - number of islands
        """
        # Step 1: Validate the input grid
        if not grid or not grid[0]:  # Check if the grid is non-empty
            return 0
        
        # Step 2: Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Step 3: Initialize a counter for the number of islands
        num_islands = 0

        # Step 4: Define a DFS helper function to explore an island
        def dfs(r, c):
            """
            Perform DFS to mark all connected land cells ('1') as visited.
            
            :param r: int - current row
            :param c: int - current column
            """
            # Base case: If out of bounds or the cell is water ('0'), stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current cell as visited by changing '1' to '0'
            grid[r][c] = '0'
            
            # Recur for all four adjacent cells
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Step 5: Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ('1'), it's a new island
                if grid[r][c] == '1':
                    num_islands += 1  # Increment the island counter
                    dfs(r, c)  # Perform DFS to mark the entire island as visited

        # Step 6: Return the total number of islands
        return num_islands
