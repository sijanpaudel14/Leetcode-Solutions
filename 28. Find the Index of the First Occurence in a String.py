class Solution(object):
    def strStr(self, haystack, needle):
        """
        Finds the index of the first occurrence of `needle` in `haystack`.
        
        Args:
        haystack (str): The string to search within.
        needle (str): The string to search for.

        Returns:
        int: The index of the first occurrence of `needle` in `haystack`, or -1 if not found.
        """
        # If needle is empty, the first occurrence is at index 0
        if not needle:
            return 0

        # Lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)

        # Loop through the haystack to find the needle
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring of haystack matches the needle
            if haystack[i:i + needle_len] == needle:
                return i  # Return the starting index of the match

        # If no match is found, return -1
        return -1
