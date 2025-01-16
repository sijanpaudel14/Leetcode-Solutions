
class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted array in-place and returns the number of unique elements.
        
        Args:
        nums (List[int]): A sorted list of integers.

        Returns:
        int: The count of unique elements in the array after removing duplicates.
        """
        # Handle edge case: if the array is empty, return 0
        if not nums:
            return 0

        # Initialize the pointer for the next unique position
        j = 0  # Points to the last unique element

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not equal to the last unique element
            if nums[i] != nums[j]:
                j += 1  # Move to the next position for a unique element
                nums[j] = nums[i]  # Update the unique position with the new unique element

        # The number of unique elements is the index of the last unique element + 1
        return j + 1
