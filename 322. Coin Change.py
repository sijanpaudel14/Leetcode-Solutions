class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]  # List of coin denominations
        :type amount: int       # Target amount to make
        :rtype: int             # Minimum number of coins required to make the amount, or -1 if not possible
        """
        
        # Step 1: Initialize a DP array to store the minimum coins required for each amount from 0 to `amount`.
        # We use 'infinity' (a very large value) to signify that the amount is initially unreachable.
        dp = [float('inf')] * (amount + 1)

        # Step 2: Base case: To make an amount of 0, 0 coins are required.
        dp[0] = 0

        # Step 3: Iterate through all amounts from 1 to `amount`.
        for a in range(1, amount + 1):
            # Step 4: For each amount `a`, check all coin denominations in the `coins` list.
            for coin in coins:
                # Step 5: If the current coin can be used (i.e., `a - coin` is non-negative),
                # calculate the number of coins needed by considering the current coin.
                if a - coin >= 0:
                    # Update dp[a] to the minimum of its current value and the value of dp[a - coin] + 1.
                    # dp[a - coin] is the minimum coins needed to make amount `a - coin`,
                    # and adding 1 accounts for the current coin.
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        # Step 6: After processing all amounts, check if dp[amount] is still 'infinity'.
        # If it is, it means the amount is not reachable using the given coins, so return -1.
        # Otherwise, return the minimum number of coins required to make the `amount`.
        return dp[amount] if dp[amount] != float('inf') else -1
    
    

# BFS APPROACH
from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0  # Base case: No coins needed for amount 0

        # Initialize a queue for BFS. Each element is (current_amount, steps).
        queue = deque([(0, 0)])
        visited = set()  # Keep track of visited amounts to avoid redundant calculations

        while queue:
            current_amount, steps = queue.popleft()

            # Try all coins
            for coin in coins:
                next_amount = current_amount + coin

                # If the next amount equals the target, return the steps + 1
                if next_amount == amount:
                    return steps + 1

                # If the next amount is valid and hasn't been visited, add it to the queue
                if next_amount < amount and next_amount not in visited:
                    queue.append((next_amount, steps + 1))
                    visited.add(next_amount)

        # If we've exhausted all possibilities, return -1 (not possible to make the amount)
        return -1
