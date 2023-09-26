print('Welcome to the goofy encoder!')

# unicode zero width space character are: \u200b and \u200c
# \u200b is a zero width space
# \u200c is a zero width non-joiner

def encode(message):
    secret = "$"
    for char in message:
        # get binary representation of the character
        binary = str(bin(ord(char))[2:])
        # if it's a 0, convert it to a zero width space
        for i in binary:
            if i == '0':
                secret += '\u200b'
            else:
                secret += '\u200c'
        secret += '$'
    return secret + '$'


def decode(message):
    clear = ''
    # remove the first and last character, which are dollar signs
    message = message[1:-1]
    # split the message into the individual characters
    characters = message.split('$')
    # remove the last character, which is an empty string
    characters.pop()
    while '' in characters:
        characters.remove('')
    # for each character, convert it to a binary representation
    for char in characters:
        binary = ''
        for i in char:
            if i == '\u200b':
                binary += '0'
            else:
                binary += '1'
        # convert the binary representation to a character
        clear += chr(int(binary, 2))
    return clear


def wrapEncode(message):
    # wrap the encoded message in another message
    encoded = encode(message)
    wrapper = input('Enter the message you want to wrap the encoded message in: ')
    if len(wrapper) != encoded.count('$')-2:
        # pad the wrapper with dots
        while len(wrapper) <= encoded.count('$')-2:
            wrapper += '.'
    wrapped = ''
    bits = encoded.split('$')
    # remove first element, which is an empty string
    bits.pop(0)
    # remove last 2 elements, which are an empty string
    bits.pop()
    bits.pop()
    for i in range(len(bits)):
        wrapped += wrapper[i] + bits[i]
    return wrapped + wrapper[len(wrapped.replace('\u200b', '').replace('\u200c', '')):] 


def wrapDecode(message):
    pog = ''
    temp = []
    # group the zero width characters each group being the one separated by a non zero width character
    for i in range(len(message)):
        if message[i] == '\u200b' or message[i] == '\u200c':
            pog += message[i]
        else:
            temp.append(pog)
            pog = ''
    # remove empty elements
    while '' in temp:
        temp.remove('')
    dec = ''
    for char in temp:
        binary = ''
        for i in char:
            if i == '\u200b':
                binary += '0'
            else:
                binary += '1'
        # convert the binary representation to a character
        dec += chr(int(binary, 2))
    return dec
    

choice = input('Would you like to encode or decode a message? (e/d): ')
if choice == 'e':
    # ask if they would like to wrap the message in another message
    wrap = input('Would you like to wrap the encoded message in another message? (y/n): ')
    if wrap == 'y':
        user_input = input('Enter the message you want to encrypt and wrap: ')
        print(wrapEncode(user_input))
    elif wrap == 'n':
        user_input = input('Enter the message you want to encrypt: ')
        print(encode(user_input))
elif choice == 'd':
    # ask if they would like to unwrap the message
    wrap = input('Would you like to unwrap the message? (y/n): ')
    if wrap == 'y':
        user_input = input('Enter the message you want to unwrap and decrypt: ')
        print(wrapDecode(user_input))
    elif wrap == 'n':

        user_input = input('Enter the message you want to decrypt: ')
        print(decode(user_input))
else:
    print('Invalid choice. Exiting...')
    exit()

