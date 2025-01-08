class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        Perform a flood fill on a 2D image starting from (sr, sc).
        
        :param image: List[List[int]] - 2D grid representing the image
        :param sr: int - starting row
        :param sc: int - starting column
        :param color: int - target color to fill
        :return: List[List[int]] - updated image after flood fill
        """
        # Step 1: Validate input
        if not image or not image[0]:  # Check if the image is non-empty
            return image
        
        # Step 2: Get the initial color of the starting pixel
        initial_color = image[sr][sc]
        
        # If the initial color is the same as the target color, no changes are needed
        if initial_color == color:
            return image

        # Step 3: Define the grid dimensions
        rows, cols = len(image), len(image[0])

        # Step 4: Define a DFS helper function to fill the connected components
        def dfs(r, c):
            """
            Recursively fill the image using depth-first search.
            
            :param r: int - current row
            :param c: int - current column
            """
            # Check boundaries and ensure the current pixel matches the initial color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != initial_color:
                return
            
            # Update the current pixel to the target color
            image[r][c] = color

            # Recur for all four directions: down, up, right, left
            dfs(r + 1, c)  # Move down
            dfs(r - 1, c)  # Move up
            dfs(r, c + 1)  # Move right
            dfs(r, c - 1)  # Move left

        # Step 5: Start the flood fill from the given starting point (sr, sc)
        dfs(sr, sc)

        # Step 6: Return the updated image
        return image
