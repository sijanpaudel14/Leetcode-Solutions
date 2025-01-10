class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Get the length of the input strings
        m, n = len(text1), len(text2)
        
        # Initialize a 2D DP array with 0s
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Iterate over the characters of the first string
        for i in range(1, m + 1):
            # Iterate over the characters of the second string
            for j in range(1, n + 1):
                # If the characters match, increment the LCS length
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # Otherwise, take the maximum of the previous LCS lengths
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Return the LCS length of the two strings
        return dp[m][n]
