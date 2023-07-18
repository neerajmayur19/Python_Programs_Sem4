import re

def find_all_vowels_consonants_and_digits(text):
    vowels = re.findall(r'[aeiouAEIOU]',text)
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]',text)
    digits = re.findall(r'\d',text)
    
    vowel_count = len(vowels)
    consonant_count = len(consonants)
    digit_count = len(digits)
    
    return vowel_count,consonant_count,digit_count
    

text = "I am neeraj mayur and i live in #4/5 2307 Bollivard Brooklyn"
v,c,d = find_all_vowels_consonants_and_digits(text)
print(v)
print(c)
print(d)
