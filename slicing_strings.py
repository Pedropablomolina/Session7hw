a = "abcdefghijklmnop"
print(a[3:6])
print(a[13:17], a[-3:], a[13:])  # all of them mean the same thing: nop
print(a[:10])

# step slice
print(a[:10:2], a[::3])

# you can use negative start, stop and even step
print(a[10:3:-1])
print(a[::-1])  # reversed string

# check if a string is palindrome:
a = "racecar"
if a == a[::-1]:
    print(a, "is palindrome")
else:
    print("not so much")