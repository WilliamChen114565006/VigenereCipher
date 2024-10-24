def vigenere_cipher_decrypt(text, key):
    key_index = 0
    key=key.upper() 
    length=len(key)
    keyAlpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain = ""

    for char in text:
        if char.isalpha():  
            shift=(keyAlpha.find(key[key_index%length])) 
            if char.islower():
                decrypted_char=chr((ord(char)-ord('a')-shift)%26+ord('a'))
            else:
                decrypted_char=chr((ord(char)-ord('A')-shift)%26+ord('A'))
            key_index+=1
        else:
            decrypted_char=char 
        plain=plain+decrypted_char

    return plain

text = input("")
key = input("")

plaintext = vigenere_cipher_decrypt(text, key)
print(plaintext)