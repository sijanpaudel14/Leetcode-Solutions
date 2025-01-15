class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]  # Sorted array of integers
        :type target: int  # Target integer to search for or insert
        :rtype: int  # Index at which the target should be inserted or found
        """
        # Initialize the left and right pointers to the start and end of the array
        left = 0
        right = len(nums) - 1
        
        # Perform binary search until the left pointer crosses the right pointer
        while left <= right:
            # Calculate the mid index between left and right
            mid = (left + right) // 2
            
            # Check if the target is found at the mid index
            if target == nums[mid]:
                return mid  # Return the index of the target if found
            # If target is smaller than the middle element, move the right pointer
            elif target < nums[mid]:
                right = mid - 1  # Search the left half
            # If target is larger than the middle element, move the left pointer
            else:
                left = mid + 1  # Search the right half
        
        # If the target is not found, return the left pointer
        # The left pointer will be at the index where the target should be inserted
        return left