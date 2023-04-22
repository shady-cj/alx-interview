#!/usr/bin/python3
"""
Contains a method that determines if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    no_of_bytes = 0

    for entry in data:
        bitmask = 128

        if no_of_bytes == 0:
            while (entry & bitmask):
                no_of_bytes += 1
                bitmask >>= 1
            if no_of_bytes == 1 or no_of_bytes > 4:
                return False
        else:
            if (entry & bitmask) == 128 and (entry & bitmask) == 0:
                no_of_bytes -= 1
                continue
            else:
                return False
    if no_of_bytes == 0:
        return True        
    return False
