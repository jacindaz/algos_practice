def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib_dynamic_programming(n):
    a, b = 0, 1
    for step in range(n):
        a, b = a + b, a
    return a


def num_paths(height, width):
    if height == 0 and width == 0:
        return 0
    if height == 0 or width == 0:
        return 1
    return num_paths(height-1, width) + num_paths(height, width-1)


def num_paths_dp(height, width):
    pass
