## Task 1:

string = ("Python is amazing.")

slice = string[0:6]
print("\n", slice)  

slice1 = string[10:17]
print("\n", slice1)

last_char = string[::-1]
print("\n", last_char)

## Task 2: 

string2 = ("hello, python world!")
strip = string2.strip()


print("\n", strip)

capitalize = string2.capitalize()

print("\n", capitalize)

replace = string2.replace("world", "universe")

print("\n", replace)

upper = string2.upper()

print("\n", upper)

## Task 3

string3 = str(input("Enter a string: "))

if string3 == string3[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

