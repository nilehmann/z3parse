from FOLTree import FOLTreeVisitor
import FOLTree as ft
import z3
import z3consts as z3c


def Iff(left, right):
    return z3.And(z3.Implies(left, right), z3.Implies(right, left))


class Z3FromTree(FOLTreeVisitor):
    def visitNot(self, node):
        return z3.Not(self.visit(node.formula()))

    def visitExists(self, node):
        ids = [z3.Int(id) for id in node.ids()]
        f = self.visit(node.formula())
        return z3.Exists(ids, f)

    def visitForAll(self, node):
        ids = [z3.Int(id) for id in node.ids()]
        f = self.visit(node.formula())
        return z3.ForAll(ids, f)

    def visitAnd(self, node):
        left = self.visit(node.formula(0))
        right = self.visit(node.formula(1))
        return z3.And(left, right)

    def visitOr(self, node):
        left = self.visit(node.formula(0))
        right = self.visit(node.formula(1))
        return z3.Or(left, right)

    def visitImpl(self, node):
        left = self.visit(node.formula(0))
        right = self.visit(node.formula(1))
        return z3.Implies(left, right)

    def visitIff(self, node):
        left = self.visit(node.formula(0))
        right = self.visit(node.formula(1))
        return Iff(left, right)

    # Atom

    def visitProp(self, node):
        return z3.Bool(node.name())

    def visitTrue(self, node):
        return z3.simplify(z3.And(True, True))

    def visitFalse(self, node):
        return z3.simplify(z3.And(False, False))

    def visitUninRel(self, node):
        args = [self.visit(term) for term in node.term()]
        sort = [z3.IntSort()]*len(node.term())+[z3.BoolSort()]
        P = z3.Function(node.name(), sort)
        return P(args)

    def visitGe(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left >= right

    def visitGt(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left > right

    def visitLe(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left <= right

    def visitLt(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left < right

    def visitEq(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left == right

    def visitNe(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left != right

    # Term

    def visitMul(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left * right

    def visitDiv(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left / right

    def visitMod(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left % right

    def visitAdd(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left + right

    def visitSub(self, node):
        left = self.visit(node.term(0))
        right = self.visit(node.term(1))
        return left - right

    def visitUninConst(self, node):
        return z3.Int(node.name())

    def visitInt(self, node):
        return node.n()


z3_op_to_tree_cnstr = {
    z3c.Z3_OP_NOT: ft.NotNode,
    z3c.Z3_OP_IMPLIES: ft.ImplNode,
    z3c.Z3_OP_AND: ft.AndNode,
    z3c.Z3_OP_OR: ft.OrNode,

    z3c.Z3_OP_TRUE: ft.TrueNode,
    z3c.Z3_OP_FALSE: ft.FalseNode,
    z3c.Z3_OP_EQ: ft.EqNode,
    z3c.Z3_OP_LE: ft.LeNode,
    z3c.Z3_OP_LT: ft.LtNode,
    z3c.Z3_OP_GE: ft.GeNode,
    z3c.Z3_OP_GT: ft.GtNode,
    z3c.Z3_OP_DISTINCT: ft.NeNode,

    z3c.Z3_OP_DIV: ft.DivNode,
    z3c.Z3_OP_MOD: ft.ModNode,
    z3c.Z3_OP_ADD: ft.AddNode,
    z3c.Z3_OP_SUB: ft.SubNode,
    z3c.Z3_OP_MUL: ft.MulNode,
    }


def treeFromQuantifier(obj, xs):
    ys = [str(obj.var_name(i)) for i in range(obj.num_vars())]
    new_xs = xs + ys
    body = treeFromZ3(obj.body(), new_xs)
    quantifier = ft.ForAllNode if obj.is_forall() else ft.ExistsNode
    return quantifier(ys, body)


def treeFromApp(obj, xs):
    k = obj.decl().kind()
    op = z3_op_to_tree_cnstr.get(k, None)
    if op is None:
        op = obj.decl().name()
    return str(op) + str([treeFromZ3(c, xs) for c in obj.children()])


def treeFromVar(obj, xs):
    idx = z3.get_var_index(obj)
    return xs[idx]


def treeFromZ3(obj, xs=[]):
    if z3.is_quantifier(obj):
        return treeFromQuantifier(obj, xs)
    elif z3.is_app(obj):
        return treeFromApp(obj, xs)
    elif z3.is_var(obj):
        return treeFromVar(obj, xs)
    else:
        raise Exception("Unrecognized expression")
