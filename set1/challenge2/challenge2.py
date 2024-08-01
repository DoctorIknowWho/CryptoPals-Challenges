# Write a function that takes two equal-length buffers
# and produces their XOR combination.

def fixed_xor(buffer1, buffer2):
    #convert inputs to bytes if they are hex strings
    if isinstance(buffer1, str):
        buffer1 = bytes.fromhex(buffer1)
    if isinstance(buffer2, str):
        buffer2 = bytes.fromhex(buffer2)

    #check for equal length buffers
    if len(buffer1) != len(buffer2):
        raise ValueError("Buffers must be of equal length")
    

    #XOR the the buffers
    xored = bytearray()
    for byte1, byte2 in zip(buffer1, buffer2):
        xored_byte = byte1 ^ byte2
        xored.append(xored_byte)

    xored = bytes(xored)

    hex_xored = xored.hex()

    return hex_xored

#user_input = input("Enter a string: ")
#user_input2 = input("Enter another string: ")
#print(fixed_xor(user_input, user_input2))