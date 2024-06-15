# conda activate TesseracT

# pip install pycryptodome

# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# def encrypt_AES_CTR(key, data):
#     cipher = AES.new(key, AES.MODE_CTR)
#     nonce = cipher.nonce
#     ciphertext = cipher.encrypt(data)
#     return nonce, ciphertext

# def decrypt_AES_CTR(key, nonce, ciphertext):
#     cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
#     plaintext = cipher.decrypt(ciphertext)
#     return plaintext

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = b'Hello, World! This is a secret message.'

# # Шифрование
# nonce, ciphertext = encrypt_AES_CTR(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_CTR(key, nonce, ciphertext)
# print("Расшифрованный текст:", decrypted_data.decode('utf-8'))

# Зашифрованный текст: b'3\x1c\xcb\x92L\xac\xf0\x98\x82`\x9fN\xe2\xb5\xc6\x8d\xa2\xaaEH\xf3\xda\x0e\xf3\xd3m\x04~&\xde\xe7h\x1f8K\xbd\xa8\xaex'
# Расшифрованный текст: Hello, World! This is a secret message.



# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import base64

# def encrypt_AES_CTR(key, data):
#     cipher = AES.new(key, AES.MODE_CTR)
#     nonce = cipher.nonce
#     ciphertext = cipher.encrypt(data.encode())
#     return nonce, base64.b64encode(ciphertext).decode()

# def decrypt_AES_CTR(key, nonce, ciphertext):
#     cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
#     ciphertext = base64.b64decode(ciphertext)
#     plaintext = cipher.decrypt(ciphertext)
#     return plaintext.decode()

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# nonce, ciphertext = encrypt_AES_CTR(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_CTR(key, nonce, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# Зашифрованный текст: 1aj3OrA5gSlSCZpTf3r85uKaTY0TuAuW+lMcBaW7T1qBnnt3aylv
# Расшифрованный текст: Hello, World! This is a secret message.


# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import base64

# def pad(data):
#     block_size = 16
#     padding = block_size - len(data) % block_size
#     return data + bytes([padding] * padding)

# def unpad(data):
#     padding = data[-1]
#     return data[:-padding]

# def encrypt_AES_ECB(key, data):
#     cipher = AES.new(key, AES.MODE_ECB)
#     padded_data = pad(data.encode())
#     ciphertext = cipher.encrypt(padded_data)
#     return base64.b64encode(ciphertext).decode()

# def decrypt_AES_ECB(key, ciphertext):
#     cipher = AES.new(key, AES.MODE_ECB)
#     ciphertext = base64.b64decode(ciphertext)
#     decrypted_data = cipher.decrypt(ciphertext)
#     return unpad(decrypted_data).decode()

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# ciphertext = encrypt_AES_ECB(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_ECB(key, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# Зашифрованный текст: G9Q2ZNtzABIYrYJh9SDsF0V7O0qDwI3vavK4SoTGVk3631u9jMmYBsY7sEVJuC+z
# Расшифрованный текст: Hello, World! This is a secret message.



# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import base64

# def encrypt_AES_CFB(key, data):
#     cipher = AES.new(key, AES.MODE_CFB)
#     ciphertext = cipher.encrypt(data.encode())
#     return base64.b64encode(cipher.iv + ciphertext).decode()

# def decrypt_AES_CFB(key, ciphertext):
#     ciphertext = base64.b64decode(ciphertext)
#     iv = ciphertext[:16]
#     cipher = AES.new(key, AES.MODE_CFB, iv=iv)
#     plaintext = cipher.decrypt(ciphertext[16:])
#     return plaintext.decode()

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# ciphertext = encrypt_AES_CFB(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_CFB(key, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# Зашифрованный текст: x+zlE7CdXOPZcSJ1eeNgn4Zq19tcMp6+31ley5ndkDnuNublGfIT5SZuynVJtDQIyRxIQSHZww==
# Расшифрованный текст: Hello, World! This is a secret message.



# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import base64

# def encrypt_AES_CTR(key, data):
#     cipher = AES.new(key, AES.MODE_CTR)
#     nonce = cipher.nonce
#     ciphertext = cipher.encrypt(data.encode())
#     return base64.b64encode(nonce + ciphertext).decode()

# def decrypt_AES_CTR(key, ciphertext):
#     ciphertext = base64.b64decode(ciphertext)
#     nonce = ciphertext[:8]
#     cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
#     plaintext = cipher.decrypt(ciphertext[8:])
#     return plaintext.decode()

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# ciphertext = encrypt_AES_CTR(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_CTR(key, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# Зашифрованный текст: TEvEJET4oD/Dob55/aSlvS48lyTgTew9QwSkpLWILWAdjJnktSYQaNeKItcboXI=
# Расшифрованный текст: Hello, World! This is a secret message.



# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import base64

# def pad(data):
#     block_size = 16
#     padding = block_size - len(data) % block_size
#     return data + chr(padding) * padding

# def unpad(data):
#     padding = ord(data[-1])
#     return data[:-padding]

# def encrypt_AES_CTR(key, data):
#     cipher = AES.new(key, AES.MODE_CTR)
#     nonce = cipher.nonce
#     padded_data = pad(data)
#     ciphertext = cipher.encrypt(padded_data.encode())
#     return base64.b64encode(nonce + ciphertext).decode()

