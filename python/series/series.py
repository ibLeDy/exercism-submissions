def slices(series, length):
    series = str(series)
    number = int(length - 1)
    
    if len(series) == 0 or len(series) < length:
        raise ValueError("Series is empty or less than length")
    if length == 0 or abs(length) != length:
        raise ValueError("Length is 0 or a negative number")
    
    start = 0
    end = length
    result = []
    
    for i in range(len(series)):
        temp = series[start:end]
        
        if len(temp) == length:
            result.append(temp)

        start += 1
        end += 1
    
    return result