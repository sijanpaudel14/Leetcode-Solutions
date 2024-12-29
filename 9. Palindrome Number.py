class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        pali = x
        total = 0
        while(x>0):
            digit = x % 10
            total = 10 * total + digit
            x//=10
        return(total == pali)

        