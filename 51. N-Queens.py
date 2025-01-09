class Solution:
    def solveNQueens(self, n):
        # Initialize sets to track columns, positive diagonals (r + c), and negative diagonals (r - c)
        col = set()  # Columns under attack
        posDiag = set()  # Positive diagonals under attack (r + c)
        negDiag = set()  # Negative diagonals under attack (r - c)

        res = []  # To store the final list of solutions
        # Initialize the board with '.' representing empty spots
        board = [["." for _ in range(n)] for _ in range(n)]

        # Helper function to perform backtracking and solve the problem
        def backtrack(r):
            # If all rows are processed, add the current board configuration to the result
            if r == n:
                # Convert the board to a list of strings and append to the result
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try placing a queen in each column of the current row
            for c in range(n):
                # If the column or the diagonals are under attack, skip the current position
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Mark the current column and diagonals as attacked
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # Place the queen in the current position
                board[r][c] = "Q"

                # Recurse to the next row
                backtrack(r + 1)

                # Backtrack: Remove the queen and unmark the attacked positions
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        # Start backtracking from row 0
        backtrack(0)

        # Return the list of all valid board configurations
        return res
