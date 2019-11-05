def classify(number):
    factors = []
    summed = 0

    if abs(number) == number and number != 0:
        for i in range(1, number + 1):
            if number % i == 0:
                if i != number:
                    factors.append(i)
                    summed += i
    else:
        raise ValueError("The number needs to be a natural one and not 0")

    if summed == number:
        return 'perfect'
    if summed > number:
        return 'abundant'
    if summed < number:
        return 'deficient'
