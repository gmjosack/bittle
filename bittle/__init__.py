
class FlagInst(object):
    def __init__(self, base, initial_value=0):
        self._base = base
        self._value = initial_value

    def _flag_value(self, flag):
        if isinstance(flag, basestring):
            if flag not in self._base.words:
                raise ValueError("%s not a valid flag." % flag)
            return self._base.words[flag]
        return flag

    def load(self, value):
        self._value = value

    def dump(self):
        return self._value

    def set(self, flag):
        flag = self._flag_value(flag)
        self._value |= flag

    def clear(self, flag):
        flag = self._flag_value(flag)
        self._value = self._value & ~flag

    def toggle(self, flag):
        flag = self._flag_value(flag)
        self._value ^= flag

    def clear_all(self):
        self._value = 0

    def has(self, flags):
        # Flags can be or'd here. If you pass in a string
        # then you can only check a single flag.
        flags = self._flag_value(flags)
        return (self._value & flags) != 0

    def __getattr__(self, name):
        return self._base.words[name]

    def __getitem__(self, key):
        return self._base.words[key]


class FlagWord(object):
    def __init__(self, words):
        self.words = {}
        for idx, word in enumerate(words):
            self.words[word] = 2 ** idx
        self.values = set(self.words.values())

    def __call__(self, initial_value=0):
        return FlagInst(self, initial_value)

    def __getattr__(self, name):
        return self.words[name]

    def __getitem__(self, key):
        return self.words[key]
