def is_armstrong_number(number):
    number = str(number)
    summed = 0
    for i in number:
        temp = int(i) ** len(number)
        summed += temp

    return True if summed == int(number) else False
