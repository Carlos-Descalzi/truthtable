from .boolexpr import BoolExprVisitor, BoolExprParser, BoolExprLexer
from abc import ABCMeta, abstractmethod, abstractproperty
import antlr4
import sys


class Operator:
    def __init__(self, name, operator):
        self._name = name
        self._operator = operator

    def __call__(self, *args):
        return self._operator(*args)

    def __str__(self):
        return self._name


AND = Operator("&", lambda x, y: x.value & y.value)
OR = Operator("|", lambda x, y: x.value | y.value)
XOR = Operator("^", lambda x, y: x.value ^ y.value)
NOT = Operator("~", lambda x: not x.value)


class Node(metaclass=ABCMeta):
    def variables(self):
        variables = []

        for child in self.children:
            if isinstance(child, Variable):
                variables.append(child)
            else:
                variables += child.variables()

        return variables

    @abstractproperty
    def terms(self):
        pass

    @abstractproperty
    def children(self):
        pass

    @abstractmethod
    def value(self):
        pass

    def __repr__(self):
        return str(self)

    def __id__(self):
        return id(str(self))

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)

    @abstractproperty
    def order(self):
        pass


class BinaryExpr(Node):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

    @property
    def value(self):
        return self.operator(self.left, self.right)

    @property
    def children(self):
        return [self.left, self.right]

    @property
    def terms(self):
        return self.left.terms + self.right.terms + [self]

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"

    @property
    def order(self):
        return max([c.order for c in self.children]) + 1


class Separator(Node):
    def __init__(self, child):
        self.child = child

    @property
    def value(self):
        return self.child.value

    @property
    def children(self):
        return [self.child]

    @property
    def terms(self):
        return self.child.terms

    def __str__(self):
        return f"( {self.child} )"

    @property
    def order(self):
        return self.child.order + 1


class UnaryExpr(Node):
    def __init__(self, child, operator):
        self.child = child
        self.operator = operator

    @property
    def value(self):
        return self.operator(self.child)

    @property
    def children(self):
        return [self.child]

    @property
    def terms(self):
        return [self] + self.child.terms

    def __str__(self):
        return f"{self.operator} {self.child}"

    @property
    def order(self):
        return self.child.order + 1


class Variable(Node):
    def __init__(self, variable):
        self.variable = variable
        self._value = 0

    def __str__(self):
        return self.variable

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    value = property(get_value, set_value)

    @property
    def terms(self):
        return [self]

    @property
    def children(self):
        return []

    @property
    def order(self):
        return 0


class Visitor(BoolExprVisitor.BoolExprVisitor):
    def __init__(self):
        super().__init__()
        self._variables_dict = {}
        self._expr_dict = {}

    def visit_all(self, ctx):
        return self.visitBoolExpr(ctx), list(self._variables_dict.values())

    def visitAndExpr(self, ctx):
        if ctx.right:
            return BinaryExpr(self.visit(ctx.left), self.visit(ctx.right), AND)
        return self.visit(ctx.left)

    def visitOrExpr(self, ctx):
        if ctx.right:
            return BinaryExpr(self.visit(ctx.left), self.visit(ctx.right), OR)
        return self.visit(ctx.left)

    def visitXorExpr(self, ctx):
        if ctx.right:
            return BinaryExpr(self.visit(ctx.left), self.visit(ctx.right), XOR)
        return self.visit(ctx.left)

    def visitUnaryExpr(self, ctx):
        if ctx.neg:
            return self.visit(ctx.neg)
        return self.visit(ctx.at)

    def visitNegatedUnary(self, ctx):
        return UnaryExpr(self.visit(ctx.at), NOT)

    def visitAtom(self, ctx):

        if ctx.and_expr:
            return Separator(self.visit(ctx.and_expr))
        return self.visit(ctx.var)

    def visitVariable(self, ctx):
        if ctx.name.text in self._variables_dict:
            return self._variables_dict[ctx.name.text]

        variable = Variable(ctx.name.text)
        self._variables_dict[ctx.name.text] = variable
        return variable


def get_tree(input_stream):
    lexer = BoolExprLexer.BoolExprLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = BoolExprParser.BoolExprParser(tokens)
    return parser.boolExpr()


def main():
    if len(sys.argv) != 2:
        print('Usage: truthtable "boolean expression"')
        sys.exit(1)

    input_stream = antlr4.InputStream(sys.argv[1])
    visitor = Visitor()
    root, variables_list = visitor.visit_all(get_tree(input_stream))
    variables = list(sorted(variables_list, key=lambda x: x.variable))

    possible_values = 2 ** len(variables)

    terms = list(sorted(filter(lambda x: x != root and x not in variables, set(root.terms)), key=lambda x: x.order))

    all_items = variables + terms + [root]

    header_str = " | ".join(map(str, all_items))
    print(header_str)
    print("-" * len(header_str))

    fmt_val = lambda l, v: " " * (l - 1) + ("1" if v else "0")

    for i in range(possible_values):

        for n, var in enumerate(variables):
            # Assign values to variables
            var.value = (i & (1 << (len(variables) - n - 1))) != 0

        # ... and print the values
        print(" | ".join([fmt_val(len(str(v)), v.value) for v in all_items]))


if __name__ == "__main__":
    main()
