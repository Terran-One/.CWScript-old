from typing import Callable, Iterator, List, Optional, Union, Any
from itertools import *
from dataclasses import dataclass

from lark import ast_utils, Transformer
from lark.lexer import Token

from cwscript.util.strings import pascal_to_snake, snake_to_pascal


def iis(test, *types: list) -> bool:
    """Returns `True` if `isinstance(test, t)` works for ANY `t` in `types`"""
    return any(isinstance(test, t) for t in types)

def _collect(item, predicate: Callable[[Any], bool], *, dfs: bool = True):
    nodes = []
    if dfs:
        # depth-first
        if predicate(item):
            nodes.append(item)
        if iis(item, _Ast):
            for child in item.__dict__.values():
                nodes.extend(_collect(child, predicate))
        elif iis(item, list, tuple):
            for elem in item:
                nodes.extend(_collect(elem, predicate))
        else:
            return nodes
    else:
        # breadth-first
        if predicate(item):
            nodes.append(item)
        if _Ast.is_ast(item):
            for child in item.__dict__.values():
                if predicate(child):
                    nodes.append(child)
        elif iis(item, list, tuple):
            for elem in item:
                if predicate(elem):
                    nodes.append(elem)
        else:
            return nodes
        nodes.extend(_collect(elem, predicate, dfs=False))
    return nodes
    
## AST Nodes
class _Ast(ast_utils.Ast):
    def collect(self, predicate: Callable[[Any], bool], *, dfs: bool = True) -> list:
        """Gets children for which the provided predicate returns True."""
        return _collect(self, predicate)

    def collect_type(self, *types, **kwargs):
        return self.collect(lambda x: iis(x, *types), **kwargs)

    def contains_type(self, *types, **kwargs):
        return len(self.collect_type(*types, **kwargs)) > 0

    def __contains__(self, _type) -> bool:
        """Alias for the 'in' operator."""
        if iis(_type, list, tuple):
            return self.contains_type(*_type)
        return self.contains_type(_type)

    @property
    def children(self) -> dict:
        return self.__members__
    
    @property
    def children_as_list(self) -> list:
        return list(self.__members__.values())
    
    def is_ast(self) -> bool:
        return iis(self, _Ast)

@dataclass
class Ident(_Ast):
    symbol: Token

    def to_pascal(self) -> "Ident":
        return Ident(snake_to_pascal(str(self.symbol)))

    def to_snake(self) -> "Ident":
        return Ident(pascal_to_snake(str(self.symbol)))

    def __str__(self) -> str:
        return str(self.symbol)


class _Stmt(_Ast):
    pass

class _Expr(_Ast):
    pass

@dataclass
class Annotation(_Ast):
    items: list

@dataclass
class _Defn(_Ast):
    annotations: Optional[List[Annotation]]

@dataclass
class FileCode(_Ast, ast_utils.AsList):
    body: list


class _ContractStmt(_Ast):
    pass


@dataclass
class ContractDefn(_Defn):
    name: str
    parents: List[Ident]
    interfaces: List[Ident]
    body: List[_ContractStmt]

@dataclass
class InterfaceDefn(_Defn):
    name: str
    body: List[_ContractStmt]

@dataclass
class EnumVariantDefn(_Defn):
    variant: "_EnumVariant"

@dataclass
class _EnumVariant(_Ast):
    pass

@dataclass
class EnumVariantStruct(_EnumVariant):
    name: "Ident"
    members: list

@dataclass
class EnumVariantTuple(_EnumVariant):
    name: "Ident"
    members: list

@dataclass
class EnumVariantUnit(_EnumVariant):
    name: "Ident"
@dataclass
class ErrorDefn(_Defn):
    defn: _EnumVariant

@dataclass
class EventDefn(_Defn):
    defn: _EnumVariant

class _StateDefn(_Defn):
    pass


@dataclass
class MapKey(_Ast):
    key: Ident
    type: "_TypeExpr"


@dataclass
class ItemDefn(_StateDefn):
    key: Ident
    type: "_TypeExpr"

@dataclass
class MapDefn(_StateDefn):
    prefix: Ident
    keys: MapKey
    value: str
    
