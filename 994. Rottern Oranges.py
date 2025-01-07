"""
Algorithm: 

Initialization:
Count the number of fresh oranges (fresh) in the grid.
Add all initially rotten oranges' positions to a queue (q) for BFS processing.

BFS for Rot Propagation:
Process the rotten oranges in the queue level by level (minute by minute).
For each rotten orange, check its 4 adjacent cells (right, left, down, up):
If an adjacent cell contains a fresh orange, mark it as rotten, decrement the fresh count, and add its position to the queue.

Time Tracking:
Increment the time variable after processing all rotten oranges at the current level.
Continue until there are no fresh oranges left or the queue becomes empty.

Result:
If all fresh oranges are rotten (fresh == 0), return the total time taken.
If there are still fresh oranges remaining after BFS, return -1 (not all oranges can be rotten).

"""




from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Initialize a queue to keep track of rotten oranges
        q = deque()
        time, fresh = 0, 0  # `time` tracks minutes passed; `fresh` counts fresh oranges
        
        # Get the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # Traverse the grid to count fresh oranges and add rotten oranges to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:  # Fresh orange
                    fresh += 1
                if grid[r][c] == 2:  # Rotten orange
                    q.append([r, c])
        
        # Define the directions for adjacent cells (right, left, down, up)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # Perform Breadth-First Search (BFS) to propagate the rotting process
        while q and fresh > 0:
            # Process all rotten oranges in the queue for the current minute
            for i in range(len(q)):
                r, c = q.popleft()
                # Check all adjacent cells
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # If the adjacent cell is out of bounds or not a fresh orange, skip it
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    # Mark the fresh orange as rotten
                    grid[row][col] = 2
                    # Add it to the queue for processing in the next minute
                    q.append([row, col])
                    # Decrease the count of fresh oranges
                    fresh -= 1
            # Increment the time after processing all current rotten oranges
            time += 1
        
        # If there are no fresh oranges left, return the time taken; otherwise, return -1
        return time if fresh == 0 else -1

