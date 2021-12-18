grammar CWScript;

sourceFile: topLevelStmt*;

topLevelStmt:
	'contract' (name = IDENT) ('extends' parent = IDENT)? (
		'implements' interfaces = identList
	)? contractBody # ContractDefn;

contractBody: '{' innerExpr* '}';

innerExpr:
	errorDefn
	| eventDefn
	| instantiateDefn
	| execDefn
	| queryDefn;

errorDefn: 'error' enumVariant | 'errors' '{' enumVariant* '}';
eventDefn: 'event' enumVariant | 'events' '{' enumVariant* '}';
instantiateDefn: 'instantiate' fnArgs fnBody;
execDefn: 'exec' (name = IDENT) fnArgs fnBody;
queryDefn: 'query' (name = IDENT) fnArgs fnBody;

fnArgs: '(' (fnArg (',' fnArg)*)? ')';
fnArg: (arg_name = IDENT) (optional = '?')? ':' typeExpr;
fnBody: '{' IDENT* '}';

enumVariant:
	enumVariant_struct
	| enumVariant_tuple
	| enumVariant_unit;

enumVariant_struct:
	(name = IDENT) (parenStructMembers | curlyStructMembers);

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