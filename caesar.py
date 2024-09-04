letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text,key):
    ciphertext = ''
    for l in text:
        l = l.lower()
        if not l ==' ':
            index = letters.find(l)
            if index==-1:
                ciphertext+=l
            else:
                new_index = index+key
                if new_index>=26:
                    new_index-=26
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext,key):
    text = ''
    for l in ciphertext:
        l = l.lower()
        if not l ==' ':
            index = letters.find(l)
            if index==-1:
                text+=l
            else:
                new_index = index - key
                if new_index<0:
                    new_index+=26
                text += letters[new_index]
    return text
                     


print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ')
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key: '))
    text = input('Enter the text to encrypt:')
    ciphertext = encrypt(text,key)
    print(f'CIPHERTEXT: {ciphertext}')
elif user_input=='d':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key: '))
    ciphertext = input('Enter the text to decrypt:')
    plaintext = decrypt(ciphertext,key)
    print(f'PLAINTEXT:{plaintext}')
