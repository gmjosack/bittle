
class FlagWord(object):
    def __init__(self, words, initial_value=0):
        self._words = {}
        for idx, word in enumerate(words):
            self._words[word] = 2 ** idx
        self._value = initial_value

    def __getattr__(self, name):
        return self._words[name]

    def __getitem__(self, key):
        return self._words[key]

    def load(self, value):
        self._value = value

    def dump(self):
        return self._value

    def set(self, flag):
        self._value |= flag

    def clear(self, flag):
        self._value = self._value & ~flag

    def toggle(self, flag):
        self._value ^= flag

    def clear_all(self):
        self._value = 0

    def has(self, flags):
        return (self._value & flags) != 0