# def decrypt_AES_CTR(key, ciphertext):
#     ciphertext = base64.b64decode(ciphertext)
#     nonce = ciphertext[:8]
#     cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
#     plaintext = cipher.decrypt(ciphertext[8:])
#     return unpad(plaintext.decode())

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# ciphertext = encrypt_AES_CTR(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_CTR(key, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# Зашифрованный текст: AwJ7qBpBUe4j9Nsn1GgCjlvZORnuQpU8wc9ttWHIiowMltceOZuZCiAwnojODgAovZYEPhjH5AU=
# Расшифрованный текст: Hello, World! This is a secret message.


# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import base64

# def encrypt_AES_CFB(key, data):
#     cipher = AES.new(key, AES.MODE_CFB)
#     ciphertext = cipher.encrypt(data.encode())
#     return base64.b64encode(cipher.iv + ciphertext).decode()

# def decrypt_AES_CFB(key, ciphertext):
#     ciphertext = base64.b64decode(ciphertext)
#     iv = ciphertext[:16]
#     cipher = AES.new(key, AES.MODE_CFB, iv=iv)
#     plaintext = cipher.decrypt(ciphertext[16:])
#     return plaintext.decode()

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# ciphertext = encrypt_AES_CFB(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_CFB(key, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# # Зашифрованный текст: v8ZfRdYvycShytcIfI31/NPouLUFt436vghIdR5kz2r6ZaZU4S1Z+TiyL2sDLQFy5xuLZ/A2kQ==
# # Расшифрованный текст: Hello, World! This is a secret message.

# # Зашифрованный текст
# encrypted_text = "v8ZfRdYvycShytcIfI31/NPouLUFt436vghIdR5kz2r6ZaZU4S1Z+TiyL2sDLQFy5xuLZ/A2kQ="
# # Расшифрованный текст
# decrypted_text = "Hello, World! This is a secret message."

# # Подсчет символов
# encrypted_length = len(encrypted_text)
# decrypted_length = len(decrypted_text)

# print("Длина зашифрованного текста:", encrypted_length)
# print("Длина расшифрованного текста:", decrypted_length)

# # Длина зашифрованного текста: 75
# # Длина расшифрованного текста: 39


# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import base64

# def pad(data):
#     block_size = 16
#     padding = block_size - len(data) % block_size
#     return data + chr(padding) * padding

# def unpad(data):
#     padding = ord(data[-1])
#     return data[:-padding]

# def encrypt_AES_CTR(key, data):
#     cipher = AES.new(key, AES.MODE_CTR)
#     nonce = cipher.nonce
#     padded_data = pad(data)
#     ciphertext = cipher.encrypt(padded_data.encode())
#     return base64.b64encode(nonce + ciphertext).decode()

# def decrypt_AES_CTR(key, ciphertext):
#     ciphertext = base64.b64decode(ciphertext)
#     nonce = ciphertext[:8]
#     cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
#     plaintext = cipher.decrypt(ciphertext[8:])
#     return unpad(plaintext.decode())

# # Генерация случайного ключа
# key = get_random_bytes(16)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# ciphertext = encrypt_AES_CTR(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_AES_CTR(key, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# Зашифрованный текст: nqe+I088f4YjK1NYkmtD0iy9CcQfC/o6g2iVXSNMFKw72olb4z1c7y6+zTdwGPWW32d7QpJb8WY=
# Расшифрованный текст: Hello, World! This is a secret message.


# from Crypto.Cipher import ChaCha20
# from Crypto.Random import get_random_bytes

# def encrypt_ChaCha20(key, data):
#     cipher = ChaCha20.new(key=key)
#     ciphertext = cipher.nonce + cipher.encrypt(data.encode())
#     return ciphertext

# def decrypt_ChaCha20(key, ciphertext):
#     nonce = ciphertext[:8]
#     cipher = ChaCha20.new(key=key, nonce=nonce)
#     plaintext = cipher.decrypt(ciphertext[8:])
#     return plaintext.decode()

# # Генерация случайного ключа
# key = get_random_bytes(32)

# # Данные для шифрования
# data = 'Hello, World! This is a secret message.'

# # Шифрование
# ciphertext = encrypt_ChaCha20(key, data)
# print("Зашифрованный текст:", ciphertext)

# # Дешифрование
# decrypted_data = decrypt_ChaCha20(key, ciphertext)
# print("Расшифрованный текст:", decrypted_data)

# # Зашифрованный текст: b'\xeep\xc9~<\xbb\xd2D\x8ae7\x8f\xb1%:\xc9\xd8c\x8fAe\x9e\xef\x88\xd4>\xe0\xf8JG\xbbj\x8f4\xf8\x16<%\x00V\x16i\xe5\x80\x03\xad\x8a'
# # Расшифрованный текст: Hello, World! This is a secret message.


from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import base64

def encrypt_ChaCha20(key, data):
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.nonce + cipher.encrypt(data.encode())
    return base64.b64encode(ciphertext).decode()

def decrypt_ChaCha20(key, ciphertext):
    ciphertext = base64.b64decode(ciphertext + '=' * (-len(ciphertext) % 4))  # Добавляем паддинг
    nonce = ciphertext[:8]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext[8:])
    return plaintext.decode()

# Генерация случайного ключа
key = get_random_bytes(32)

# Данные для шифрования
data = 'Hello, World! This is a secret message.'

# Шифрование
ciphertext = encrypt_ChaCha20(key, data)
print("Зашифрованный текст:", ciphertext)

# Дешифрование
decrypted_data = decrypt_ChaCha20(key, ciphertext)
print("Расшифрованный текст:", decrypted_data)

# Зашифрованный текст: CmCwYYLS1SMp3JQZ1fAqNkMYD1VCeUW1jNA42SqFOJpXyIDepMixs2Kjn3huVrE=
# Расшифрованный текст: Hello, World! This is a secret message.