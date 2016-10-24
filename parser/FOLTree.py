class FOLNode:
    def __init__(self, children=[]):
        self._children = children

    def children(self, i=None):
        if i is None:
            return self._children
        else:
            assert(i < len(self._children))
            return self._children[i]


class NotNode(FOLNode):
    def __init__(self, formulas):
        if not isinstance(formulas, list):
            formulas = [formulas]
        super().__init__(formulas)

    def formula(self):
        return self.children(0)

    def accept(self, visitor):
        return visitor.visitNot(self)

    def __str__(self):
        return '¬ %s' % str(self.children(0))


class IffNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def formula(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitIff(self)

    def __str__(self):
        return '{} <-> {}'.format(*self.children)

class ImplNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def formula(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitImpl(self)

    def __str__(self):
        return '{} -> {}'.format(*self.children())

class OrNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def formula(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitOr(self)

    def __str__(self):
        return '{} or {}'.format(*self.children())

class AndNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def formula(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitAnd(self)

    def __str__(self):
        return '{} and {}'.format(*self.children())

class ExistsNode(FOLNode):
    def __init__(self, ids, formula):
        super().__init__([formula])
        self._ids = ids

    def formula(self):
        return self.children(0)

    def ids(self):
        return self._ids

    def accept(self, visitor):
        return visitor.visitExists(self)

    def __str__(self):
        return 'exists {}, {}'.format(' '.join(self.ids()), *self.children())

class ForAllNode(FOLNode):
    def __init__(self, ids, formula):
        super().__init__([formula])
        self._ids = ids

    def formula(self):
        return self.children(0)

    def ids(self):
        return self._ids

    def accept(self, visitor):
        return visitor.visitForAll(self)

    def __str__(self):
        return 'forall {}, {}'.format(' '.join(self.ids()), *self.children())
# Atom


class FalseNode(FOLNode):
    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitFalse(self)

    def __str__(self):
        return 'False'

class TrueNode(FOLNode):
    def __init__(self, *args):
        pass

    def accept(self, visitor):
        return visitor.visitTrue(self)

    def __str__(self):
        return 'True'

class PropNode(FOLNode):
    def __init__(self, name, *args):
        self._name = name

    def name(self):
        return self._name

    def accept(self, visitor):
        return visitor.visitProp(self)

    def __str__(self):
        return self._name


class LeNode(FOLNode):
    def __init__(self, left, right):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i=None):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitLe(self)

    def __str__(self):
        return '%s <= %s' % (str(self.children(0)), str(self.children(1)))


class GeNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i=None):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitGe(self)

    def __str__(self):
        return '%s >= %s' % (str(self.children(0)), str(self.children(1)))

class GtNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i=None):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitGt(self)

    def __str__(self):
        return '%s > %s' % (str(self.children(0)), str(self.children(1)))

class LtNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i=None):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitLt(self)

    def __str__(self):
        return '%s < %s' % (str(self.children(0)), str(self.children(1)))

class EqNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i=None):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitEq(self)


class NeNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i=None):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitNe(self)


class UninRelNode(FOLNode):
    def __init__(self, name, args):
        super().__init__(args)
        self._name = name

    def name(self):
        return self._name

    def term(self, i=None):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitUninRel(self)

    def __str__(self):
        return '%s(%s)' % (self._name, ','.join([str(c) for c in self.children()]))

# Term


class UninConstNode(FOLNode):
    def __init__(self, name, *args):
        self._name = name

    def name(self):
        return self._name

    def accept(self, visitor):
        return visitor.visitUninConst(self)

    def __str__(self):
        return self._name


class IntNode(FOLNode):
    def __init__(self, n):
        self._n = n

    def n(self):
        return self._n

    def accept(self, visitor):
        return visitor.visitInt(self)

    def __str__(self):
        return str(self._n)


class FunNode(FOLNode):
    def __init__(self, name, args):
        super().__init__(args)
        self._name = name

    def name(self):
        return self._name

    def term(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitFun(self)


class AddNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitAdd(self)


class SubNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitSub(self)


class ModNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitMod(self)


class MulNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitMul(self)


class DivNode(FOLNode):
    def __init__(self, left, right=None):
        if right is None:
            children = left
        else:
            children = [left, right]
        super().__init__(children)

    def term(self, i):
        return self.children(i)

    def accept(self, visitor):
        return visitor.visitDiv(self)


class FOLTreeVisitor:
    def visit(self, node):
        return node.accept(self)

    def visitNot(self, node):
        raise NotImplementedError('Operation not implemented: visitNot')

    def visitIff(self, node):
        raise NotImplementedError('Operation not implemented: visitIff')

    def visitImpl(self, node):
        raise NotImplementedError('Operation not implemented: visitImpl')

    def visitOr(self, node):
        raise NotImplementedError('Operation not implemented: visitOr')

    def visitAnd(self, node):
        raise NotImplementedError('Operation not implemented: visitAnd')

    def visitExists(self, node):
        raise NotImplementedError('Operation not implemented: visitExists')

    def visitForAll(self, node):
        raise NotImplementedError('Operation not implemented: visitForAll')

    # Atom

    def visitFalse(self, node):
        raise NotImplementedError('Operation not implemented: visitFalse')

    def visitTrue(self, node):
        raise NotImplementedError('Operation not implemented: visitTrue')

    def visitProp(self, node):
        raise NotImplementedError('Operation not implemented: visitProp')

    def visitLe(self, node):
        raise NotImplementedError('Operation not implemented: visitLe')

    def visitGe(self, node):
        raise NotImplementedError('Operation not implemented: visitGe')

    def vistGt(self, node):
        raise NotImplementedError('Operation not implemented: visitGt')

    def visitLt(self, node):
        raise NotImplementedError('Operation not implemented: visitLt')

    def visitEq(self, node):
        raise NotImplementedError('Operation not implemented: visitEq')

    def visitNe(self, node):
        raise NotImplementedError('Operation not implemented: visitNe')

    def visitUninRel(self, node):
        raise NotImplementedError('Operation not implemented: visitUninRel')

    # Term

    def visitInt(self, node):
        raise NotImplementedError('Operation not implemented: visitInt')

    def visitFun(self, node):
        raise NotImplementedError('Operation not implemented: visitFun')

    def visitAdd(self, node):
        raise NotImplementedError('Operation not implemented: visitAdd')

    def visitSub(self, node):
        raise NotImplementedError('Operation not implemented: visitSub')

    def visitMod(self, node):
        raise NotImplementedError('Operation not implemented: visitMod')

    def visitMul(self, node):
        raise NotImplementedError('Operation not implemented: visitMul')

    def visitDiv(self, node):
        raise NotImplementedError('Operation not implemented: visitDiv')

    def visitUninConst(self, node):
        raise NotImplementedError('Operation not implemented: visitUninConst')
