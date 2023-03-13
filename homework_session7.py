import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
print(r.text)
a = r.text
alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
words = a.split('\n')
message = ""
for word in words:
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
    message += alphabet[vowel_count]

print(message)


