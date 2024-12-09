def collatz(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

# Test Collatz for numbers up to a limit
limit = 10**20
for i in range(1, limit + 1):
    collatz(i)
print(f"All numbers up to {limit} verified!")
