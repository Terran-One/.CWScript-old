from typing import Callable, List, Optional, Union, Any
from dataclasses import dataclass

from lark import ast_utils, Transformer
from lark.lexer import Token

from cwscript.util.strings import pascal_to_snake, snake_to_pascal


def iis(test, *types: list) -> bool:
    """Returns `True` if `isinstance(test, t)` works for ANY `t` in `types`"""
    return any(isinstance(test, t) for t in types)


## AST Nodes
class _Ast(ast_utils.Ast):
    def collect(self, predicate: Callable[[Any], bool], *, dfs: bool = True) -> list:
        """Gets children for which the provided predicate returns True."""
        nodes = []
        for (key, child) in self.__dict__.items():
            if predicate(child):
                nodes.append(child)
            if dfs:
                if iis(child, _Ast):
                    nodes.extend(child.collect(predicate, dfs=True))
                elif iis(child, list, tuple):
                    for elem in child:
                        if predicate(elem):
                            nodes.append(elem)
                        if iis(elem, _Ast):
                            nodes.extend(elem.collect(predicate, dfs=True))
        if not dfs:
            for (key, child) in self.__dict__.items():
                if iis(child, _Ast):
                    nodes.extend(child.collect(predicate, dfs=False))
                elif iis(child, list, tuple):
                    for elem in child:
                        if predicate(elem):
                            nodes.append(elem)
                        if iis(elem, _Ast):
                            nodes.extend(elem.collect(predicate, dfs=False))
        return nodes

    def collect_type(self, *types, **kwargs):
        return self.collect(lambda x: iis(x, *types), **kwargs)

    def contains_type(self, *types, **kwargs):
        return len(self.collect(lambda x: iis(x, *types), **kwargs)) > 0

    def __contains__(self, _type) -> bool:
        """Alias for the 'in' operator."""
        if iis(_type, list, tuple):
            return self.contains_type(*_type)
        return self.contains_type(_type)

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


class _DeclStmt(_Ast):
    class Types:
        CONTRACT = "contract"
        ERROR = "error"
        EVENT = "event"
        STATE = "state"
        INSTANTIATE = "instantiate"
        EXEC = "exec"
        QUERY = "query"
        STRUCT = "struct"
        ENUM = "enum"


@dataclass
class ContractDefn(_Defn):
    name: str
    body: List[_ContractStmt]


@dataclass
class DeclContract(_DeclStmt):
    defn: ContractDefn

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
class DeclError(_DeclStmt, ast_utils.AsList):
    defns: List["ErrorDefn"]


@dataclass
class EventDefn(_Defn):
    defn: _EnumVariant

@dataclass
class DeclEvent(_DeclStmt, ast_utils.AsList):
    defns: list


@dataclass
class DeclExec(_DeclStmt, ast_utils.AsList):
    defns: list


class _StateDefn(_Defn):
    pass


@dataclass
class ItemDefn(_StateDefn):
    key: Ident
    type: "_TypeExpr"

@dataclass
class MapDefn(_StateDefn):
    prefix: str
    keys: str
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
class ElseIfClause(_Ast):
    predicate: str
    body: str


@dataclass
class IfElseIfElseExpr(_Ast):
    if_clause: str
    else_if_clauses: str
    else_clause: str


@dataclass
class DeclQuery(_DeclStmt, ast_utils.AsList):
    defns: List["_QueryDefn"]


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
        return f"(" + ",".join(m.typestr for m in self.members) + ")"

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
        return "Option<{self.wrapped.typestr}>"

@dataclass
class TypePath(_TypeExpr, ast_utils.AsList):
    parts: List[Ident]
   
    @property 
    def typestr(self) -> str:
        return "::".join(self.parts.join())

@dataclass
class SimplePath(_Ast, ast_utils.AsList):
    parts: List[Ident]
    
    def __str__(self) -> str:
        return "::".join(self.parts)
   
@dataclass
class TypeAssign(_Defn):
    name: str
    type: _TypeExpr


@dataclass
class Typename(_TypeExpr):
    name: str

    @property
    def typestr(self) -> str:
        return self.name


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
class DeclInstantiate(_DeclStmt):
    defn: "InstantiateDefn"


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
class MapKeyDefn(_Ast):
    key: str
    type: str


@dataclass
class EnumDefn(_Defn, _TypeExpr):
    name: str
    variants: List[_EnumVariant]

    @property
    def typestr(self) -> str:
        return self.name



@dataclass
class DeclState(_DeclStmt, ast_utils.AsList):
    defns: list

@dataclass
class StructDefn(_Defn, _TypeExpr):
    
    @property
    def typestr(self) -> str:
        return self.name
@dataclass
class StructCDefn(StructDefn):
    name: Ident
    members: List[TypeAssign]

@dataclass
class StructTupleDefn(StructDefn):
    name: Ident
    members: List[_TypeExpr]

@dataclass
class StructUnitDefn(StructDefn):
    name: Ident
@dataclass
class MapKey(_Ast):
    key: Ident
    type: _TypeExpr
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
   
    annotations = as_list
    annotation_items = as_list
    contract_stmts = as_list
    errors_group = as_list
    events_group = as_list 
    exec_group = as_list 
    state_group = as_list
    fn_body = as_list
    fn_call_args = as_list
    type_assign_and_sets = as_list
    type_assigns = as_list
    map_keys = as_list
    struct_val_assigns = as_list
    enum_variant_defns = as_list
   
    ## usually if the first elem is:
    ## RULE: "(" [plural] ")"
    fn_args = as_list
    tuple = as_list
    struct_members = as_list
    struct_members_with_assign = as_list
    
    ## values
    integer = alias_to(Integer)
    string = alias_to(String)
    infix_op = first
    assign_op = first
    ident_pascal = alias_to(Ident)
    ident_snake = alias_to(Ident)
    special_key = alias_to(Ident)