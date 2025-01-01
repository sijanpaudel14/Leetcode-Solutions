def largestRectangleArea(height):
    # Append a 0 to the end of the height list to ensure that all remaining elements
    # in the stack will be processed at the end of the loop.
    height.append(0)

    # Initialize an empty stack with -1. The stack will store the indices of the bars
    # in a way that ensures the bars in the stack are in non-decreasing order of height.
    stack = [-1]

    # Initialize the answer to store the maximum area found so far.
    ans = 0

    # Iterate over each bar in the height list (including the extra 0 added).
    for i in range(len(height)):  # Use `range(len(height))` instead of `xrange` in Python 3
        # While the current bar is shorter than the bar at the top of the stack,
        # calculate the area of the rectangle formed by the bar at the top of the stack.
        while height[i] < height[stack[-1]]:
            # Pop the top element from the stack. This is the height of the rectangle.
            h = height[stack.pop()]

            # Calculate the width of the rectangle. The width is determined by the current index `i`
            # and the new top of the stack, which represents the index of the last smaller bar.
            w = i - stack[-1] - 1

            # Update the answer with the maximum area found so far.
            ans = max(ans, h * w)

        # Push the current index onto the stack.
        # This is to maintain the non-decreasing order of heights in the stack.
        stack.append(i)

    # Remove the extra 0 appended to the height list at the beginning.
    height.pop()

    # Return the maximum area found.
    return ans
