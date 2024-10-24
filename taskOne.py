def vigenere_cipher_encrypt(text, key):
    key_index = 0
    key = key.upper() 
    length = len(key)
    keyAlpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""

    for char in text:
        if char.isalpha():  
            shift=(keyAlpha.find(key[key_index%length])) 
            if char.islower():
                encrypted_char=chr((ord(char)-ord('a')+shift)%26+ord('a'))
            else:
                encrypted_char=chr((ord(char)-ord('A')+shift)%26+ord('A'))
            key_index+=1
        else:
            encrypted_char = char 
        cipher=cipher+encrypted_char

    return cipher

text = input("")
key = input("")

ciphertext = vigenere_cipher_encrypt(text, key)
print(vigenere_cipher_encrypt(text, key))