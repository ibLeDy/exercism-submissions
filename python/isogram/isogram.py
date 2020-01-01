import string


def is_isogram(text):

    if not isinstance(text, str):
        return False
    elif text == "":
        return True
    elif len(text) < 1:
        return False

    punc = string.punctuation
    s = list(text.lower())

    word = ''.join([o for o in s if o not in punc])
    word = ''.join(word.strip().split())

    if len(word) == len(set(word)):
        return True
    else:
        return False
