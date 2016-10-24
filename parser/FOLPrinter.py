from FOLVisitor import FOLVisitor
from FOLParser import *


class FOLPrinter(FOLVisitor):

    def visitExists(self, ctx):
        id = ctx.ID().getText()
        f = self.visit(ctx.formula())
        return 'exists '+id+", "+f

    def visitForall(self, ctx):
        id = ctx.ID().getText()
        f = self.visit(ctx.formula())
        return 'forall '+id+", "+f

    def visitAnd(self, ctx):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return left+ '/\\'+ right

    def visitOr(self, ctx):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        return left+ '\\/'+ right

    def visitImplIff(self, ctx):
        left = self.visit(ctx.formula(0))
        right = self.visit(ctx.formula(1))
        op = '->' if ctx.impl_op() else '<->'
        print(left,op,right)
        return left + op + right

    def visitFormulaAtom(self, ctx):
        return self.visit(ctx.atom())

    def visitParens(self, ctx):
        return '(' + self.visit(ctx.formula()) + ')'

    def visitAtom(self, ctx):
        left = self.visit(ctx.term(0));
        right = self.visit(ctx.term(1));
        ops = {
            FOLParser.GT: '>',
            FOLParser.LT: '<',
            FOLParser.GE: '>=',
            FOLParser.LE: '<=',
            FOLParser.EQ: '=',
        }
        op = ops[ctx.op.type]
        return left + ' ' + op + ' ' + right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.term(0))
        right = self.visit(ctx.term(1))
        ops = {
            FOLParser.ADD: '+',
            FOLParser.SUB: '-',
        }
        op = ops[ctx.op.type]
        return left + op + right

    def visitTermId(self, ctx):
        return ctx.ID().getText()

    def visitTermInt(self, ctx):
        return ctx.INT().getText()
