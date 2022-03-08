# Generated from BoolExpr.g by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BoolExprParser import BoolExprParser
else:
    from BoolExprParser import BoolExprParser

# This class defines a complete generic visitor for a parse tree produced by BoolExprParser.

class BoolExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BoolExprParser#boolExpr.
    def visitBoolExpr(self, ctx:BoolExprParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoolExprParser#andExpr.
    def visitAndExpr(self, ctx:BoolExprParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoolExprParser#orExpr.
    def visitOrExpr(self, ctx:BoolExprParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoolExprParser#xorExpr.
    def visitXorExpr(self, ctx:BoolExprParser.XorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoolExprParser#unaryExpr.
    def visitUnaryExpr(self, ctx:BoolExprParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoolExprParser#negatedUnary.
    def visitNegatedUnary(self, ctx:BoolExprParser.NegatedUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoolExprParser#atom.
    def visitAtom(self, ctx:BoolExprParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoolExprParser#variable.
    def visitVariable(self, ctx:BoolExprParser.VariableContext):
        return self.visitChildren(ctx)



del BoolExprParser