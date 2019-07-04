def decimal_number_to_binary(number):
    # keep track of remainder in a list
    binary_stack = []

    # keep dividing by 2
    while number >= 1:
        remainder = number % 2
        number = int(number/2)
        print(f"remainder: {remainder}, number: {number}")

        binary_stack.append(remainder)
        print(f"binary_stack: {binary_stack}")


    # build up the binary number by popping off the stack
    binary_number = ""
    while len(binary_stack) > 0:
        binary_number = binary_number + str(binary_stack.pop())

    # return binary number
    return binary_number


print(decimal_number_to_binary(100))
