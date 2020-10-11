from string import ascii_lowercase


def add_spaces(text):
    spaced_text = ''
    for i, char in enumerate(text, 1):
        spaced_text += char
        if i % 5 == 0:
            spaced_text += ' '
    return spaced_text.strip()


def cipher(text, action):
    result = ''
    for char in text:
        if char.isalpha():
            idx = ascii_lowercase.index(char.lower()) + 1
            result += ascii_lowercase[len(ascii_lowercase) - idx]
        elif char.isnumeric():
            result += char
    if action == 'encode':
        result = add_spaces(result)
    return result


def encode(plain_text):
    return cipher(plain_text, 'encode')


def decode(ciphered_text):
    return cipher(ciphered_text, 'decode')