FnArgs = List["TypeAssign"]

@dataclass
class ExecDefn(_Defn):
    name: Ident
    args: FnArgs
    body: str

@dataclass
class InfixOpExpr(_Ast):
    lhs: str
    op: str
    rhs: str

@dataclass
class PrefixOpExpr(_Ast):
    op: str
    arg: str

@dataclass
class MemberAccessExpr(_Ast):
    item: str
    member: str


@dataclass
class TableLookupExpr(_Ast):
    item: str
    key: str


@dataclass
class FnCallExpr(_Ast):
    fn_name: str
    args: list


@dataclass
class IfExpr(_Ast):
    if_clause: str
    else_if_clauses: str
    else_body: str


@dataclass
class IfClause(_Ast):
    predicate: str
    body: str

@dataclass
class IfSome(_Ast):
    predicate: str
    body: str

@dataclass
class OptionIdent(_Ast):
    ident: Ident

@dataclass
class ElseIfClause(_Ast):
    predicate: str
    body: str


@dataclass
class IfElseIfElseExpr(_Ast):
    if_clause: str
    else_if_clauses: str
    else_clause: str



@dataclass
class _QueryDefn(_Defn):
    pass


@dataclass
class QueryDefnFn(_QueryDefn):
    name: Ident
    args: FnArgs
    response_type: "_TypeExpr"
    body: Optional[List[Union[_Stmt, _Expr]]]

@dataclass
class QueryDefnResponds(_QueryDefn):
    name: Ident
    args: FnArgs
    response_defn: "QueryResponseDefn"

    def to_query_defn_fn(self) -> QueryDefnFn:
        struct_name = f"{self.name.to_pascal()}Response"
        struct_members = [tas.type_assign for tas in self.response_defn]
        return QueryDefnFn(
            annotations=self.annotations,
            name=self.name,
            args=self.args,
            response_type=StructCDefn(None, struct_name, struct_members),
            body=None,
        )


@dataclass
class QueryResponseDefn(_Ast):
    body: List["TypeAssignAndSet"]


class _TypeExpr(_Ast):
    @property
    def typestr(self) -> str:
        raise NotImplementedError(f"property {self.__class__}.typestr not implemented")
    
@dataclass
class TupleType(_TypeExpr, ast_utils.AsList):
    members: List[_TypeExpr]

    @property
    def typestr(self) -> str:
        return f"({', '.join(m.typestr for m in self.members)})"

@dataclass
class VectorType(_TypeExpr):
    item: _TypeExpr
    
    @property
    def typestr(self) -> str:
        return f"Vec<{self.item.typestr}>"

@dataclass
class RefType(_TypeExpr):
    wrapped: _TypeExpr
    
    @property
    def typestr(self) -> str:
        return f"&{self.wrapped.typestr}"

@dataclass
class Option(_TypeExpr):
    wrapped: _TypeExpr
   
    @property 
    def typestr(self) -> str:
        return f"Option<{self.wrapped.typestr}>"

@dataclass
class TypePath(_TypeExpr, ast_utils.AsList):
    parts: List[_TypeExpr]
   
    @property 
    def typestr(self) -> str:
        return "::".join(x.typestr for x in self.parts)

@dataclass
class SimplePath(_Ast, ast_utils.AsList):
    parts: List[Ident]
    
    def __str__(self) -> str:
        return "::".join(str(x) for x in self.parts)

@dataclass
class ReflectiveTypePath(_Ast):
    type_path: TypePath
       
    def __str__(self) -> str:
        return "::".join(str(x) for x in self.parts)
@dataclass
class TypeAssign(_Defn):
    name: Ident 
    type: _TypeExpr
    checks: list


@dataclass
class Typename(_TypeExpr):
    name: Ident 

    @property
    def typestr(self) -> str:
        return str(self.name)


@dataclass
class ParamzdTypeExpr(_TypeExpr):
    base_type: _TypeExpr
    param: _TypeExpr

    def __str__(self) -> str:
        return f"{self.base_type.typestr}<{self.param.typestr}>"


@dataclass
class StructDictAssign(_Ast):
    name: str
    value: str


