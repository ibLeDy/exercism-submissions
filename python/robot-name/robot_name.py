import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"


class Robot(object):
    def __init__(self):
        self.name = self.create_name()

    def reset(self):
        random.seed("Is this random?")
        self.name = self.create_name()

    def create_name(self):
        name = [random.choice(letters),
                random.choice(letters),
                random.choice(numbers),
                random.choice(numbers),
                random.choice(numbers)]

        result = "".join(name)
        return result
