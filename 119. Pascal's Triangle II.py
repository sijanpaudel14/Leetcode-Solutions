class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_row = [1]  # Start with the 0th row
        
        for row_num in range(1, rowIndex + 1):
            # Create the current row based on the previous row 
            curr_row = [1] * (row_num + 1)
            for j in range(1, row_num):
                curr_row[j] = prev_row[j - 1] + prev_row[j]
            
            # Update previous row to the current row
            prev_row = curr_row
        
        return prev_row
