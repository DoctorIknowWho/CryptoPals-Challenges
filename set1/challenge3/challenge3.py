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
		common_chars = '/[ETAOIN SHRDLU]'
		decoded_scores.append((decoded, sum(decoded.count(c) for c in common_chars), k))

	#sort the decoded strings by the score
	decoded_scores.sort(key=lambda x: x[1], reverse=True)

	return decoded_scores[0]

user_input = input("Enter a hex encoded string: ")
print(singe_byte_xor_cipher(user_input))