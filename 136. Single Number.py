class Solution:
    def singleNumber(self, nums) :
        """
        Finds the single number that appears only once in an array where all other numbers appear twice.

        Args:
            nums: A list of integers.

        Returns:
            The integer that appears only once.
        """

        # Initialize a variable to store the result
        result = 0

        # Iterate through each number in the list
        for num in nums:
            # XOR the current number with the result
            result ^= num

        # After iterating, the result will contain the single number
        return result