class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize pointers for the search space
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # Check if the target is at the mid index
            if nums[mid] == target:
                return mid  # Target found, return its index
            
            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Narrow the search to the left half
                else:
                    left = mid + 1  # Narrow the search to the right half
            else:
                # Otherwise, the right half must be sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Narrow the search to the right half
                else:
                    right = mid - 1  # Narrow the search to the left half
        
        # If the loop ends, the target is not in the array
        return -1
