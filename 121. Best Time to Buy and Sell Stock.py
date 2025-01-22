class Solution:
    def maxProfit(self, prices):
        if not prices:  # If there are no prices, return 0 profit
            return 0
        
        min_price = float('inf')  # Start with a very high number
        max_profit = 0  # Start with 0 profit
        
        for price in prices:
            # Update the minimum price found so far
            if price < min_price:
                min_price = price
            # Update the maximum profit if we can make more profit by selling at current price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit  # Return the maximum profit


# Using Dynamic Programming
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        # DP array to track maximum profit at each day
        dp = [0] * len(prices)
        
        # The min price up to that point
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            # Update the min price
            min_price = min(min_price, prices[i])
            
            # Maximum profit if sold at prices[i]
            dp[i] = max(dp[i-1], prices[i] - min_price)
        
        return dp[-1]  # Maximum profit up to the last day
