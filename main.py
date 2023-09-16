print('Welcome to the goofy encoder!')

# unicode zero width space character are: \u200b and \u200c
# \u200b is a zero width space
# \u200c is a zero width non-joiner

def encode(message):
    secret = "$"
    for char in message:
        # get binary representation of the character
        binary = str(bin(ord(char))[2:])
        # print(binary)
        # if it's a 0, convert it to a zero width space
        for i in binary:
            if i == '0':
                secret += '\u200b'
            else:
                secret += '\u200c'
        secret += '$'
    return secret + '$'
def decode(message):
    clear = ""
    # remove the first and last character, which are dollar signs
    message = message[1:-1]
    # split the message into the individual characters
    characters = message.split('$')
    # remove the last character, which is an empty string
    characters.pop()
    # print(characters)
    # for each character, convert it to a binary representation
    for char in characters:
        binary = ''
        for i in char:
            if i == '\u200b':
                binary += '0'
            else:
                binary += '1'
        # print(binary)
        # convert the binary representation to a character
        clear += chr(int(binary, 2))
    return clear
    
    

choice = input('Would you like to encode or decode a message? (e/d): ')
if choice == 'e':
    user_input = input('Enter the message you want to encrypt: ')
    print(encode(user_input))
elif choice == 'd':
    user_input = input('Enter the message you want to decrypt: ')
    print(decode(user_input))
else:
    print('Invalid choice. Exiting...')
    exit()

    
