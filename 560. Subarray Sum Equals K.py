class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Use a hashmap (counter) to store the frequency of prefix sums
        counter = {0: 1}  # Initialize with 0 sum for empty subarray
        count = 0         # Count of subarrays with sum equal to k
        currentSum = 0    # Running cumulative sum

        # Step 2: Iterate through the nums array
        for num in nums:
            currentSum += num  # Update the running sum
            
            # Check if (currentSum - k) exists in the counter
            if currentSum - k in counter:
                count += counter[currentSum - k]
            
            # Update the counter for the current cumulative sum
            if currentSum in counter:
                counter[currentSum] += 1
            else:
                counter[currentSum] = 1

        return count
