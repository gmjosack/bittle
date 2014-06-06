#!/usr/bin/env python

import unittest

from bittle import FlagWord

Flags = FlagWord(["foo", "bar", "baz"])


class FlagWordTest(unittest.TestCase):
    def setUp(self):
        self.test_flags = Flags()

    def test_flags(self):
        flags = self.test_flags

        self.assertFalse(flags.has(flags.foo))
        self.assertFalse(flags.has(Flags.bar))
        self.assertFalse(flags.has("baz"))

        flags.set(flags.foo)
        self.assertTrue(flags.has(flags.foo))
        self.assertFalse(flags.has(flags.bar))
        self.assertFalse(flags.has(flags.baz))

        flags.toggle(flags.foo)
        flags.toggle(Flags.bar)
        flags.toggle("baz")
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

        flags.set("foo")
        self.assertNotEqual(flags.dump(), 0)

        flags.clear_all()
        self.assertEqual(flags.dump(), 0)


if __name__ == "__main__":
    unittest.main()
