class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right element, the minimum is to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is in the left half or at mid
                right = mid
        
        # When the loop ends, left == right and pointing to the minimum element
        return nums[left]
