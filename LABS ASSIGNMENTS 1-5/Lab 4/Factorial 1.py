def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        fact = factorial(num)
        print(f"\nThe factorial of {num} is: {fact}")
    except ValueError as e:
        print(f"Invalid input: {e}")