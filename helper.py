'''************************

Helper basic methods for 
the classical Caesar Cipher.

*****************************'''



from typing import *

def generate_key(n: int, italian: bool=True):

    """Generates a Key for encryption

    Returns:
        _type_: (str), encryption key.
    """

    letters : str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if italian:
        letters : str = "ABCDEFGHILMNOPQRSTUVZ"
    key : dict = {}
    cnt : int = 0
    for c in letters:
        key[c] : str = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key

def get_decryption_key(key: dict):
    """Given an encrypted key, 
       performs decription.

    Args:
        key (dict): encryption key.

    Returns:
        _type_: decrypted key

    """
    
    dkey : dict = {}
    for c in key:
        dkey[key[c]] : str = c
    return dkey

def encrypt(key: dict, message: str):
    """Encrypt a message given a key.

    Args:
        key (dict): encryption key
        message (str): a text or string

    Returns:
        _type_: encrypted message.
    """
    cipher : str = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c

    return cipher


