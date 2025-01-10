class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If the number of steps is 1 or 2, the number of ways to climb is equal to 'n'
        if n <= 2: 
            return n

        # Initialize a DP array of size n+1 to store the number of ways to climb to each step
        dp = [0] * (n + 1)

        # Base cases:
        # There is 1 way to climb 1 step: [1]
        dp[1] = 1  
        # There are 2 ways to climb 2 steps: [1,1], [2]
        dp[2] = 2  

        # Fill the DP array for steps 3 through n
        # The number of ways to reach step i is the sum of ways to reach (i-1) and (i-2)
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the number of ways to climb n steps
        return dp[n]
