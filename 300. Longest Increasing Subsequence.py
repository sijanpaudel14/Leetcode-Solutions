class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the input list is empty, there is no increasing subsequence
        if not nums:
            return 0

        # Get the length of the input array
        n = len(nums)

        # Initialize the LIS array where LIS[i] represents
        # the length of the longest increasing subsequence ending at index i.
        LIS = [1] * n

        # Loop through each element of the array to calculate the LIS
        for i in range(n):
            # Check all elements before index i to find potential subsequences
            for j in range(i):
                # If nums[j] < nums[i], it means we can extend the LIS ending at nums[j]
                if nums[j] < nums[i]:
                    # Update LIS[i] to the maximum length by including nums[i]
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        # The longest increasing subsequence will be the maximum value in the LIS array
        # because it stores the LIS for every index.
        return max(LIS)


import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # List to store the smallest tail of all increasing subsequences
        sub = []
        
        # Iterate through each number in the array
        for num in nums:
            # Find the position to replace or append using binary search
            pos = bisect.bisect_left(sub, num)
            
            # If pos is equal to the length of sub, append the number
            if pos == len(sub):
                sub.append(num)
            else:
                # Otherwise, replace the number at position 'pos'
                sub[pos] = num
        
        # The length of the 'sub' list is the length of the LIS
        return len(sub)


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(sub, target):
            """
            Perform binary search to find the first position in `sub`
            where the value is greater than or equal to `target`.
            """
            left, right = 0, len(sub) - 1
            while left <= right:
                mid = (left + right) // 2
                if sub[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # Initialize an empty list to represent the LIS tail values
        sub = []

        # Iterate through each number in the input array
        for num in nums:
            # Find the position to insert or replace using binary search
            pos = binary_search(sub, num)
            
            # If `pos` is equal to the length of `sub`, append `num` (extend LIS)
            if pos == len(sub):
                sub.append(num)
            else:
                # Otherwise, replace the value at position `pos`
                sub[pos] = num

        # The length of `sub` is the length of the LIS
        return len(sub)
