from challenge3 import singe_byte_xor_cipher

def detect_single_character_xor():
    #open the file
    with open('encoded_strings.txt', 'r') as file:
        encoded_strings = file.read().splitlines()
        

    list_of_decoded_strings = []
    #iterate through all the encoded strings
    for encoded_string in encoded_strings:
        #decode the string
        decoded_string = singe_byte_xor_cipher(encoded_string)
        list_of_decoded_strings.append(decoded_string)
    #calculate the score of the decoded string
    common_chars = '/[ETAOINSHRDLU] etaoinsrhdlu'
    decoded_scores = []
    for decoded_string in list_of_decoded_strings:
        decoded_scores.append((decoded_string, sum(decoded_string.count(c) for c in common_chars)))

    #sort the decoded strings by the score
    decoded_scores.sort(key=lambda x: x[1], reverse=True)
    return decoded_scores[0]


print(detect_single_character_xor())
