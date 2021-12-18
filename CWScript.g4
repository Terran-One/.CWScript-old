grammar CWScript;

sourceFile: topLevelStmt*;

topLevelStmt:
	'contract' (name = IDENT) ('extends' parent = IDENT)? (
		'implements' interfaces = identList
	)? contractBody # ContractDefn;

contractBody: '{' innerExpr* '}';

innerExpr: errorDefn;

errorDefn: 'error' enumVariant;
enumVariant:
	enumVariant_struct
	| enumVariant_tuple
	| enumVariant_unit;

enumVariant_struct: (name = IDENT) parenStructMembers
	| curlyStructMembers;
enumVariant_tuple: (name = IDENT) tupleMembers;
enumVariant_unit: (name = IDENT);

tupleMembers: '(' typeExpr (',' typeExpr)* ')';
parenStructMembers: '(' (structMember (',' structMember)*)? ')';
curlyStructMembers:
	'{' (structMember (',' structMember)* ','?)? '}';
structMember: (IDENT ':' typeExpr);

typeExpr: (symbol = IDENT) # TypeName;

identList: IDENT (',' IDENT)*;
IDENT: [$a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\n]+ -> skip;