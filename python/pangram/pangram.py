import string

letters = string.ascii_lowercase
punctuation = string.punctuation
digits = string.digits
space = string.whitespace


def make_dict():
    letter_count = {}

    for letter in letters:
        letter_count[letter] = 0

    return letter_count


def is_pangram(sentence):
    foo = make_dict()

    for bar in sentence.lower():
        if bar.isalpha():
            foo[bar] = foo[bar] + 1

    result = [v for v in foo.values() if v > 0]

    if len(result) == 26:
        return True
    else:
        return False
