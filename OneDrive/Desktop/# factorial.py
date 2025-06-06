# factorial.py

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {number} is {factorial(number)}")
    except ValueError:
        print("Please enter a valid integer.")

