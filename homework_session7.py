import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
print(r.text)
a = r.text
alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
