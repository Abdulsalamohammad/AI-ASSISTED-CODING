def factorial_iterative(n):
    """Calculate factorial using an iterative approach."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate factorial using a recursive approach."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        fact_iter = factorial_iterative(num)
        fact_rec = factorial_recursive(num)
        print(f"\nIterative factorial of {num} is: {fact_iter}")
        print(f"Recursive factorial of {num} is: {fact_rec}")
    except ValueError as e:
        print(f"Invalid input: {e}")