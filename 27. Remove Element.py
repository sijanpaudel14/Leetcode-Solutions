class Solution(object):
    def removeElement(self, nums, val):
        """
        Removes all occurrences of `val` from the array `nums` in-place.
        Returns the number of elements remaining after removal.

        Args:
        nums (List[int]): Input array of integers.
        val (int): The value to be removed.

        Returns:
        int: The number of elements remaining in the array after removal.
        """
        # Pointer to track the next position for valid elements
        j = 0

        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:  # If the current element is not equal to `val`
                nums[j] = nums[i]  # Place the current element at the `j`th position
                j += 1  # Increment `j` to the next position for valid elements

        # Return the count of elements remaining after removal
        return j
