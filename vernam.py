import random

def generate_key(message):
    key = ''
    for _ in range(len(message)):
        key += chr(random.randint(97, 122))  # генерируем случайный символ из диапазона 'a'-'z'
    return key

def encrypt(message, key):
    ciphertext = ''
    for i in range(len(message)):
        ciphertext += chr((ord(message[i]) + ord(key[i])) % 256)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext += chr((ord(ciphertext[i]) - ord(key[i]) + 256) % 256)
    return plaintext

message = 'Hello, World!'
key = generate_key(message)

ciphertext = encrypt(message, key)

decrypted_message = decrypt(ciphertext, key)

print('Message:', message)
print('Key:', key)
print('Ciphertext:', ciphertext)
print('Decrypted message:', decrypted_message)

'''
Message: Hello, World!
Key: uhunxfrjxlcft
Ciphertext: ½ÍáÚçÁçÞÏÊ
Decrypted message: Hello, World!
'''