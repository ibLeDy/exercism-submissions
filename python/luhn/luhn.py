import string


class Luhn:
    def __init__(self, card_num):
        self.passed = True
        self.num = self.prepare(card_num)

    def valid(self):
        if self.passed:
            if len(self.num) <= 1:
                return False

            if sum(self.operate()) % 10 == 0:
                return True

            return False

        return False

    def prepare(self, card_num):
        splitted = card_num.split(" ")
        if any(str(i) in string.punctuation for i in card_num):
            self.passed = False
        elif not all(str(i) in string.digits for i in card_num.replace(" ", "")):
            self.passed = False

        return "".join(splitted)[::-1]

    def operate(self):
        numbers = [int(i) for i in self.num]
        factors = [1 if i % 2 == 0 else 2 for i, v in enumerate(self.num)]

        multiplied = []
        for i, f in enumerate(factors):
            operation = numbers[i] * f
            if operation > 9:
                operation -= 9
            multiplied.append(operation)

        return multiplied
