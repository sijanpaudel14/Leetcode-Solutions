class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        prev_row = []
        
        for row_num in range(numRows):
            # Create a new row with 1 at the start and end
            curr_row = [1] * (row_num + 1)
            
            # Fill the inner elements of the row
            for j in range(1, row_num):
                curr_row[j] = prev_row[j - 1] + prev_row[j]
            
            # Add the current row to the triangle
            triangle.append(curr_row)
            prev_row = curr_row  # Update previous row
        
        return triangle
