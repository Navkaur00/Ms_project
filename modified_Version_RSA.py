from Database_Operations import *

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)

if __name__ == '__main__':
    print("=======================================")
    print("==== RSA Encryptor / Decrypter ========")

    publicKey= fetch_public_key_indexes()
    privateKey= fetch_private_key_indexes()

    print(" Public key is ", publicKey, " Private key is ", privateKey)

    message = input(" - Enter a message to encrypt: ")
    encrypted_msg = encrypt(publicKey, message)

    print(" - Encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" - Decrypting message with private key ", privateKey, " . . .")
    print(" - Your message is: ", decrypt(privateKey, encrypted_msg))
    print(" ")
    print("============== END =============================")
    print("================================================")
