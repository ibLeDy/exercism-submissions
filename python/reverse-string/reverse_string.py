def reverse(text):
    new_text = ''
    idx = len(text) - 1
    while idx >= 0:
        new_text += text[idx]
        idx -= 1
    return new_text
