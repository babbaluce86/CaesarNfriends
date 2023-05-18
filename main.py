from helper import *


if __name__ == '__main__':

    print('Enter an integer number ')
    n = int(input())
    print('The generated key is as follows:')
    print('\n')
    key = generate_key(n)
    print(key)
    print('\n')
    print('Type a message: ')
    print('\n')
    message = input()
    print('Encrypted message: ')
    print('\n')
    encrypted_message = encrypt(key=key, message=str(message))
    print(encrypted_message)
    print('\n')
    print('Want to Decrypt back? (Y/N) ')
    yn = input() 
    if (yn == 'Y') | (yn == 'y'):
        dkey = get_decryption_key(key)
        print('The Decrypted message is: ')
        print('\n')
        print(encrypt(key=dkey, message=encrypted_message))
        print('\n')

    elif (yn == 'N') | (yn == 'n'):
        print('Want to try an attack on the encrypted message? (Y/N)')
        ny = input()

        if (ny == 'Y') | (ny == 'y'):


            for i in range(0, 26):
                dkey = generate_key(i)
                message = encrypt(dkey, encrypted_message)
                print(i, message)

        else:
            print('Goodbye')        
    