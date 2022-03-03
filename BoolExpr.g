
grammar BoolExpr;

boolExpr: andExpr;

andExpr: left=orExpr (AND right=boolExpr)?;

orExpr: left=xorExpr (OR right=boolExpr)?;

xorExpr: left=unaryExpr (XOR right=boolExpr)?;

unaryExpr: at=atom | (neg=negatedUnary);

negatedUnary: NOT at=atom;

atom: var=variable | (LPAR and_expr=andExpr RPAR);

variable: name=VARIABLE;

VARIABLE: [a-zA-Z][0-9a-zA-Z_]*;

LPAR: '(';

RPAR: ')';

NOT: '~';

XOR: '^';

AND: '&';

OR: '|';

WS: [ \r\n\t]+ -> skip;
