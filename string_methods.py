print(dir(""))

help("".capitalize)
print("bogDAN!", "bogDAN!".capitalize())

# lower
print("lower example ABCDEF =", "ABCDEF".lower())

# center
print("center example: James=", "James".center(30))

# count
a = "ana-ana-ana-naana"
print(a.count("ana"), a.count("a"))

# find - index of first occurrence unless a start is specified
a = "banana, i like bananas"
print(a.find("banana"), a.find("banana", 5), a[5:].find("banana"))

# islower
print("banana".islower(), "Banana".islower())

# split, breaks down by delimiter
a = "I see a cat on a roof"
print(a.split())  # breaks down by space and returns a list
a = "I,like,fish,and,chips!"
print(a.split(","))
print(a.split("fish"))

# join (kinda like the opposite of split)
a = "I see a cat on a roof"
words = a.split()

print(" ".join(words))
print("++".join(words))
print(" freaking ".join(words))




