from dataclasses import dataclass

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import parsimonious.exceptions

from datatypes import (
    Identifier,
    Number,
    String,
    Queue
)

IncompleteParseError = parsimonious.exceptions.IncompleteParseError

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
        literal = String(contents.replace(r"\"", '"'))
        return Queue([literal])

    def visit_number(self, node, visited_children):
        literal = Number(node.text)
        return Queue([literal])

    def visit_identifier(self, node, visited_children):
        literal = Identifier(node.text)
        return Queue([literal])

    def visit_whitespace(self, node, visited_children):
        return Queue([])

    def visit_comment(self, node, visited_children):
        return Queue([])

    def generic_visit(self, node, visited_children):
        if node.expr_name == "":
            return self._flatten(visited_children)
        assert False, f"Missing visitor for node type: {node.expr_name}"

    def _flatten(self, visited_children):
        return Queue([stmt for queue in visited_children for stmt in queue.statements])


def parse(text):
    tree = grammar.parse(text)
    return Visitor().visit(tree)
