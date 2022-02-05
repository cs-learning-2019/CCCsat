# f_1 = 1, f_2 = 1
def fib(n):
    # Base case
    if n == 1 or n == 2:
        return 1

    # Recursive step
    return fib(n - 1) + fib(n - 2)


print(fib(5))  # we expect 5
