infix1 = "(B * C)"
def infix_to_postfix(infix_string):
    # Create an empty stack called operation_stack for keeping operators.
    operation_stack = []

    # Create an empty list for output.
    output_list = []

    # Convert the input infix string to a list by using the string method split.
    infix_list = infix_string.split(" ")

    # Scan the token list from left to right.
    for char in infix_list:

        # If the token is an operand, append it to the end of the output list.


        # If the token is a left parenthesis, push it on the operation_stack.

        # If the token is a right parenthesis, pop the operation_stack until
        # the corresponding left parenthesis is removed.
        # Append each operator to the end of the output list.

        # If the token is an operator, *, /, +, or -, push it on the operation_stack.
        # However, first remove any operators already on the operation_stack
        # that have higher or equal precedence and append them to the output list.

    # When the input expression has been completely processed,
    # check the operation_stack. Any operators still on the stack
    # can be removed and appended to the end of the output list.



print(infix_to_postfix(infix1)) # expected 'B C *'
