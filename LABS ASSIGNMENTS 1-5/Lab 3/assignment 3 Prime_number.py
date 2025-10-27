# Implementations from different prompting strategies

# Zero-Shot
def is_prime_zero_shot(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# One-Shot
def is_prime_one_shot(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

# Few-Shot
def is_prime_few_shot(n):
    if n <= 1:
        return "Not Prime"
    if n == 2:
        return "Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

# Context-Managed (Optimized)
def is_prime_context(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test numbers
test_numbers = [2, 3, 4, 5, 17, 19, 20, 97, 100, 9973]

print("Number | Zero-Shot | One-Shot | Few-Shot | Context-Managed")
print("-" * 55)

for num in test_numbers:
    z = is_prime_zero_shot(num)
    o = is_prime_one_shot(num)
    f = is_prime_few_shot(num)
    c = is_prime_context(num)
    print(f"{num:<6} | {z!s:<9} | {o:<8} | {f:<8} | {c}")
