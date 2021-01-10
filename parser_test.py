import textwrap
import unittest

import parser


class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parser.parse(""), parser.Queue([]))

    def test_identifiers(self):
        accepted = ["foo", "x", "λ"]
        for ident in accepted:
            actual = parser.parse(ident)
            expected = parser.Queue([parser.Identifier(ident)])
            self.assertEqual(actual, expected)

        # Because `literal` comes before `identifier` in the expression rule,
        # numeric literals have priority over identifiers.
        rejected = ["123abc"]
        for ident in rejected:
            with self.assertRaises(parser.IncompleteParseError):
                parser.parse(ident)

    def test_strings(self):
        accepted = {
            '"Hello, world!"': "Hello, world!",
            '""': "",
            r'"backslash-escaped quote \" characters"': 'backslash-escaped quote " characters',
        }
        for source, contents in accepted.items():
            actual = parser.parse(source)
            expected = parser.Queue([parser.String(contents)])
            self.assertEqual(actual, expected)

        rejected = ['"unterminated string']
        for string in rejected:
            with self.assertRaises(parser.IncompleteParseError):
                parser.parse(string)

    def test_numbers(self):
        accepted = ["0", "1", "123", "123.321", "12.0", "-1", "-0", "-123.321", "-12.0"]
        for number in accepted:
            actual = parser.parse(number)
            expected = parser.Queue([parser.Number(number)])
            self.assertEqual(actual, expected)

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
        actual = parser.parse(source)
        expected = parser.Queue(
            [
                parser.Number("1"),
                parser.Number("1"),
                parser.Identifier("+"),
                parser.Number("3"),
                parser.Identifier("-"),
            ]
        )
        self.assertEqual(actual, expected)

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
        actual = parser.parse(source)
        expected = parser.Queue(
            [
                parser.Number("1"),
                parser.Number("1"),
                parser.Number("3"),
                parser.Identifier("+"),
                parser.Identifier("-"),
            ]
        )
        print(actual)
        print(expected)
        self.assertEqual(actual, expected)

    def test_single_number(self):
        actual = parser.parse("1")
        expected = parser.Queue([parser.Number("1")])
        self.assertEqual(actual, expected)

    def test_comment(self):
        actual = parser.parse("# I am a comment")
        expected = parser.Queue([])
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
