from string import ascii_uppercase as letters


def abbreviate(words):
    splitted = words.split()
    acronym = []

    for word in splitted:
        for letter in word:
            letter = letter.upper()
            if letter in letters:
                acronym.append(letter)
                break

        if "-" in word and "-" != word:
            acronym.append(word.split("-")[-1][0].upper())

    return "".join(acronym)
