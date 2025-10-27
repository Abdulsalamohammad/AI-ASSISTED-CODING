# Dictionary to store already computed factorial values
memo = {}

def factorial(n):
    """
    Dynamic (memoized) recursive function to calculate factorial.
    Uses a dictionary to store already computed values to avoid recomputation.
    """

    # Step 1: Base case check
    if n == 0 or n == 1:
        return 1

    # Step 2: Check if result already exists in memo
    if n in memo:
        return memo[n]

    # Step 3: Compute factorial recursively and store in memo
    memo[n] = n * factorial(n - 1)

    # Step 4: Return stored result
    return memo[n]


# --- Main Program ---
# Ask the user for input
num = int(input("Enter a number to find its factorial: "))

# Call factorial function
result = factorial(num)

# Display result
print(f"\n✅ Factorial of {num} is {result}\n")

# --- Summary of the algorithm ---
print("📌 Summary of Flow:")
print("1. Used recursion with memoization (dynamic programming).")
print("2. Base case: factorial(0) = factorial(1) = 1.")
print("3. Recursive case: n! = n × factorial(n-1).")
print("4. Stored computed values in 'memo' to avoid recalculating.")
print("5. Final result obtained by combining results from recursive calls.\n")

# Show memo contents for clarity
print("🗂️ Stored intermediate results in memo:")
for key in sorted(memo.keys()):
    print(f"{key}! = {memo[key]}")
