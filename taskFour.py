from collections import Counter
import string
import math

english_freq = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074
}

def vigenere_cipher_decrypt(text, key):
    key_index = 0
    key = key.upper() 
    key_length = len(key)
    keyAlpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain = ""

    for char in text:
        if char.isalpha():  
            shift=(keyAlpha.find(key[key_index % key_length])) 
            if char.islower():
                decrypted_char = chr((ord(char)-ord('a')-shift)%26+ord('a'))
            else:
                decrypted_char = chr((ord(char)-ord('A')-shift)%26+ord('A'))
            key_index+=1
        else:
            decrypted_char = char 
        plain=plain+decrypted_char

    return plain

def vigenere_cipher_decrypt_key_size(ciphertext, key_length):
    key=""
    key_length=int(key_length)
    cipherSegments = ['' for _ in range(key_length)]

    index = 0
    for char in ciphertext:
        if char.isalpha():
            cipherSegments[index % key_length] += char.lower()
            index += 1

    for n in range(len(cipherSegments)):
        letterChiTest_array=[]

        cipher_shift=[]
        for shift in range(26):
            shifted_word=""
            for char in cipherSegments[n]:
                shifted_char=chr((ord(char)-ord('a')-shift) % 26 + ord('a'))
                shifted_word+=shifted_char
            cipher_shift.append(shifted_word)

        for group in cipher_shift:
            chi=0
            observed_freq=Counter(group)
            total_letters = len(observed_freq)
            for char in string.ascii_lowercase:
                observed = observed_freq[char] if char in observed_freq else 0
                expected = english_freq[char] * total_letters/100
                if expected > 0:
                    chi+=((observed-expected)**2)/expected
            letterChiTest_array.append(chi)
        min_chi=letterChiTest_array.index(min(letterChiTest_array))
        key+=chr(97+min_chi)

    decodedCipher=vigenere_cipher_decrypt(ciphertext, key)
    print(key.upper())
    return decodedCipher

def count_coincidences(ciphertext, shift):
    coincidences = 0
    for i in range(len(ciphertext) - shift):
        if ciphertext[i] == ciphertext[i + shift]:
            coincidences += 1
    return coincidences

def mean(values):
    return sum(values)/len(values)

def standard_deviation(values, mean):
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

def vigenere_cipher_decrypt_find_key_length(ciphertext):
    clean_text = ''.join([char.lower() for char in ciphertext if char.isalpha()])
    coincidence_count=[]

    text_percent75=int(len(clean_text)*0.75)
    for shift in range(1, text_percent75):
        coincidences = count_coincidences(clean_text, shift)
        coincidence_count.append(coincidences)

    significant_shifts = []
    for shift, coincidences in enumerate(coincidence_count, start=1):
        if coincidences > mean(coincidence_count) + 1.5 * standard_deviation(coincidence_count, mean(coincidence_count)):
            significant_shifts.append(shift)

    differences = []
    for i in range(1, len(significant_shifts)):
        difference = significant_shifts[i] - significant_shifts[i - 1]
        differences.append(difference)
    difference_counts = Counter(differences)
    most_common_difference = difference_counts.most_common(1)[0][0]
  
    return vigenere_cipher_decrypt_key_size(ciphertext, most_common_difference)
            

text=input("")
test=vigenere_cipher_decrypt_find_key_length(text)
print(test)



    