import re

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import parsimonious.exceptions

from datatypes import (
    Number,
    String,
    Queue,
    Boolean,
    Block,
)

from identifier import Identifier

IncompleteParseError = parsimonious.exceptions.IncompleteParseError
VisitationError = parsimonious.exceptions.VisitationError

with open("grammar.peg") as f:
    grammar = Grammar(f.read())


class Visitor(NodeVisitor):
    def visit_program(self, node, visited_children):
        return self._flatten(visited_children)

    def visit_statements(self, node, visited_children):
        return self._flatten(visited_children)

    def visit_statement(self, node, visited_children):
        assert len(visited_children) == 1
        return visited_children[0]

    def visit_command(self, node, visited_children):
        assert len(visited_children) == 1
        return Queue(visited_children)

    def visit_string(self, node, visited_children):
        # Drop the wrapping quotes
        contents = node.text[1:-1]
        # Unescape escaped quotes
        literal = String(re.sub(r'\\["bfnrtv\\]', self._unescape_string, contents))
        return Queue([literal])

    def _unescape_string(self, match):
        escape = match.group(0)
        return {
            r'\"': '"',
            r'\b': "\b",
            r'\f': "\f",
            r'\n': "\n",
            r'\r': "\r",
            r'\t': "\t",
            r'\v': "\v",
            r'\\': "\\",
        }.get(escape, escape)

    def visit_number(self, node, visited_children):
        literal = Number(int(node.text))
        return Queue([literal])

    def visit_boolean(self, node, visited_children):
        literal = Boolean(node.text == "true")
        return Queue([literal])

    def visit_identifier(self, node, visited_children):
        literal = Identifier(node.text)
        return Queue([literal])

    def visit_whitespace(self, node, visited_children):
        return Queue([])

    def visit_comment(self, node, visited_children):
        return Queue([])

    def visit_lbracket(self, node, visited_children):
        return Queue([])

    def visit_rbracket(self, node, visited_children):
        return Queue([])

    def visit_block(self, node, visited_children):
        _lbr, *queues, _rbr = visited_children
        return Queue([Block(self._flatten(queues).statements)])

    def generic_visit(self, node, visited_children):
        if node.expr_name == "":
            return self._flatten(visited_children)
        assert False, f"Missing visitor for node type: {node.expr_name}"

    def _flatten(self, visited_children):
        return Queue([stmt for queue in visited_children for stmt in queue.statements])


def parse(text):
    tree = grammar.parse(text)
    return Visitor().visit(tree)
