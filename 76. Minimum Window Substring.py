class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):  # If s is smaller than t, no valid window can exist
            return ""

        # Initialize frequency maps for t and the current window
        t_freq = {}
        for char in t:  # Create frequency map for characters in t
            t_freq[char] = t_freq.get(char, 0) + 1

        window_freq = {}  # Frequency map for the current window in s
        start = 0  # Start of the sliding window
        end = 0  # End of the sliding window
        required_chars = len(t_freq)  # Number of unique characters we need to match
        min_len = float('inf')  # Start with an infinite minimum length
        min_window = ""  # Store the result for the smallest window found

        while end < len(s):
            # Expand the window by adding s[end]
            char_end = s[end]
            window_freq[char_end] = window_freq.get(char_end, 0) + 1

            # If char_end matches the frequency in t, reduce required_chars
            if char_end in t_freq and window_freq[char_end] == t_freq[char_end]:
                required_chars -= 1

            # Shrink the window when all required characters are matched
            while required_chars == 0:
                window_len = end - start + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[start:end + 1]

                # Shrink the window by moving start
                char_start = s[start]
                window_freq[char_start] -= 1
                if char_start in t_freq and window_freq[char_start] < t_freq[char_start]:
                    required_chars += 1

                start += 1  # Move the start of the window forward

            # Expand the window by moving end
            end += 1

        return min_window  # Return the smallest valid window found
