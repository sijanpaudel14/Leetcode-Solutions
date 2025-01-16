class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Finds the length of the last word in the string `s`.

        Args:
        s (str): Input string.

        Returns:
        int: Length of the last word in the string.
        """
        # Strip any trailing spaces to avoid counting extra spaces
        s = s.strip()

        # Split the string into words using default whitespace delimiter
        words = s.split()

        # Return the length of the last word
        return len(words[-1])
