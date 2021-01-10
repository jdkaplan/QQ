import textwrap
import unittest

import parser
import identifier
import math_operations


class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertQueue(parser.parse(""), parser.Queue([]))

    def test_identifiers(self):
        accepted = identifier.identifiers
        for ident in accepted:
            with self.subTest(ident):
                actual = parser.parse(ident)
                expected = parser.Queue([parser.Identifier(ident)])
                self.assertQueue(actual, expected)

    def test_unknown_identifier(self):
        with self.assertRaises(parser.VisitationError):
            parser.parse("func")

    def test_unparseable_identifier(self):
        with self.assertRaises(parser.IncompleteParseError):
            parser.parse("123abc")

    def test_strings(self):
        accepted = {
            '"Hello, world!"': "Hello, world!",
            '""': "",
            r'"backslash-escaped quote \" characters"': 'backslash-escaped quote " characters',
            r'"\b\f\n\r\t\v\\"': "\b\f\n\r\t\v\\",
        }
        for source, contents in accepted.items():
            with self.subTest(source):
                actual = parser.parse(source)
                expected = parser.Queue([parser.String(contents)])
                self.assertQueue(actual, expected)

        rejected = ['"unterminated string']
        for string in rejected:
            with self.subTest(string):
                with self.assertRaises(parser.IncompleteParseError):
                    parser.parse(string)

    def test_numbers(self):
        accepted = ["0", "1", "123", "123.321", "12.0", "-1", "-0", "-123.321", "-12.0"]
        for number in accepted:
            actual = parser.parse(number)
            expected = parser.Queue([parser.Number(number)])
            self.assertQueue(actual, expected)

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
                math_operations.Add(),
                parser.Number("3"),
                math_operations.Sub(),
            ]
        )
        self.assertQueue(actual, expected)

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
        self.assertQueue(actual, expected)

    def test_single_number(self):
        actual = parser.parse("1")
        expected = parser.Queue([parser.Number("1")])
        self.assertQueue(actual, expected)

    def test_comment(self):
        source = textwrap.dedent(
            """\
            1 print # I am a comment
            """
        )
        actual = parser.parse(source)
        expected = parser.Queue([parser.Number("1"), parser.Identifier("print")])
        self.assertQueue(actual, expected)

    def test_comments_are_not_identifiers(self):
        actual = parser.parse("# I am a comment")
        expected = parser.Queue([])
        self.assertQueue(actual, expected)

    def assertQueue(self, actual, expected):
        assert type(actual) == type(expected), f"Expected #{type(expected)} got #{type(actual)}"
        self.assertEqual(actual.statements, expected.statements)


if __name__ == "__main__":
    unittest.main()
