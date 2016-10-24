# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .FOLVisitor import FOLVisitor
else:
    from FOLVisitor import FOLVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3(")
        buf.write("\u0085\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2\35\n\2\f\2\16\2 \13\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write("\'\n\2\f\2\16\2*\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\5\2\64\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\7\2F\n\2\f\2\16\2I\13\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3T\n\3\f\3\16\3W\13\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3^\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4g\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4r\n")
        buf.write("\4\f\4\16\4u\13\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\13\2\4\2\6\f\2\4\6\b\n\f\16\20")
        buf.write("\22\24\2\16\3\2\32\37\3\2\6\7\3\2\b\t\3\2\"#\3\2 !\3\2")
        buf.write("\n\r\3\2\16\17\3\2\20\21\3\2\22\23\3\2\24\25\3\2\26\27")
        buf.write("\3\2\30\31\u008e\2\63\3\2\2\2\4]\3\2\2\2\6f\3\2\2\2\b")
        buf.write("v\3\2\2\2\nx\3\2\2\2\fz\3\2\2\2\16|\3\2\2\2\20~\3\2\2")
        buf.write("\2\22\u0080\3\2\2\2\24\u0082\3\2\2\2\26\27\b\2\1\2\27")
        buf.write("\30\5\b\5\2\30\31\5\2\2\13\31\64\3\2\2\2\32\36\5\n\6\2")
        buf.write("\33\35\7%\2\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2")
        buf.write("\36\37\3\2\2\2\37!\3\2\2\2 \36\3\2\2\2!\"\7\3\2\2\"#\5")
        buf.write("\2\2\6#\64\3\2\2\2$(\5\f\7\2%\'\7%\2\2&%\3\2\2\2\'*\3")
        buf.write("\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*(\3\2\2\2+,\7\3\2")
        buf.write("\2,-\5\2\2\5-\64\3\2\2\2.\64\5\4\3\2/\60\7\4\2\2\60\61")
        buf.write("\5\2\2\2\61\62\7\5\2\2\62\64\3\2\2\2\63\26\3\2\2\2\63")
        buf.write("\32\3\2\2\2\63$\3\2\2\2\63.\3\2\2\2\63/\3\2\2\2\64G\3")
        buf.write("\2\2\2\65\66\f\n\2\2\66\67\5\22\n\2\678\5\2\2\138F\3\2")
        buf.write("\2\29:\f\t\2\2:;\5\24\13\2;<\5\2\2\n<F\3\2\2\2=>\f\b\2")
        buf.write("\2>?\5\16\b\2?@\5\2\2\b@F\3\2\2\2AB\f\7\2\2BC\5\20\t\2")
        buf.write("CD\5\2\2\bDF\3\2\2\2E\65\3\2\2\2E9\3\2\2\2E=\3\2\2\2E")
        buf.write("A\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\3\3\2\2\2IG\3")
        buf.write("\2\2\2JK\5\6\4\2KL\t\2\2\2LM\5\6\4\2M^\3\2\2\2NO\7&\2")
        buf.write("\2OP\7\4\2\2PU\5\6\4\2QR\7\3\2\2RT\5\6\4\2SQ\3\2\2\2T")
        buf.write("W\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7")
        buf.write("\5\2\2Y^\3\2\2\2Z^\7&\2\2[^\t\3\2\2\\^\t\4\2\2]J\3\2\2")
        buf.write("\2]N\3\2\2\2]Z\3\2\2\2][\3\2\2\2]\\\3\2\2\2^\5\3\2\2\2")
        buf.write("_`\b\4\1\2`a\7\4\2\2ab\5\6\4\2bc\7\5\2\2cg\3\2\2\2dg\7")
        buf.write("%\2\2eg\7\'\2\2f_\3\2\2\2fd\3\2\2\2fe\3\2\2\2gs\3\2\2")
        buf.write("\2hi\f\b\2\2ij\t\5\2\2jr\5\6\4\tkl\f\7\2\2lm\7$\2\2mr")
        buf.write("\5\6\4\bno\f\6\2\2op\t\6\2\2pr\5\6\4\7qh\3\2\2\2qk\3\2")
        buf.write("\2\2qn\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2t\7\3\2\2")
        buf.write("\2us\3\2\2\2vw\t\7\2\2w\t\3\2\2\2xy\t\b\2\2y\13\3\2\2")
        buf.write("\2z{\t\t\2\2{\r\3\2\2\2|}\t\n\2\2}\17\3\2\2\2~\177\t\13")
        buf.write("\2\2\177\21\3\2\2\2\u0080\u0081\t\f\2\2\u0081\23\3\2\2")
        buf.write("\2\u0082\u0083\t\r\2\2\u0083\25\3\2\2\2\f\36(\63EGU]f")
        buf.write("qs")
        return buf.getvalue()


class FOLParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"'('", u"')'", u"'true'", u"'True'", 
                     u"'false'", u"'False'", u"'not'", u"'neg'", u"'~'", 
                     u"'¬'", u"'∃'", u"'exists'", u"'∀'", u"'forall'", u"'→'", 
                     u"'->'", u"'↔'", u"'<->'", u"'∧'", u"'and'", u"'∨'", 
                     u"'or'", u"'<'", u"'>'", u"'>='", u"'<='", u"'='", 
                     u"'!='", u"'+'", u"'-'", u"'*'", u"'/'", u"'%'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"LT", u"GT", u"GE", u"LE", u"EQ", u"NE", u"ADD", 
                      u"SUB", u"MUL", u"DIV", u"MOD", u"ID", u"PRED", u"INT", 
                      u"WD" ]

    RULE_formula = 0
    RULE_atom = 1
    RULE_term = 2
    RULE_neg = 3
    RULE_exists_op = 4
    RULE_forall_op = 5
    RULE_impl_op = 6
    RULE_iff_op = 7
    RULE_and_op = 8
    RULE_or_op = 9

    ruleNames =  [ "formula", "atom", "term", "neg", "exists_op", "forall_op", 
                   "impl_op", "iff_op", "and_op", "or_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    LT=24
    GT=25
    GE=26
    LE=27
    EQ=28
    NE=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MOD=34
    ID=35
    PRED=36
    INT=37
    WD=38

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def neg(self):
            return self.getTypedRuleContext(FOLParser.NegContext,0)

        def formula(self):
            return self.getTypedRuleContext(FOLParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class IffContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FOLParser.FormulaContext,i)

        def iff_op(self):
            return self.getTypedRuleContext(FOLParser.Iff_opContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitIff(self)
            else:
                return visitor.visitChildren(self)


    class ImplContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FOLParser.FormulaContext,i)

        def impl_op(self):
            return self.getTypedRuleContext(FOLParser.Impl_opContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitImpl(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FOLParser.FormulaContext,i)

        def or_op(self):
            return self.getTypedRuleContext(FOLParser.Or_opContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class ForAllContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def forall_op(self):
            return self.getTypedRuleContext(FOLParser.Forall_opContext,0)

        def formula(self):
            return self.getTypedRuleContext(FOLParser.FormulaContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(FOLParser.ID)
            else:
                return self.getToken(FOLParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitForAll(self)
            else:
                return visitor.visitChildren(self)


    class ExistsContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def exists_op(self):
            return self.getTypedRuleContext(FOLParser.Exists_opContext,0)

        def formula(self):
            return self.getTypedRuleContext(FOLParser.FormulaContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(FOLParser.ID)
            else:
                return self.getToken(FOLParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitExists(self)
            else:
                return visitor.visitChildren(self)


    class FormulaParensContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(FOLParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitFormulaParens(self)
            else:
                return visitor.visitChildren(self)


    class FormulaAtomContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(FOLParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitFormulaAtom(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.FormulaContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FOLParser.FormulaContext,i)

        def and_op(self):
            return self.getTypedRuleContext(FOLParser.And_opContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FOLParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = FOLParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.neg()
                self.state = 22
                self.formula(9)
                pass

            elif la_ == 2:
                localctx = FOLParser.ExistsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.exists_op()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==FOLParser.ID:
                    self.state = 25
                    self.match(FOLParser.ID)
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 31
                self.match(FOLParser.T__0)
                self.state = 32
                self.formula(4)
                pass

            elif la_ == 3:
                localctx = FOLParser.ForAllContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.forall_op()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==FOLParser.ID:
                    self.state = 35
                    self.match(FOLParser.ID)
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 41
                self.match(FOLParser.T__0)
                self.state = 42
                self.formula(3)
                pass

            elif la_ == 4:
                localctx = FOLParser.FormulaAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.atom()
                pass

            elif la_ == 5:
                localctx = FOLParser.FormulaParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(FOLParser.T__1)
                self.state = 46
                self.formula(0)
                self.state = 47
                self.match(FOLParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 67
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = FOLParser.AndContext(self, FOLParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 51
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 52
                        self.and_op()
                        self.state = 53
                        self.formula(9)
                        pass

                    elif la_ == 2:
                        localctx = FOLParser.OrContext(self, FOLParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 55
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 56
                        self.or_op()
                        self.state = 57
                        self.formula(8)
                        pass

                    elif la_ == 3:
                        localctx = FOLParser.ImplContext(self, FOLParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 59
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 60
                        self.impl_op()
                        self.state = 61
                        self.formula(6)
                        pass

                    elif la_ == 4:
                        localctx = FOLParser.IffContext(self, FOLParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 63
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 64
                        self.iff_op()
                        self.state = 65
                        self.formula(6)
                        pass

             
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.AtomContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRED(self):
            return self.getToken(FOLParser.PRED, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitProp(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.AtomContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.AtomContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class InRelContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.AtomContext)
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.TermContext)
            else:
                return self.getTypedRuleContext(FOLParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitInRel(self)
            else:
                return visitor.visitChildren(self)


    class UninRelContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.AtomContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRED(self):
            return self.getToken(FOLParser.PRED, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.TermContext)
            else:
                return self.getTypedRuleContext(FOLParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitUninRel(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = FOLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 91
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = FOLParser.InRelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.term(0)
                self.state = 73
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FOLParser.LT) | (1 << FOLParser.GT) | (1 << FOLParser.GE) | (1 << FOLParser.LE) | (1 << FOLParser.EQ) | (1 << FOLParser.NE))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 74
                self.term(0)
                pass

            elif la_ == 2:
                localctx = FOLParser.UninRelContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(FOLParser.PRED)
                self.state = 77
                self.match(FOLParser.T__1)
                self.state = 78
                self.term(0)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==FOLParser.T__0:
                    self.state = 79
                    self.match(FOLParser.T__0)
                    self.state = 80
                    self.term(0)
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.match(FOLParser.T__2)
                pass

            elif la_ == 3:
                localctx = FOLParser.PropContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(FOLParser.PRED)
                pass

            elif la_ == 4:
                localctx = FOLParser.TrueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                _la = self._input.LA(1)
                if not(_la==FOLParser.T__3 or _la==FOLParser.T__4):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                pass

            elif la_ == 5:
                localctx = FOLParser.FalseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                _la = self._input.LA(1)
                if not(_la==FOLParser.T__5 or _la==FOLParser.T__6):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermIntContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(FOLParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitTermInt(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.TermContext)
            else:
                return self.getTypedRuleContext(FOLParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.TermContext)
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.TermContext)
            else:
                return self.getTypedRuleContext(FOLParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class TermParensContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(FOLParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitTermParens(self)
            else:
                return visitor.visitChildren(self)


    class TermIdContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FOLParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitTermId(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FOLParser.TermContext)
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FOLParser.TermContext)
            else:
                return self.getTypedRuleContext(FOLParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FOLParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            token = self._input.LA(1)
            if token in [FOLParser.T__1]:
                localctx = FOLParser.TermParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 94
                self.match(FOLParser.T__1)
                self.state = 95
                self.term(0)
                self.state = 96
                self.match(FOLParser.T__2)

            elif token in [FOLParser.ID]:
                localctx = FOLParser.TermIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(FOLParser.ID)

            elif token in [FOLParser.INT]:
                localctx = FOLParser.TermIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(FOLParser.INT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 111
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = FOLParser.MulDivContext(self, FOLParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 102
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 103
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==FOLParser.MUL or _la==FOLParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 104
                        self.term(7)
                        pass

                    elif la_ == 2:
                        localctx = FOLParser.ModContext(self, FOLParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 105
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 106
                        self.match(FOLParser.MOD)
                        self.state = 107
                        self.term(6)
                        pass

                    elif la_ == 3:
                        localctx = FOLParser.AddSubContext(self, FOLParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 108
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 109
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==FOLParser.ADD or _la==FOLParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 110
                        self.term(5)
                        pass

             
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NegContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_neg

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)




    def neg(self):

        localctx = FOLParser.NegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_neg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FOLParser.T__7) | (1 << FOLParser.T__8) | (1 << FOLParser.T__9) | (1 << FOLParser.T__10))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exists_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_exists_op

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitExists_op(self)
            else:
                return visitor.visitChildren(self)




    def exists_op(self):

        localctx = FOLParser.Exists_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exists_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==FOLParser.T__11 or _la==FOLParser.T__12):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Forall_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_forall_op

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitForall_op(self)
            else:
                return visitor.visitChildren(self)




    def forall_op(self):

        localctx = FOLParser.Forall_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_forall_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not(_la==FOLParser.T__13 or _la==FOLParser.T__14):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Impl_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_impl_op

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitImpl_op(self)
            else:
                return visitor.visitChildren(self)




    def impl_op(self):

        localctx = FOLParser.Impl_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_impl_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not(_la==FOLParser.T__15 or _la==FOLParser.T__16):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Iff_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_iff_op

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitIff_op(self)
            else:
                return visitor.visitChildren(self)




    def iff_op(self):

        localctx = FOLParser.Iff_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_iff_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==FOLParser.T__17 or _la==FOLParser.T__18):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_and_op

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitAnd_op(self)
            else:
                return visitor.visitChildren(self)




    def and_op(self):

        localctx = FOLParser.And_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_and_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not(_la==FOLParser.T__19 or _la==FOLParser.T__20):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FOLParser.RULE_or_op

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, FOLVisitor ):
                return visitor.visitOr_op(self)
            else:
                return visitor.visitChildren(self)




    def or_op(self):

        localctx = FOLParser.Or_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_or_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not(_la==FOLParser.T__21 or _la==FOLParser.T__22):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         



