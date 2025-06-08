#Task 1

def greet_user(name):
    str = name
print("Hello, please enter your name:")
name = input()
greet_user(name)
print(f"Hello, {name}!")

def add_numbers(n):
    print("Please enter two numbers to add:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print (f"The sum of {num1} and {num2} is {result}.")


#Task 2

def describe_pet(per_name, animal_type="dog"):
    print(input("please enter the name of your pet:", per_name))
    print(input("please enter the type of your pet:", animal_type))
    print(f"I have a {animal_type} named {per_name}.")

#Task 3

def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

#Task 4

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
   if n <= 0:
       return 0
   elif n == 1:
       return 1
   return fibonacci(n - 1) + fibonacci(n - 2)