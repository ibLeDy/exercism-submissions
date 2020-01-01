# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = ['_'] * len(word)
        self.guesses = {}

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Game over!")

        if char not in self.word or char in self.guesses.keys():
            self.remaining_guesses -= 1
            if self.remaining_guesses == -1:
                self.status = STATUS_LOSE
        else:
            self.guesses[char] = True
            indices = [i for i, letter in enumerate(self.word) if letter == char]

            for idx in indices:
                self.masked_word[idx] = char

            if ''.join(self.masked_word) == self.word:
                self.status = STATUS_WIN

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status
