def check_number(number):
    if abs(number) != number:
        raise ValueError(f"{number} is not a positive integer")
    elif number == 0:
        raise ValueError("0 is not a positive integer")

def steps(number):
    check_number(number)
    steps = 0

    new = number
    while new != 1:
        if new % 2 == 0:
            new = new / 2
        elif new % 2 == 1:
            new = (new * 3) + 1
        steps += 1

    return steps
