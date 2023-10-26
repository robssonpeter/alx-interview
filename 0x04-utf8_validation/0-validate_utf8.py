#!/usr/bin/python3
""" The function that is going to determin valid utf-8 characters """


def validUTF8(data):
    """ Number of expected continuation bytes """
    num_bytes_to_follow = 0

    """ Iterate through each integer in the data list """
    for byte in data:
        """ Ensure that only the 8 least significant bits are considered """
        byte = byte & 0xFF

        """ If we are expecting continuation bytes """
        if num_bytes_to_follow > 0:
            """ Check if the byte is a valid
            continuation byte (starts with "10") """
            if (byte >> 6) != 0b10:
                return False
            """ Decrement the number of expected continuation bytes """
            num_bytes_to_follow -= 1
        else:
            """ Determine the number of bytes in the UTF-8 character """
            if (byte >> 7) == 0b0:
                num_bytes_to_follow = 0
            elif (byte >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False  # Invalid UTF-8 start byte

    """ If we have any remaining continuation bytes, it's not valid UTF-8 """
    return num_bytes_to_follow == 0
