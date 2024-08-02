import base64
from itertools import combinations, zip_longest

def break_repeating_xor_cipher(encrypted_msg):


    #convert hex string to bytes
    bytestring = base64.b64decode(encrypted_msg)

    #find key length
    key_length = find_key_length(bytestring)

    return find_key(key_length, bytestring)



def compute_hamming_distance(s1, s2):

    
    if isinstance(s1, str) and isinstance(s2, str):

        #convert to hex strings
        hex_string1 = s1.encode().hex()
        hex_string2 = s2.encode().hex()

        #convert hex strings to bytes
        byte_string1 = bytes.fromhex(hex_string1)
        byte_string2 = bytes.fromhex(hex_string2)

    elif isinstance(s1, bytes) and isinstance(s2, bytes):
        byte_string1 = s1
        byte_string2 = s2


    #initialize variables
    hamming_distance = 0

    #XOR the the buffers
    xored = bytearray()
    for byte1, byte2 in zip(byte_string1, byte_string2):
        xored_byte = byte1 ^ byte2
        xored.append(xored_byte)

    xored = bytes(xored)

    #calculate the hamming distance
    for byte in xored:
        hamming_distance += bin(byte).count('1')

    return hamming_distance

def find_key_length(bytestring):
    #searching for length that produces lowest hamming distance

    min_score = len(bytestring)

    for keysize in range(2,40):
        chunks = [bytestring[i:i+keysize] for i in range(0, len(bytestring), keysize)] #divide string into chunks of size KEYSIZE
        subgroup = chunks[:4]
        average_score = (sum(compute_hamming_distance(a, b) for a,b in combinations(subgroup, 2)) / 6) / keysize

        if average_score < min_score:
            min_score = average_score
            key_length = keysize

    return key_length

def find_key(key_length, bytestring):
    key_blocks = [bytestring[start:start + key_length] for start in range(0, len(bytestring), key_length)]

    #the nth character of each chunk will result in a list of 
    #characters encrypted with a single byte XOR cipher, whose key is the nth character
    # of our repeating key

    key = []
    single_XOR_blocks = [list(filter(None, i)) for i in zip_longest(*key_blocks)]
    for block in single_XOR_blocks:
        #convert list of bytes to hex string
        block = ''.join([chr(c) for c in block])
        #find the key for the block
        key_n = (singe_byte_xor_cipher(block))
        key.append(key_n)

    ascii_key = ''.join([chr(c) for c in key])
    return ascii_key

def singe_byte_xor_cipher(hex_encoded_string):
    #convert hex string to bytes
    
	bytestring = bytes.fromhex(hex_encoded_string)

	#initialize variables
	decoded_string = '' #to store the decoded string
	decoded_scores = [] #to store the scores of the decoded strings
	key = '' #to store the key used for decoding
	char_occurences = {} #to store the occurance of each character in the decoded string

	list_of_keys = [chr(i) for i in range(256)] #list of all possible keys

	#iterate through all possible keys

	for k in list_of_keys:
		decoded = ''
		for byte in bytestring:
			decoded += chr(byte ^ ord(k))

		#calculate the score of the decoded string
		common_chars = '/[ETAOINSHRDLU] etaoinsrhdlu'
		decoded_scores.append((decoded, sum(decoded.count(c) for c in common_chars), k))

	#sort the decoded strings by the score
	decoded_scores.sort(key=lambda x: x[1], reverse=True)

	return decoded_scores[0]

#print(compute_hamming_distance("this is a test", "wokka wokka!!!"))

with open('encrypted_msg.txt') as file:
    encrypted_msg = file.read().replace('\n', '')
    print(break_repeating_xor_cipher(encrypted_msg))

