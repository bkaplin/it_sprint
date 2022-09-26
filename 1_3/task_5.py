def convert_to_binar(value):
    b = ''
    while value > 0:
        b = str(value % 2) + b
        value = value // 2
    return b


def multiply_binar(a, b):
    a10 = int(a, 2)
    b10 = int(b, 2)
    return convert_to_binar(a10 * b10)


x1 = input('x1: ')
x2 = input('x2: ')
print(multiply_binar(x1, x2))
