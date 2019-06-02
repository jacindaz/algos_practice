my_stack = [1,2,3,4,5]

def push(stack,item):
    stack.append(item)
    return stack
# print(push(my_stack, 6))


def pop(stack):
    item_to_delete = stack[-1]
    del(item_to_delete)
    return item_to_delete
# print(pop(my_stack))


def peek(stack):
    return stack[-1]
# print(peek(my_stack))


balanced1 = "(()()()())"
not_balanced1 = "((((((())"
def balanced_parentheses(parens_string):
    parens_stack = []

    for char in parens_string:
        print("\n=================\n")
        print(f"original string: {parens_string}")
        print(f"char: {char}, parens_stack: {parens_stack}")

        # if opening parens, push to stack
        if char == "(":
            parens_stack.append(char)
            print(f"appended stack: {parens_stack}")

        # if closing parens, pop the stack
        elif char == ")":
            last_item = parens_stack[-1]
            print(f"last_item: {last_item}")
            if last_item == "(": # if match
                del(parens_stack[-1])
                print(f"match,deleted last_item, new stack: {parens_stack}")

            elif last_item != "(": # if not match
                print(f"last item doesn't match, last_item: {last_item}")
                return False

    # at the end of the string, stack should be empty
    if len(parens_stack) == 0:
        return True
    else:
        return False

print(balanced_parentheses(balanced1))
# print(balanced_parentheses(not_balanced1))
