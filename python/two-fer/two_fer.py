def two_fer(name=""):
    if name != "":
        sentence = ("One for {}, one for me.".format(name))
    else:
        sentence = ("One for you, one for me.")
    return sentence
