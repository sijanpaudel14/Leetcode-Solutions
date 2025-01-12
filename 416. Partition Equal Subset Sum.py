class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)

        # If total sum is odd, partitioning is impossible
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # Initialize DP array
        dp = [False] * (target + 1)
        dp[0] = True  # A sum of 0 can always be achieved

        # Update DP array for each number in `nums`
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        # Return whether target sum is achievable
        return dp[target]
