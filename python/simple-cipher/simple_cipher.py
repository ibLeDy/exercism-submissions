from string import ascii_lowercase
import random


class Cipher(object):
    alpha = ascii_lowercase
    key = ''

    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            key = self.alpha[random.randint(1, 25)]
            while len(self.key) < 32:
                for char in key:
                    self.key += char

    def encode(self, text):
        encoded = ''
        self.check_key(text)

        for i, char in enumerate(text):
            idx = self.alpha.index(self.key[i])
            if idx > 0:
                rot = self.alpha.index(char.lower()) + idx
                if rot <= len(self.alpha) - 1:
                    encoded += self.alpha[rot]
                else:
                    encoded += self.alpha[abs(len(self.alpha) - rot)]
            else:
                encoded += char

        return encoded

    def decode(self, text):
        decoded = ''
        self.check_key(text)

        for i, char in enumerate(text):
            idx = self.alpha.index(self.key[i])
            if idx > 0:
                rot = self.alpha.index(char.lower()) - idx
                decoded += self.alpha[rot]
            else:
                decoded += char

        return decoded

    def check_key(self, text):
        if len(text) > len(self.key):
            diff = len(text) - len(self.key)
            if diff <= len(self.key):
                self.key += self.key[:diff]
            else:
                self.key += self.key * diff
