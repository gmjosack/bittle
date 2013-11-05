import unittest

from bittle import FlagWord


class FlagWordTest(unittest.TestCase):
    def setUp(self):
        self.test_flags = FlagWord(["foo", "bar", "baz"])

    def test_flags(self):
        flags = self.test_flags

        self.assertFalse(flags.has(flags.foo))
        self.assertFalse(flags.has(flags.bar))
        self.assertFalse(flags.has(flags.baz))

        flags.set(flags.foo)
        self.assertTrue(flags.has(flags.foo))
        self.assertFalse(flags.has(flags.bar))
        self.assertFalse(flags.has(flags.baz))

        flags.toggle(flags.foo)
        flags.toggle(flags.bar)
        flags.toggle(flags.baz)
        self.assertFalse(flags.has(flags.foo))
        self.assertTrue(flags.has(flags.bar))
        self.assertTrue(flags.has(flags.baz))

        flags.clear(flags.baz)
        self.assertFalse(flags.has(flags.foo))
        self.assertTrue(flags.has(flags.bar))
        self.assertFalse(flags.has(flags.baz))

        self.assertFalse(flags.has(flags.foo | flags.baz))
        self.assertTrue(flags.has(flags.foo | flags.bar))
        self.assertTrue(flags.has(flags.baz | flags.bar))

    def test_clear_all(self):
        flags = self.test_flags

        flags.set(flags.foo)
        self.assertNotEqual(flags.dump(), 0)

        flags.clear_all()
        self.assertEqual(flags.dump(), 0)


if __name__ == "__main__":
    unittest.main()
