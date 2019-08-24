CHAR_FOR_INT = '0123456789abcdef'

def to_string(num, base):
    # base case
    # what state changes?
    # recursive call
    print(f"\noriginal num: {num}, base: {base}")

    if num < base:
        print(f"num is less than base: {num}. result: {CHAR_FOR_INT[num]}")
        return CHAR_FOR_INT[num]

    new_num = num // base
    mod_num = num % base
    translated_mod = CHAR_FOR_INT[mod_num]
    print(f"new_num: {new_num}, original num: {num}")
    print(f"modular original number: {mod_num}, translated_mod: {translated_mod}")

    return to_string(new_num, base) + translated_mod
