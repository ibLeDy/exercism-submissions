def sum_of_multiples(limit, multiples):
    temp = []
    for i in range(2, limit):
        for j in range(len(multiples)):
            try:
                if i % multiples[j] == 0:
                    temp.append(i)
            except ZeroDivisionError as e:
                print(e)

    temp = set(temp)
    result = 0
    
    for num in temp:
        result += num

    if len(multiples) == 1 and multiples[0] == 1:
        return result + 1
    else:
        return result
