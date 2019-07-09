import string

def word_count(phrase):
    result = {}
    word = ""

    for char in phrase.lower():
        if char.isalnum():
            word += char
        # elif char in string.punctuation:
            # word += char
        else:
            if len(word):
                if result.get(word):
                    result[word] += 1
                else:
                    result.update({word: 1})
                word = ""

    if result.get(word) and len(word):
        result[word] += 1
    elif len(word):
        result.update({word: 1})
        
    return result
    # print(result)

# def word_count(phrase):
#     result = {}
#     word = ""

#     for char in phrase:
#         pass
#         # print(char)

# phrase = "Joe can't tell between 'large' and large."
# test = word_count(phrase)
