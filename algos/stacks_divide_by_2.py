def decimal_number_to_binary(number):
    """
    Convert decimal number (base 10) to binary
    """
    binary_stack = []
    while number >= 1:
        remainder = number % 2
        number = int(number/2)

        binary_stack.append(remainder)

    binary_number = ""
    while len(binary_stack) > 0:
        binary_number = binary_number + str(binary_stack.pop())

    return binary_number


def convert_to_base(decimal_number, base):
    """
    Convert to any base between 2-16
    """
    digits = '0123456789abcdef'
    base_stack = []
    while decimal_number > 0:
        remainder = decimal_number % base
        base_stack.append(digits[remainder])
        decimal_number = decimal_number // base

    final_conversion = ""
    while len(base_stack) > 0:
        final_conversion += str(base_stack.pop())

    return final_conversion
