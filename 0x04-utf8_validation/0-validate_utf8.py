#!/usr/bin/python3
"""
Function to validate if a given data set is valid UTF-8 encoding.
"""

def validUTF8(data):
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7      # 10000000
    mask2 = 1 << 6      # 01000000

    for byte in data:
        # Mask to keep only the 8 least significant bits
        byte &= 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue  # 1-byte character (ASCII)
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1  # 2-byte character
            elif (byte & (mask1 >> 2)) == (mask1 | mask2):
                num_bytes = 2  # 3-byte character
            elif (byte & (mask1 >> 3)) == (mask1 | mask2 | (mask1 >> 2)):
                num_bytes = 3  # 4-byte character
            else:
                return False
        else:
            # Check if byte is a continuation byte (10xxxxxx)
            if (byte & mask1) != mask1 or (byte & mask2) == 0:
                return False
            num_bytes -= 1

    return num_bytes == 0

