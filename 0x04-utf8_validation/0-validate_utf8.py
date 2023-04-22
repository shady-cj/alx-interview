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
        four_bits = entry & 240
        three_bits = entry & 224
        two_bits = entry & 192
        first_bit = entry & 128
        second_bit = entry & 64
        if no_of_bytes == 0:
            if four_bits == 240:
                no_of_bytes = 4
            elif three_bits == 224:
                no_of_bytes = 3
            elif two_bits == 192:
                no_of_bytes = 2
            elif first_bit == 0:
                continue
            else:
                return False
        else:
            if first_bit == 128 and second_bit == 0:
                no_of_bytes -= 1
                continue
            else:
                return False
    return True
