class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the last digit of the array (least significant digit)
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, simply increment it
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry-over needed; return the result
            
            # If the current digit is 9, set it to 0 (carry over)
            digits[i] = 0
        
        # If the loop completes, all digits were 9 (e.g., 999 -> 1000)
        # Add 1 at the beginning to handle the carry
        return [1] + digits


#My solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Initialize an empty string to store the concatenated digits
        concatenated_number = ""
        # Initialize an empty list to store the result
        result = []
        
        # Loop through each digit in the input list
        for i in range(len(digits)):
            # Convert each digit to a string and concatenate it
            concatenated_number += str(digits[i])
        
        # Convert the concatenated string back to an integer and add 1
        incremented_number = str(int(concatenated_number) + 1)
        
        # Convert the result back to a list of digits
        for digit in incremented_number:
            result.append(int(digit))

        # Return the result as a list of digits
        return result
