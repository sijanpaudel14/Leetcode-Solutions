def maxArea(height):
    left, right = 0, len(height) - 1  # Initialize two pointers
    max_area = 0  # To store the maximum area

    while left < right:
        # Calculate the current area
        current_area = min(height[left], height[right]) * (right - left)
        
        # Update max_area if the current area is larger
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1  # Move the left pointer inward
        else:
            right -= 1  # Move the right pointer inward

    return max_area