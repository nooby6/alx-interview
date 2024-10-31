#!/usr/bin/python3
"""Contains a method for validating data as UTF-8"""

from typing import List

def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing bytes in the data set.
    
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
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
