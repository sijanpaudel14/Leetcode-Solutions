class Solution:
    # Function to reverse the bits of a 32-bit unsigned integer
    def reverseBits(self, n: int) -> int:
        res = 0  # Initialize the result to 0
        for i in range(32):  # Loop through all 32 bits
            # Extract the least significant bit (LSB) of 'n'
            bit = n & 1  
            
            # Shift 'res' to the left by 1 to make space for the new bit
            res = res << 1  
            
            # Add the extracted bit to 'res'
            res += bit  
            
            # Shift 'n' to the right by 1 to process the next bit
            n = n >> 1  
            
            # Print the intermediate steps (optional for debugging)
            # print(f"Step {i + 1}: res = {bin(res)[2:].zfill(32)}, n = {bin(n)[2:].zfill(32)}")
        
        return res  # Return the reversed bits as an integer
