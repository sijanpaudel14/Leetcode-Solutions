class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert binary string to decimal
        def convertToDecimal(num):
            decimal = 0
            length = len(num)
            for i in range(length):
                # Multiply each bit by 2^(position from the right)
                decimal += int(num[i]) * (2 ** (length - i - 1))
            return decimal
        
        # Convert decimal to binary
        def convertToBinary(num):
            if num == 0:
                return "0"
            binary = ""
            while num > 0:
                binary = str(num % 2) + binary  # Prepend the remainder
                num = num // 2
            return binary
        
        # Convert inputs to decimal
        a_decimal = convertToDecimal(a)
        b_decimal = convertToDecimal(b)
        
        # Add the decimal numbers
        sum_decimal = a_decimal + b_decimal
        
        # Convert the sum back to binary
        return convertToBinary(sum_decimal)
