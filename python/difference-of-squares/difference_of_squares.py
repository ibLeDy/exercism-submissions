def square_of_sum(number):
    square = 0
    for i in range(number + 1):
        square += i

    square = square ** 2
    return square


def sum_of_squares(number):
    sum = 0
    for i in range(number + 1):
        sum += i ** 2

    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
