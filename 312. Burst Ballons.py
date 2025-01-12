class Solution:
    def maxCoins(self, nums):
        # Add virtual balloons with value 1 at the ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # DP table to store the maximum coins we can collect from i to j
        dp = [[0] * n for _ in range(n)]
        
        # Start with the subproblems of size 2 (i.e., intervals between i and j)
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                # Try bursting each balloon k between i and j
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        
        return dp[0][n - 1]
#  1 3 1 5 8 1 