import string


class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.check_number()
        self.number = self.strip_number()

    def check_number(self):
        chars = [char for char in self.phone_number]
        # fuck me, i don't know regex
        if chars[0] == "(" and chars[1] in "01" or chars[6] in "01":
            raise ValueError("The number is not NANP compliant")
        elif chars[0] == "1" and "(" in chars:
            raise ValueError("The number is not NANP compliant")

    def strip_number(self):
        number = []
        excluded = '!"#$%&\'*,/:;<=>?@[\\]^_`{|}~'
        for char in self.phone_number:
            if char in excluded:
                raise ValueError("The number is not NANP compliant")
            if char not in string.punctuation and char != ' ':
                try:
                    int(char)
                except Exception as e:
                    raise ValueError("The number is not NANP compliant")
                    print("error", e)
                number.append(char)

        if len(number) > 11 or len(number) < 10:
            raise ValueError("The number is not NANP compliant")
        if len(number) == 11 and number[0] != "1":
            raise ValueError("The number is not NANP compliant")

        self.area_code = "".join(number[1:4]) if len(number) == 11 else "".join(number[0:3])
        return "".join(number) if len(number) == 10 else "".join(number[1:])

    def pretty(self):
        number = self.number
        if len(number) == 10:
            return "({}) {}-{}".format(''.join(number[0:3]), ''.join(number[3:6]), ''.join(number[6:]))
        else:
            return "({}) {}-{}".format(''.join(number[1:4]), ''.join(number[4:7]), ''.join(number[7:]))
