# %%
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib(10))  # Output: <generator object fib at 0x...>

# %%
