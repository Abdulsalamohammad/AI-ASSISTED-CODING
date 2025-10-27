def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    # Using a while loop for slightly better efficiency (less overhead than for loop in some cases)
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            fact = factorial(num)
            print(f"\nThe factorial of {num} is: {fact}")
    except ValueError as e:
        print(f"Invalid input: {e}")