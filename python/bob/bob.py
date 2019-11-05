def response(text):
    splitted = text.split()

    if text.isupper() and text.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif text.isupper():
        if text.endswith("!"):
            return "Whoa, chill out!"
        else:
            return "Whoa, chill out!"
    elif "?" in text and text.endswith(" "):
        return "Sure."
    elif text.endswith("?"):
        return "Sure."
    elif text[1:].islower():
        return "Whatever."
    elif not text.isalpha():
        result = None
        for word in splitted:
            if word.isalnum():
                return "Whatever."
        return "Fine. Be that way!"
    else:
        return "Whatever."