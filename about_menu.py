import turtle

def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Recursive function to calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def draw_fractal(branch_length, t):
    """Recursive function to draw a fractal tree using the turtle library."""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal(branch_length - 15, t)
        t.left(40)
        draw_fractal(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def fractal_pattern():
    """Set up the turtle environment and draw a fractal tree."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_fractal(100, t)
    screen.mainloop()

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate the factorial of a number")
        print("2. Find the nth Fibonacci number")
        print("3. Draw a recursive fractal pattern")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                num = int(input("Enter a number to find its factorial: "))
                if num < 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The factorial of {num} is {factorial(num)}.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        elif choice == "2":
            try:
                num = int(input("Enter the position of the Fibonacci number: "))
                if num < 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        elif choice == "3":
            print("Drawing a fractal pattern...")
            fractal_pattern()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()