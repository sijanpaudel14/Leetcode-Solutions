class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if a given string is a palindrome, considering only alphanumeric characters and ignoring case.

        Args:
            s: The input string.

        Returns:
            True if the string is a palindrome, False otherwise.
        """

        # 1. Clean the string: Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(char for char in s if char.isalnum()).lower()

        # 2. Base case: An empty string is considered a palindrome
        if not s:
            return True

        # 3. Initialize pointers: 
        #    - 'i' at the beginning of the string
        #    - 'j' at the end of the string
        i = 0
        j = len(s) - 1

        # 4. Two-pointer approach: 
        #    - Iterate while the starting pointer ('i') is before the ending pointer ('j')
        while i < j:
            # 5. Check if characters at 'i' and 'j' are equal
            if s[i] != s[j]:
                return False  # Not a palindrome

            # 6. Move pointers inwards
            i += 1
            j -= 1

        # 6. If the loop completes without finding any mismatches, it's a palindrome
        return True