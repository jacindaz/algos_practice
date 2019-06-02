def balanced_parentheses(parens_string):
    parens_stack = []
    opening = "("
    closing = ")"

    for char in parens_string:
        print("\n=================\n")
        print(f"original string: {parens_string}")
        print(f"char: {char}, parens_stack: {parens_stack}")

        if char == opening:
            parens_stack.append(char)
            print(f"appended stack: {parens_stack}")

        if len(parens_stack) > 0 and parens_stack[-1] == opening and char == closing:
                del(parens_stack[-1])
                print(f"match,deleted last_item, new stack: {parens_stack}")
        elif len(parens_stack) == 0:
            return False

    # at the end of the string, stack should be empty
    if len(parens_stack) == 0:
        return True
    return False


def match_and_pop(current_item, stack):
    last_item = stack[-1]
    if last_item == "(" and current_item == ")": # match
        del(stack[-1])

    return stack

def balanced_parentheses2(parens_string):
    opening = "("
    closing = ")"
    parens_stack = []

    for char in parens_string:
        if char == opening:
            parens_stack.append(opening)
        else:
            try:
                match_and_pop(char, parens_stack)
            except IndexError:
                return False

    return len(parens_stack) == 0
