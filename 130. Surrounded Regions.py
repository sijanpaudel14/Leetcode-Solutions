class Solution(object):
    def solve(self, board):
        """
        Modify the board in-place to capture all surrounded regions.
        
        :param board: List[List[str]] - 2D grid of 'X' and 'O'
        :return: None (in-place modification)
        """
        # Step 1: Validate input
        if not board or not board[0]:  # Ensure the board is non-empty
            return
        
        # Step 2: Get the dimensions of the board
        rows, cols = len(board), len(board[0])

        # Step 3: Define a DFS helper function to mark boundary-connected 'O's
        def dfs(r, c):
            """
            Perform DFS to mark all 'O's connected to the boundary as non-capturable.
            
            :param r: int - current row
            :param c: int - current column
            """
            # Base case: If out of bounds or the cell is not 'O', stop
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark the current 'O' as non-capturable (e.g., change it to 'E')
            board[r][c] = 'E'

            # Recur for all four adjacent cells
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Step 4: Mark all boundary-connected 'O's as non-capturable
        for r in range(rows):
            for c in range(cols):
                # Check the first and last columns of each row
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == 'O':
                        dfs(r, c)

        # Step 5: Traverse the board to update cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':  # Capturable 'O', flip to 'X'
                    board[r][c] = 'X'
                elif board[r][c] == 'E':  # Non-capturable 'O', restore to 'O'
                    board[r][c] = 'O'
