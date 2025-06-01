#Task 1

list_og =  ['Oranges', 'Apples', 'Bananas', 'Grapes', 'Pineapples']
print ("This is the original list:", list_og)

list_og.append('Mangoes')
print ("Mangoes added:", list_og)

list_og.remove('Pineapples')
print ("Pineapples removed:", list_og)

list_og.reverse()
print ("List reversed:", list_og)

#Task 2
my_info = {
    "name": "Justin",
    "age": 19,
    "city": "Houston"
}
my_info["favorite color"] = "Black"
my_info["city"] = "Los Angeles"

print("Keys:", ", ".join(my_info.keys()))
print("Values:", ", ".join(str(value) for value in my_info.values()))

#Task 3

favorite_things = ('Movies', 'Gaming', 'Coding')

try:
    favorite_things[0] = 'The Matrix'
except TypeError:
    print("Oops! Tuples cannot be changed.")

print("Favorite things:", favorite_things)
print("Length of tuple:", len(favorite_things))