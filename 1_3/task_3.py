def process_res(a, b, str_a, str_b, str_c):
    if a == 4:
        if b == 0:
            res = f'{str_a}{str_b}'
        elif b == 1:
            res = f'{str_a}{str_c}'
        else:
            res = ''
    else:
        res = str_b * b + str_a * a
    return res


def convert_to_roma(value):
    try:
        value = int(value)
    except:
        return 'Error'

    m = value // 1000
    d = (value - m * 1000) // 500
    c = (value - m * 1000 - d * 500) // 100
    l = (value - m * 1000 - d * 500 - c * 100) // 50
    x = (value - m * 1000 - d * 500 - c * 100 - l * 50) // 10
    v = (value - m * 1000 - d * 500 - c * 100 - l * 50 - x * 10) // 5
    i = value - m * 1000 - d * 500 - c * 100 - l * 50 - x * 10 - v * 5

    res = 'M' * m

    res += process_res(c, d, 'C', 'D', 'M')
    res += process_res(x, l, 'X', 'L', 'C')
    res += process_res(i, v, 'I', 'V', 'X')

    # TODO: оставил комментарий для понимания
    # if c == 4:
    #     if d == 0:
    #         res += 'CD'
    #     elif d == 1:
    #         res += 'CM'
    # else:
    #     res += 'D' * d
    #     res += 'C' * c
    #
    # if x == 4:
    #     if l == 0:
    #         res += 'XL'
    #     elif l == 1:
    #         res += 'XC'
    # else:
    #     res += 'L' * l
    #     res += 'X' * x
    #
    # if i == 4:
    #     if v == 0:
    #         res += 'IV'
    #     elif v == 1:
    #         res += 'IX'
    # else:
    #     res += 'V' * v
    #     res += 'I' * i

    return res


print(convert_to_roma(input('x: ')))
