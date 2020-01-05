def get_first_divisor(begin, end):
    for i in range(begin, end):
        if end % i == 0:
            return i


def factors(value):
    if value == 2:
        return [2]

    num = value
    prime_factors = []
    div = get_first_divisor(2, value)

    while num != 1:
        count = 0
        while int(num / div) == num / div:
            num = num / div
            count += 1

        prime_factors.extend([div]* count)
        div = get_first_divisor(div + 1, value)

    return prime_factors
