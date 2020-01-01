def is_valid(isbn):
    result = Isbn(isbn)
    return result.valid


class Isbn:
    def __init__(self, isbn):
        self.isbn = isbn
        self.length = len(isbn)
        self.valid_lengths = [10, 13]
        self.valid = self.apply_formula()

    def apply_formula(self):
        if self.length not in self.valid_lengths:
            return False

        try:
            self.check_character = int(self.isbn[-1])
        except ValueError:
            if self.isbn[-1] == "X":
                self.check_character = 10
                self.isbn = self.isbn[:-1]
            else:
                return False

        if self.length == self.valid_lengths[0]:
            try:
                self.isbn = [int(i) for i in self.isbn]
            except ValueError:
                return False

            self.formula = (self.isbn[0] * 10 + self.isbn[1] * 9 + self.isbn[2] * 8 + self.isbn[3] * 7 + self.isbn[4] * 6 + self.isbn[5] * 5 + self.isbn[6] * 4 + self.isbn[7] * 3 + self.isbn[8] * 2 + self.check_character * 1)

        elif self.length == self.valid_lengths[1]:
            groups = self.isbn.split('-')

            try:
                self.isbn = [int(i) for i in ''.join(groups)]
            except ValueError:
                return False

            if len(groups) != 4:
                return False

            self.formula = (self.isbn[0] * 10 + self.isbn[1] * 9 + self.isbn[2] * 8 + self.isbn[3] * 7 + self.isbn[4] * 6 + self.isbn[5] * 5 + self.isbn[6] * 4 + self.isbn[7] * 3 + self.isbn[8] * 2 + self.check_character * 1)

        return True if self.formula % 11 == 0 else False
