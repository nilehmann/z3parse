from FOLVisitor import FOLVisitor
from FOLParser import FOLParser
import FOLTree as ft


class TreeFromParser(FOLVisitor):
    def visitNot(self, ctx):
        return ft.NotNode(self.visit(ctx.formula()))

    def visitExists(self, ctx):
        ids = [id.getText() for id in ctx.ID()]
        f = self.visit(ctx.formula())
        return ft.ExistsNode(ids, f)

    def visitForAll(self, ctx):
        ids = [id.getText() for id in ctx.ID()]
        f = self.visit(ctx.formula())
        return ft.ForAllNode(ids, f)

    def visitAnd(self, ctx):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return ft.AndNode(left, right)

    def visitOr(self, ctx):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return ft.OrNode(left, right)

    def visitImpl(self, ctx):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return ft.ImplNode(left, right)

    def visitIff(self, ctx):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return ft.IffNode(left, right)

    def visitInRel(self, ctx):
        left = self.visit(ctx.term(0))
        right = self.visit(ctx.term(1))
        ops = {
            FOLParser.GT: ft.GtNode,
            FOLParser.LT: ft.LtNode,
            FOLParser.GE: ft.GeNode,
            FOLParser.LE: ft.LeNode,
            FOLParser.EQ: ft.EqNode,
            FOLParser.NE: ft.NeNode,
        }
        if ctx.op.type not in ops:
            raise Exception('Not viable predicate')
        op = ops[ctx.op.type]
        return op(left, right)

    def visitUninRel(self, ctx):
        args = [self.visit(t) for t in ctx.term()]
        return ft.UninRelNode(ctx.PRED().getText(), args)

    def visitProp(self, ctx):
        return ft.PropNode(ctx.PRED().getText())

    def visitTrue(self, ctx):
        return ft.TrueNode()

    def visitFalse(self, ctx):
        return ft.FalseNode()

    def visitFormulaParens(self, ctx):
        return self.visit(ctx.formula())

    def visitTermParens(self, ctx):
        return self.visit(ctx.term())

    def visitAddSub(self, ctx):
        left = self.visit(ctx.term(0))
        right = self.visit(ctx.term(1))
        ops = {
            FOLParser.ADD: ft.AddNode,
            FOLParser.SUB: ft.SubNode,
        }
        if ctx.op.type not in ops:
            raise Exception('Not viable operator')
        op = ops[ctx.op.type]
        return op(left, right)

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.term(0))
        right = self.visit(ctx.term(1))
        ops = {
            FOLParser.MUL: ft.MulNode,
            FOLParser.DIV: ft.MulNode,
        }
        if ctx.op.type not in ops:
            raise Exception('Not viable operator')
        op = ops[ctx.op.type]
        return op(left, right)

    def visitMod(self, ctx):
        left = self.visit(ctx.term(0))
        right = self.visit(ctx.term(1))
        return ft.ModNode(left, right)

    def visitTermId(self, ctx):
        return ft.UninConstNode(ctx.ID().getText())

    def visitTermInt(self, ctx):
        return ft.IntNode(int(ctx.INT().getText()))
