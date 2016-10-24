grammar FOL;

formula : neg formula                   # not
        | formula and_op formula        # and
        | formula or_op formula         # or
        | <assoc=right> formula impl_op formula # impl
        | formula iff_op formula        # iff
        | exists_op ID* ',' formula     # exists
        | forall_op ID* ',' formula     # forAll
        | atom                          # formulaAtom
        | '(' formula ')'               # formulaParens
        ;

atom : term op=('<'|'<='|'>'|'>='|'='|'!=') term # inRel
     | PRED'('term (',' term)*')' # uninRel
     | PRED          # prop
     | ('true'|'True')   # true
     | ('false'|'False') # false
     ;

term : term op=('*'|'/') term   # MulDiv
     | term '%' term            # mod
     | term op=('+'|'-') term   # AddSub
     | '(' term ')'             # termParens
     | ID                       # termId
     | INT                      # termInt
     ;

neg       : 'not' | 'neg' | '~' | '¬' ;
exists_op : '∃' | 'exists' ;
forall_op : '∀' | 'forall' ;
impl_op   : '→' | '->'  ;
iff_op    : '↔' | '<->' ;
and_op    : '∧' | 'and' ;
or_op     : '∨' | 'or' ;

LT        : '<' ;
GT        : '>' ;
GE        : '>=' ;
LE        : '<=' ;
EQ        : '=' ;
NE        : '!=' ;

ADD       : '+' ;
SUB       : '-' ;
MUL       : '*' ;
DIV       : '/' ;
MOD       : '%' ;

ID        : [a-z][A-Za-z_]* ;
PRED      : [A-Z][A-za-z_]* ;
INT       : '-'?[0-9]+ ;
WD        : [ \t\r\n]+ -> skip ;
