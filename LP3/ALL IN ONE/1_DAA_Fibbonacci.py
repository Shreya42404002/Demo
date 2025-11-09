# Recursive + step count (simple)
steps = 0
def fib_rec(n):
    global steps
    steps += 1
    return n if n <= 1 else fib_rec(n-1) + fib_rec(n-2)

# Iterative (fast)
def fib_iter(n):
    a, b, steps = 0, 1, 0
    if n == 0: return 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
        steps += 1
    return b, steps

n = 10
for i in range(n+1):
    steps = 0
    print(f"F({i})={fib_rec(i)} | steps={steps}")
print("Iterative:", fib_iter(10))

