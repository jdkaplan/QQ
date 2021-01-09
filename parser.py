from dataclasses import dataclass

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import parsimonious.exceptions

IncompleteParseError = parsimonious.exceptions.IncompleteParseError

with open("grammar.peg") as f:
    grammar = Grammar(f.read())


@dataclass(frozen=True)
class Statement:
    pass


@dataclass(frozen=True)
class Identifier:
    name: str


@dataclass(frozen=True)
class Expression:
    pass


@dataclass(frozen=True)
class Command(Expression):
    pass


@dataclass(frozen=True)
class Program:
    statements: list[Statement]


class Visitor(NodeVisitor):
    # def visit_program(self, node, visited_children):
    #     return Program(node.children)

    # def visit_identifier(self, node, _visited_children):
    #     return Identifier(node.text)

    # def visit_expression(self, node, visited_children):
    #     return Expression(visited_children)

    def generic_visit(self, node, visited_children):
        return node


def parse(text):
    tree = grammar.parse(text)
    return Visitor().visit(tree)
