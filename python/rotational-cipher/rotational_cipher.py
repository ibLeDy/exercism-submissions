from string import ascii_lowercase


def rotate(text, key):
    result = ''
    for char in text:
        if char.lower() not in ascii_lowercase:
            result += char
            continue

        idx = ascii_lowercase.index(char.lower()) + key
        if idx >= 26:
            idx = idx - 26

        new_letter = ascii_lowercase[idx]
        if char.isupper():
            new_letter = new_letter.upper()

        result += new_letter

    return result
