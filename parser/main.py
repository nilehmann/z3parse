#!/usr/bin/python
import sys
from antlr4 import *
from FOLLexer import FOLLexer
from FOLParser import FOLParser
from Z3Tree import Z3FromTree, z3visitor
from TreeFromParser import TreeFromParser
from z3 import *

def parse(str):
  input = InputStream(str)
  lexer = FOLLexer(input)
  stream = CommonTokenStream(lexer)
  parser = FOLParser(stream)
  return parser.formula()


def main(argv):
    # input = FileStream(argv[1])
    # visitor = FOLPrinter()
    if len(argv) < 2:
        print('Number of arguments invalid')
        return
    z3 = Z3FromTree().visit(TreeFromParser().visit(parse(argv[1])))
    solver = Solver()
    if len(argv) == 2:
        print(z3)
        qe = Tactic('qe')
        solver.add(z3)
        check = solver.check()
        print('check:', check)
        if check == sat:
            print('model', solver.model())
        # print('qe:', simplify(qe(simplify(z3)).as_expr()))
        print('qe:', z3visitor(simplify(qe(simplify(z3)).as_expr())))
    if len(argv) > 2:
        z32 = Z3FromTree().visit(TreeFromParser().visit(parse(argv[2])))
        print(z3)
        print(z32)
        solver.push()
        solver.add(Not(Implies(z3, z32)))
        b = True
        if solver.check() == unsat:
            print('-> OK')
        else:
            print('-> fails')
            print('model:', solver.model())
            b = False
        solver.pop()
        solver.add(Not(Implies(z32, z3)))
        if solver.check() == unsat:
            print('<- OK')
        else:
            print('<- fails')
            b = False
        if b:
            print('Equivalent')

if __name__ == '__main__':
    main(sys.argv)
