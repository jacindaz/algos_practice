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
    memoized_values = []
    for current_height in range(height+1):
        height_values = []
        for current_width in range(width+1):
            if current_height == 0 or current_width == 0:
                height_values.append(1)
        memoized_values.append(height_values)

    for current_height in range(height+1):
        height_values = []
        for current_width in range(width+1):
            if current_height != 0 and current_width != 0:
                print(f"\nmemoized values: {memoized_values}===============")
                print(f"current_height: {current_height}, current_width: {current_width}")

                # look up: height-1
                up = memoized_values[current_height-1][current_width]
                print(f"up: {up}")

                # look left: width-1
                left = memoized_values[current_height][current_width-1]
                print(f"left: {left}")

                # add up + left
                sum = up + left
                print(f"sum: {sum}")

                # set new value
                memoized_values[current_height].append(sum)

    return memoized_values[height][width]
