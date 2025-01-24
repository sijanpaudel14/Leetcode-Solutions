class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for zero-based indexing
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            columnNumber //= 26

        # Since we build the title from the least significant to the most significant, reverse it
        return ''.join(result[::-1])
