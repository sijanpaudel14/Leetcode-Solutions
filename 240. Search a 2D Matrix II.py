class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Initialize the starting point (top-right corner)
        row, col = 0, len(matrix[0]) - 1
        
        # Iterate through the matrix while within bounds
        while row < len(matrix) and col >= 0: 
            if matrix[row][col] == target:
                return True  # Target found
            elif matrix[row][col] > target:
                col -= 1  # Move left if current element is greater than target
            else:
                row += 1  # Move down if current element is less than target
        
        # If the loop exits, target is not found
        return False
