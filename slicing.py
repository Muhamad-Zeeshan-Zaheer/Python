#slicing in python means to access  a part of string
string = "Hello, World!"
print(string[0:5])  # Output: Hello
print(string[7:])   # Output: World!
print(string[:5])   # Output: Hello
print(string[-6:])  # Output: World!
print(string[::2])  # Output: Hlo ol!
print(string[::-1]) # Output: !dlroW ,olleH
print(string[1:5:2]) # Output: el
print(string[::3]) # Output: Hoo!
print(string[1:5:3]) # Output: e
print(string[1:5:-1]) # Output: (empty string)
print(string[5:1:-1]) # Output: ,olle
print(string[1:5:-2]) # Output: (empty string)
