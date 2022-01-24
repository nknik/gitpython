#A python program to illustrate Caesar Cipher Technique
def decrpt(encrypted_text,shift):
    # shift = 4 # defining the shift count

    # encrypted_text = "KHOOR ZRUOG"

    plain_text = ""

    for c in encrypted_text:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the negative shift
            new_index = (c_index - shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to plain string
            plain_text = plain_text + new_character

        else:

            # since character is not uppercase, leave it as it is
            plain_text += c

    print("Encrypted text:",encrypted_text)

    print("key=>",shift,"Decrypted text:",plain_text)
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

#check the above function
text = "ATTACKATONCE"
s = 4
print( "Text : " + text)
print( "Shift : " + str(s))
print( "Cipher: " + encrypt(text,s))
for i in range(1,15):
    decrpt(encrypt(text,s),i)
