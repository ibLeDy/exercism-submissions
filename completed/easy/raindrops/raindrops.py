factors = ((3, "Pling"), (5, "Plang"), (7, "Plong"))

def raindrops(number):

    result = [s for f, s in factors if number % f == 0]

    return "".join(result) if result else str(number)