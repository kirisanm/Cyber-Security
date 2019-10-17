Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(k, p):
	return translateMsg(k, p, 'encrypt')

def translateMsg(k, p, mode):
	translated = [] # stores the encrypted message string
	keyindex = 0
	k = k.upper()

	for symbol in p:
		num = Alphabet.find(symbol.upper())
		if num != -1: # -1 means symbol.upper was not found in the alphabet
			if mode == 'encrypt':
				num += Alphabet.find(k[keyindex]) # + since encryption

			num %= len(Alphabet) 

			if symbol.isupper():
				translated.append(Alphabet[num])
			elif symbol.islower():
				translated.append(Alphabet[num].lower())

			keyindex += 1 # move to the next letter in the key
			if keyindex == len(k):
				keyindex = 0
		else:
			translated.append(symbol)
        
	return ''.join(translated)

try:
    start = input("Press 1 then enter to start: ")
    key= input('enter key: ')
    if start == '1':
       plaintext = input("enter the plaintext: ")
       translated = encrypt(key, plaintext)
       print("encrypted: ", translated)
     
    else:
        print("Please press the right start button!")
except Exception as e:
    print(e)
    exit("Enter a valid text please! ")