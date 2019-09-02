# y be familiar enough to you that you are able to take a “top down” approach: identifying the recursive relationship simply by considering the definition of the Fibonacci sequence. In other words, a “top down” approach considers the statement “calculating subsequent numbers as the sum of the previous two numbers” and recognizes the relationship
# f(n) = f(n-1) + f(n-2)f(n)=f(n−1)+f(n−2).


def fib(n):
    if n <= 1:
        # print(f"base case: {n}")
        return n

    # print(f"n: {n}")
    return fib(n-1) + fib(n-2)


def fib_dynamic_programming(n):
    a, b = 0, 1

    for step in range(n):
        print(f"a: {a}, b: {b}")
        # a = a + b
        # b = a
        # a, b = a + b, b
        a, b = a + b, a

    return a
