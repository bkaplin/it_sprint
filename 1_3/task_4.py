VARS_LEFT = ['[', '(', '{']
VARS_RIGHT = [']', ')', '}']
MIRROW_DICT = {
    '[': ']',
    '(': ')',
    '{': '}',
    ']': '[',
    ')': '(',
    '}': '{'
}


def check_str(value):
    lefts = []
    for elem in value:
        if elem in VARS_LEFT:
            lefts.append(elem)
        elif elem in VARS_RIGHT:
            if lefts and elem == MIRROW_DICT.get(lefts[-1], None):
                lefts.pop()
            else:
                return False

    return True if not lefts else False


print(check_str(input('value: ')))