@dataclass
class InstantiateDefn(_Defn):
    args: list
    body: list


@dataclass
class TypeAssignAndSet(_Ast):
    type_assign: "TypeAssign"
    value: str


@dataclass
class AssignStmt(_Stmt):
    lhs: str
    assign_op: str
    rhs: str

@dataclass
class ForStmt(_Stmt):
    for_elems: str
    iterable: str
    body: str

@dataclass
class CheckLambda(_Ast):
    name: Ident
    type_bound: _TypeExpr
    predicate: _Expr
    error_type: _TypeExpr

@dataclass
class CheckFn(_Ast):
    name: Ident
    type_bound: _TypeExpr
    body: list

@dataclass
class ForDestructure(_Ast, ast_utils.AsList):
    idents: Ident 

@dataclass
class StructCallExpr(_Expr):
    fn: MemberAccessExpr
    args: list

@dataclass
class StructArg(_Ast):
    name: str 
    value: str 


@dataclass
class EnumDefn(_Defn, _TypeExpr):
    name: Ident
    variants: List[_EnumVariant]

    @property
    def typestr(self) -> str:
        return str(self.name)


@dataclass
class StructDefn(_Defn, _TypeExpr):
    name: Ident
    
    @property
    def typestr(self) -> str:
        return str(self.name)
@dataclass
class StructCDefn(StructDefn):
    members: List[TypeAssign]

@dataclass
class Check(_Ast):
    name: Ident
    args: List[str]

@dataclass
class StructTupleDefn(StructDefn):
    members: List[_TypeExpr]

@dataclass
class StructUnitDefn(StructDefn):
    pass
@dataclass
class EmitStmt(_Stmt):
    expr: _Expr


@dataclass
class FailStmt(_Stmt):
    expr: _Expr


class _Value(_Expr):
    pass

@dataclass
class StructVal(_Value):
    name: Ident
    members: list

@dataclass
class StructValAssign(_Ast):
    name: Ident
    value: _Expr

@dataclass
class String(_Value):
    value: str

@dataclass
class AndExpr(_Expr):
    a: _Expr
    b: _Expr

@dataclass
class OrExpr(_Expr):
    a: _Expr
    b: _Expr

@dataclass
class IdentAssignExpr(_Expr):
    ident: Ident
    val: _Expr
@dataclass
class Integer(_Value):
    value: int


as_list = lambda _, x: x
first = lambda _, x: x[0]
alias_to = lambda t: lambda _, x: t(*x)

## Transformer
class CWScriptToAST(Transformer):

    error_defn2 = alias_to(ErrorDefn)
    event_defn2 = alias_to(EventDefn)
    
    ## state
    item_defn2 = alias_to(ItemDefn) 
    map_defn2 = alias_to(MapDefn)
    exec_defn2 = alias_to(ExecDefn)
    
    query_defn_fn2 = alias_to(QueryDefnFn)
    query_defn_responds2 = alias_to(QueryDefnResponds)
    
    decl_contract = as_list 
    decl_error = as_list
    decl_event = as_list
    decl_state = as_list
    decl_instantiate = as_list
    decl_exec = as_list
    decl_query = as_list
    decl_type = as_list
    
    extends = as_list
    implements = as_list
   
    annotations = as_list
    annotation_items = as_list
    contract_stmts = as_list
    errors_group = as_list
    events_group = as_list 
    exec_group = as_list 
    query_group = as_list
    state_group = as_list
    fn_body = as_list
    fn_call_args = as_list
    type_assign_and_sets = as_list
    type_assigns = as_list
    map_keys = as_list
    struct_val_assigns = as_list
    enum_variant_defns = as_list
    checks = as_list
    contract_body = first
    struct_call_args = as_list
   
    ## usually if the first elem is:
    ## RULE: "(" [plural] ")"
    fn_args = as_list
    tuple_members = as_list
    struct_members = as_list
    struct_members_with_assign = as_list
    
    ## values
    integer = alias_to(Integer)
    string = alias_to(String)
    infix_op = first
    prefix_op = first
    assign_op = first
    ident_pascal = alias_to(Ident)
    ident_snake = alias_to(Ident)
    special_key = alias_to(Ident)