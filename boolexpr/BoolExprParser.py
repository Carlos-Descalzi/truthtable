# Generated from BoolExpr.g by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4")
        buf.write("\3\4\5\4\35\n\4\3\5\3\5\3\5\5\5\"\n\5\3\6\3\6\5\6&\n\6")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b\60\n\b\3\t\3\t\3")
        buf.write("\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2\60\2\22\3\2\2\2\4\24")
        buf.write("\3\2\2\2\6\31\3\2\2\2\b\36\3\2\2\2\n%\3\2\2\2\f\'\3\2")
        buf.write("\2\2\16/\3\2\2\2\20\61\3\2\2\2\22\23\5\4\3\2\23\3\3\2")
        buf.write("\2\2\24\27\5\6\4\2\25\26\7\b\2\2\26\30\5\2\2\2\27\25\3")
        buf.write("\2\2\2\27\30\3\2\2\2\30\5\3\2\2\2\31\34\5\b\5\2\32\33")
        buf.write("\7\t\2\2\33\35\5\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\7\3\2\2\2\36!\5\n\6\2\37 \7\7\2\2 \"\5\2\2\2!\37\3\2")
        buf.write("\2\2!\"\3\2\2\2\"\t\3\2\2\2#&\5\16\b\2$&\5\f\7\2%#\3\2")
        buf.write("\2\2%$\3\2\2\2&\13\3\2\2\2\'(\7\6\2\2()\5\16\b\2)\r\3")
        buf.write("\2\2\2*\60\5\20\t\2+,\7\4\2\2,-\5\4\3\2-.\7\5\2\2.\60")
        buf.write("\3\2\2\2/*\3\2\2\2/+\3\2\2\2\60\17\3\2\2\2\61\62\7\3\2")
        buf.write("\2\62\21\3\2\2\2\7\27\34!%/")
        return buf.getvalue()


class BoolExprParser ( Parser ):

    grammarFileName = "BoolExpr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'~'", "'^'", 
                     "'&'", "'|'" ]

    symbolicNames = [ "<INVALID>", "VARIABLE", "LPAR", "RPAR", "NOT", "XOR", 
                      "AND", "OR", "WS" ]

    RULE_boolExpr = 0
    RULE_andExpr = 1
    RULE_orExpr = 2
    RULE_xorExpr = 3
    RULE_unaryExpr = 4
    RULE_negatedUnary = 5
    RULE_atom = 6
    RULE_variable = 7

    ruleNames =  [ "boolExpr", "andExpr", "orExpr", "xorExpr", "unaryExpr", 
                   "negatedUnary", "atom", "variable" ]

    EOF = Token.EOF
    VARIABLE=1
    LPAR=2
    RPAR=3
    NOT=4
    XOR=5
    AND=6
    OR=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self):
            return self.getTypedRuleContext(BoolExprParser.AndExprContext,0)


        def getRuleIndex(self):
            return BoolExprParser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)




    def boolExpr(self):

        localctx = BoolExprParser.BoolExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_boolExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.andExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # OrExprContext
            self.right = None # BoolExprContext

        def orExpr(self):
            return self.getTypedRuleContext(BoolExprParser.OrExprContext,0)


        def AND(self):
            return self.getToken(BoolExprParser.AND, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(BoolExprParser.BoolExprContext,0)


        def getRuleIndex(self):
            return BoolExprParser.RULE_andExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = BoolExprParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_andExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            localctx.left = self.orExpr()
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 19
                self.match(BoolExprParser.AND)
                self.state = 20
                localctx.right = self.boolExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # XorExprContext
            self.right = None # BoolExprContext

        def xorExpr(self):
            return self.getTypedRuleContext(BoolExprParser.XorExprContext,0)


        def OR(self):
            return self.getToken(BoolExprParser.OR, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(BoolExprParser.BoolExprContext,0)


        def getRuleIndex(self):
            return BoolExprParser.RULE_orExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = BoolExprParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_orExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            localctx.left = self.xorExpr()
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 24
                self.match(BoolExprParser.OR)
                self.state = 25
                localctx.right = self.boolExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XorExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # UnaryExprContext
            self.right = None # BoolExprContext

        def unaryExpr(self):
            return self.getTypedRuleContext(BoolExprParser.UnaryExprContext,0)


        def XOR(self):
            return self.getToken(BoolExprParser.XOR, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(BoolExprParser.BoolExprContext,0)


        def getRuleIndex(self):
            return BoolExprParser.RULE_xorExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorExpr" ):
                listener.enterXorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorExpr" ):
                listener.exitXorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXorExpr" ):
                return visitor.visitXorExpr(self)
            else:
                return visitor.visitChildren(self)




    def xorExpr(self):

        localctx = BoolExprParser.XorExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_xorExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            localctx.left = self.unaryExpr()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoolExprParser.XOR:
                self.state = 29
                self.match(BoolExprParser.XOR)
                self.state = 30
                localctx.right = self.boolExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.at = None # AtomContext
            self.neg = None # NegatedUnaryContext

        def atom(self):
            return self.getTypedRuleContext(BoolExprParser.AtomContext,0)


        def negatedUnary(self):
            return self.getTypedRuleContext(BoolExprParser.NegatedUnaryContext,0)


        def getRuleIndex(self):
            return BoolExprParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = BoolExprParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unaryExpr)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BoolExprParser.VARIABLE, BoolExprParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                localctx.at = self.atom()
                pass
            elif token in [BoolExprParser.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                localctx.neg = self.negatedUnary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegatedUnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.at = None # AtomContext

        def NOT(self):
            return self.getToken(BoolExprParser.NOT, 0)

        def atom(self):
            return self.getTypedRuleContext(BoolExprParser.AtomContext,0)


        def getRuleIndex(self):
            return BoolExprParser.RULE_negatedUnary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegatedUnary" ):
                listener.enterNegatedUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegatedUnary" ):
                listener.exitNegatedUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegatedUnary" ):
                return visitor.visitNegatedUnary(self)
            else:
                return visitor.visitChildren(self)




    def negatedUnary(self):

        localctx = BoolExprParser.NegatedUnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_negatedUnary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(BoolExprParser.NOT)
            self.state = 38
            localctx.at = self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var = None # VariableContext
            self.and_expr = None # AndExprContext

        def variable(self):
            return self.getTypedRuleContext(BoolExprParser.VariableContext,0)


        def LPAR(self):
            return self.getToken(BoolExprParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(BoolExprParser.RPAR, 0)

        def andExpr(self):
            return self.getTypedRuleContext(BoolExprParser.AndExprContext,0)


        def getRuleIndex(self):
            return BoolExprParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BoolExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BoolExprParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                localctx.var = self.variable()
                pass
            elif token in [BoolExprParser.LPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(BoolExprParser.LPAR)
                self.state = 42
                localctx.and_expr = self.andExpr()
                self.state = 43
                self.match(BoolExprParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def VARIABLE(self):
            return self.getToken(BoolExprParser.VARIABLE, 0)

        def getRuleIndex(self):
            return BoolExprParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BoolExprParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            localctx.name = self.match(BoolExprParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





