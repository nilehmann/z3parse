# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by FOLParser.

class FOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FOLParser#not.
    def visitNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#iff.
    def visitIff(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#impl.
    def visitImpl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#or.
    def visitOr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#forAll.
    def visitForAll(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#formulaParens.
    def visitFormulaParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#exists.
    def visitExists(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#formulaAtom.
    def visitFormulaAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#and.
    def visitAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#inRel.
    def visitInRel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#uninRel.
    def visitUninRel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#prop.
    def visitProp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#true.
    def visitTrue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#false.
    def visitFalse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#termInt.
    def visitTermInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#AddSub.
    def visitAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#mod.
    def visitMod(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#termParens.
    def visitTermParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#MulDiv.
    def visitMulDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#termId.
    def visitTermId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#neg.
    def visitNeg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#exists_op.
    def visitExists_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#forall_op.
    def visitForall_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#impl_op.
    def visitImpl_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#iff_op.
    def visitIff_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#and_op.
    def visitAnd_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FOLParser#or_op.
    def visitOr_op(self, ctx):
        return self.visitChildren(ctx)


