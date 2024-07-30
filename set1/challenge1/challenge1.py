# Author  : Andrew Paiva
# Date    : 07/23/2024
# Purpose : Convert hexadecimal to base64

# Process is as follows: 

# def hex_to_base64(hex_string):

#     for digit in hex_string:
#         if digit.upper() not in '0123456789ABCDEF':
#             return 'Invalid hex string'
#         else: 
#             pass

#     #convert hex string to binary string
#     binary_string = ''
#     for digit in hex_string:
#         binary_string += bin(int(digit, 16))[2:].zfill(4)

#     #pad binary string to make its length | 6
#     len_binary = len(binary_string)
#     padding = len_binary % 6
#     if padding:
#         binary_string = binary_string + '0' * (6 - padding)

#     #print(binary_string)

    

#     #convert binary string to base64
#     base64_string = ''
#     base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#     for i in range(0, len(binary_string), 6):
#         six_bit_chunk = binary_string[i:i+6]
#         #print(six_bit_chunk)
#         decimal_value = int(six_bit_chunk, 2)
#         #print(decimal_value)
#         base64_string += base64_chars[decimal_value]
#         #print(base64_string)

#     # Add padding, if neccecary
#     padding = len(hex_string) % 3
#     if padding:
#         base64_string += '=' * padding
#         #if padding is 1, add 2 '=', if padding is 2, add 1 '='

#     return base64_string

#user_input = input ("Enter a hexadecimal string: ")
#print(hex_to_base64(user_input))

import base64

# Convert hex string to bytes and convering bytes to base64
def hex_to_base64(hex_string):
    for digit in hex_string:
        if digit.upper() not in '0123456789ABCDEF':
            return 'Invalid hex string'
        else: 
            pass

    # Ensure the hex string has an even number of digits
    if len(hex_string) == 1:
        hex_string = '0' + hex_string

    #convert hex string to bytes
    byte_string = bytes.fromhex(hex_string)

    #convert bytes to base64
    base64_string = base64.b64encode(byte_string)

    return base64_string.decode()