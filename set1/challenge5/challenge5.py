def repeating_key_xor(string, key):

    encrypted_msg = []
    i = 0
    for char in string:
        encrypted_msg.append(ord(char) ^ ord(key[i]))
        i += 1
        if i == len(key):
            i = 0
    encrypted_msg = bytes(encrypted_msg)
    return encrypted_msg.hex()


message_input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key_input = "ICE"
print(repeating_key_xor(message_input, key_input))