import textwrap
import unittest

import parser


class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parser.parse("").text, "")

    def test_identifiers(self):
        accepted = ["foo", "x", "λ"]
        for ident in accepted:
            self.assertEqual(parser.parse(ident).text, ident)

        # Because `literal` comes before `identifier` in the expression rule,
        # numeric literals have priority over identifiers.
        rejected = ["123abc"]
        for ident in rejected:
            with self.assertRaises(parser.IncompleteParseError):
                parser.parse(ident)

    def test_strings(self):
        accepted = ['"Hello, world!"', '""', r'"backslash-escaped quote \" characters"']
        for string in accepted:
            self.assertEqual(parser.parse(string).text, string)

        rejected = ['"unterminated string']
        for string in rejected:
            with self.assertRaises(parser.IncompleteParseError):
                parser.parse(string)

    def test_numbers(self):
        accepted = ["0", "1", "123", "123.321", "12.0", "-1", "-0", "-123.321", "-12.0"]
        for number in accepted:
            self.assertEqual(parser.parse(number).text, number)

        rejected = ["0.", ".0"]
        for number in rejected:
            with self.assertRaises(parser.IncompleteParseError):
                parser.parse(number)

    def test_simple_math_1(self):
        source = textwrap.dedent(
            """\
            1
            1
            +
            3
            -
            """
        )
        parser.parse(source)

    def test_simple_math_2(self):
        source = textwrap.dedent(
            """\
            1
            1
            3
            # [ 1 1 3 ]
            +
            # [ 3 2 ]
            -
            # [ 1 ]
            """
        )
        parser.parse(source)


if __name__ == "__main__":
    unittest.main()
