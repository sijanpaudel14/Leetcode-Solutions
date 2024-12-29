class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_num(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total

        slow = n  
        fast = get_num(n)  

        while slow != fast:  
            slow = get_num(slow)  
            fast = get_num(get_num(fast))  

        return slow == 1  
