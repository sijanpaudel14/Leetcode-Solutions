class Solution:
    def titleToNumber(self, columnTitle):
        result = 0
        
        # Iterate over each character in the string
        for char in columnTitle:
            # Update the result by multiplying by 26 (shifting the number)
            # and adding the current character's value ('A' = 1, 'B' = 2, ..., 'Z' = 26)
            result = result * 26 + (ord(char) - ord('A') + 1)
        
        return result
