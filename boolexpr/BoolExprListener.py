# Generated from BoolExpr.g by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BoolExprParser import BoolExprParser
else:
    from BoolExprParser import BoolExprParser

# This class defines a complete listener for a parse tree produced by BoolExprParser.
class BoolExprListener(ParseTreeListener):

    # Enter a parse tree produced by BoolExprParser#boolExpr.
    def enterBoolExpr(self, ctx:BoolExprParser.BoolExprContext):
        pass

    # Exit a parse tree produced by BoolExprParser#boolExpr.
    def exitBoolExpr(self, ctx:BoolExprParser.BoolExprContext):
        pass


    # Enter a parse tree produced by BoolExprParser#andExpr.
    def enterAndExpr(self, ctx:BoolExprParser.AndExprContext):
        pass

    # Exit a parse tree produced by BoolExprParser#andExpr.
    def exitAndExpr(self, ctx:BoolExprParser.AndExprContext):
        pass


    # Enter a parse tree produced by BoolExprParser#orExpr.
    def enterOrExpr(self, ctx:BoolExprParser.OrExprContext):
        pass

    # Exit a parse tree produced by BoolExprParser#orExpr.
    def exitOrExpr(self, ctx:BoolExprParser.OrExprContext):
        pass


    # Enter a parse tree produced by BoolExprParser#xorExpr.
    def enterXorExpr(self, ctx:BoolExprParser.XorExprContext):
        pass

    # Exit a parse tree produced by BoolExprParser#xorExpr.
    def exitXorExpr(self, ctx:BoolExprParser.XorExprContext):
        pass


    # Enter a parse tree produced by BoolExprParser#unaryExpr.
    def enterUnaryExpr(self, ctx:BoolExprParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by BoolExprParser#unaryExpr.
    def exitUnaryExpr(self, ctx:BoolExprParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by BoolExprParser#negatedUnary.
    def enterNegatedUnary(self, ctx:BoolExprParser.NegatedUnaryContext):
        pass

    # Exit a parse tree produced by BoolExprParser#negatedUnary.
    def exitNegatedUnary(self, ctx:BoolExprParser.NegatedUnaryContext):
        pass


    # Enter a parse tree produced by BoolExprParser#atom.
    def enterAtom(self, ctx:BoolExprParser.AtomContext):
        pass

    # Exit a parse tree produced by BoolExprParser#atom.
    def exitAtom(self, ctx:BoolExprParser.AtomContext):
        pass


    # Enter a parse tree produced by BoolExprParser#variable.
    def enterVariable(self, ctx:BoolExprParser.VariableContext):
        pass

    # Exit a parse tree produced by BoolExprParser#variable.
    def exitVariable(self, ctx:BoolExprParser.VariableContext):
        pass



del BoolExprParser