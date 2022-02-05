# Python CCC
# Dynamic Programming
# Kavan Lam
# Nov 19, 2021

import time

# -------------------------------------------------------
def fib_simple_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_simple_recursive(n - 1) + fib_simple_recursive(n - 2)

# -------------------------------------------------------
n = 35
fib = [0] + ([-1] * n)
fib[1] = 1
fib[2] = 1

def fib_dp_loop(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        
    return fib[n]

start_time = time.time()
print(fib_dp_loop(n))  # expect 9227465 for n = 35
end_time = time.time()
print(end_time - start_time, "sec")
