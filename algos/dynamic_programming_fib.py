def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib_dynamic_programming(n):
    a, b = 0, 1
    for step in range(n):
        a, b = a + b, a
    return a
