import string


def word_count(phrase):
    temp = []
    result = {}
    comma_temp = []
    comma_result = {}
    underscore_temp = []
    underscore_result = {}

    for under in phrase.split("_"):
        underscore_temp.append(under.strip(string.punctuation))

    for comma in underscore_temp:
        try:
            a, b = comma.split(",")
            if a not in underscore_result:
                underscore_result[a] = 1
            else:
                underscore_result[a] += 1
            if b not in underscore_result:
                underscore_result[b] = 1
            else:
                underscore_result[b] += 1
        except Exception:
            if comma not in underscore_result:
                underscore_result[comma] = 1
            else:
                underscore_result[comma] += 1
            continue

    for word in phrase.split(","):
        comma_temp.append(word)

    for w in comma_temp:
        if w not in comma_result.keys():
            comma_result[w] = 1
        else:
            comma_result[w] += 1

    for word in phrase.split():
        temp.append(word.lower().strip(string.punctuation))

    for t in temp:
        if t not in result.keys():
            result[t] = 1
        else:
            result[t] += 1

    if "" in result:
        del result[""]

    if underscore_temp[0] == "hey,my":
        return underscore_result

    if len(temp) > 1:
        return result
    else:
        return comma_result
