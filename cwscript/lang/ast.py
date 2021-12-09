from typing import Callable, List, Optional, Union, Any
from dataclasses import dataclass, field

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
    
    def collect_with_depth(self, predicate, *, dfs: bool = True) -> dict:
        nodes = {}
        
        for (key, child) in self.__dict__.items():
            if predicate(child):
                nodes[key] = child
            if dfs:
                if iis(child, _Ast):
                    matches = child.collect_with_depth(predicate, dfs=False)
                    if len(matches) > 0:
                        nodes[key] = matches
                elif iis(child, list, tuple):
                    nodes[key] = {}
                    for (i, elem) in enumerate(child):
                        if predicate(elem):
                            nodes[key][str(i)] = elem
                        elif iis(elem, _Ast):
                            matches = elem.collect_with_depth(predicate, dfs=True)
                            if len(matches) > 0:
                                nodes[key][str(i)] = matches
        if not dfs:
            # process subnodes after all children
            for (key, child) in self.__dict__.items():
                if iis(child, _Ast):
                    matches = child.collect_with_depth(predicate, dfs=False)
                    if len(matches) > 0:
                        nodes[key] = matches
                elif iis(child, list, tuple):
                    nodes[key] = {}
                    for (i, elem) in enumerate(child):
                        if predicate(elem):
                            nodes[key][str(i)]= elem
                        elif iis(elem, _Ast):
                            matches = elem.collect_with_depth(predicate, dfs=False)
                            if len(matches) > 0:
                                nodes[key][str(i)] = matches
        return nodes

    def collect_type(self, *types, **kwargs):
        return self.collect(lambda x: iis(x, *types), **kwargs)
    
    def contains_type(self, *types, **kwargs):
        return len(self.collect(lambda x: iis(x, *types), **kwargs)) > 0
    
    def __contains__(self, _type) -> bool:
        """Alias for the 'in' operator."""
        return self.contains_type(_type)
            

class _Stmt(_Ast):
    pass


class _Expr(_Ast):
    pass


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
class ContractDefn(_Ast):
    name: str
    body: List[_ContractStmt]

@dataclass
class DeclContract(_DeclStmt):
    defn: ContractDefn


@dataclass
class ErrorDefn(_Ast):
    name: str
    members: Optional[List["TypeAssign"]]
    body: Optional[List[Union["_Stmt", "_Expr"]]]
    
    def __post_init__(self):
        if self.members is None:
            self.members = []
        if self.body is None:
            self.body = []
    
    def to_struct_defn(self) -> "StructDictDefn":
        return StructDictDefn(self.name, self.members)


@dataclass
class DeclError(_DeclStmt, ast_utils.AsList):
    defns: List["ErrorDefn"]


@dataclass
class EventDefn(_Ast):
    name: str
    members: Optional[List["TypeAssign"]]
    body: Optional[List[Union["_Stmt", "_Expr"]]]
    
    def __post_init__(self):
        if self.members is None:
            self.members = []
        if self.body is None:
            self.body = []
    
    def to_struct_defn(self) -> "StructDictDefn":
        return StructDictDefn(self.name, self.members)

@dataclass
class DeclEvent(_DeclStmt, ast_utils.AsList):
    defns: list


@dataclass
class DeclExec(_DeclStmt, ast_utils.AsList):
    defns: list


class _StateDefn(_Ast):
    pass


@dataclass
class ItemDefn(_StateDefn):
    key: str
    type_expr: str


@dataclass
class MapDefn(_StateDefn):
    prefix: str
    type_keys: list
    type_value: str


@dataclass
class ExecDefn(_Ast):
    name: str
    args: list
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
    
class _QueryDefn(_Ast):
    pass

@dataclass
class QueryDefnFn(_QueryDefn):
    name: str
    args: Optional[List["TypeAssign"]]
    response_type: "_TypeExpr"
    body: Optional[List[Union[_Stmt, _Expr]]]
    
    def to_enum_variant(self) -> "EnumVariant":
        if self.args is None:
            return EnumVariantUnit(self.name.to_pascal(), self.args)
        else:
            return EnumVariantDict(snake_to_pascal(self.name), self.args)

@dataclass
class QueryDefnResponds(_QueryDefn):
    name: "Ident"
    args: str
    response_defn: "QueryResponseDefn"
    
    def to_query_defn_fn(self) -> QueryDefnFn:
        struct_name = f"{self.name.to_pascal()}Response" 
        struct_members = [tas.type_assign for tas in self.response_defn.body]
        return QueryDefnFn(name = self.name, args = self.args, response_type = StructDictDefn(struct_name, struct_members), body=None)

@dataclass
class QueryResponseDefn(_Ast):
    body: List["TypeAssignAndSet"]

class _TypeExpr(_Ast): 
    @property
    def typestr(self) -> str:
        raise NotImplementedError(f"property {self.__class__}.typestr not implemented")

class ToTypeExpr:
    """Denotes that a node can be represented also as a type expression."""
    
    def to_type_expr(self):
        raise NotImplementedError(f"{self.__class__}.to_type_expr() not implemented")

@dataclass
class TypeAssign(_Ast):
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
class InstantiateDefn(_Ast):
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


class EnumVariant(_Ast):
    pass


@dataclass
class EnumVariantUnit(EnumVariant):
    name: str


@dataclass
class EnumVariantTuple(EnumVariant):
    name: str
    members: list

@dataclass
class EnumDefn(_TypeExpr):
    name: str
    variants: List[EnumVariant]
   
    @property 
    def typestr(self) -> str:
        return self.name 

@dataclass
class EnumVariantDict(EnumVariant):
    name: str
    members: List[TypeAssign]

@dataclass
class DeclState(_DeclStmt, ast_utils.AsList):
    defns: list

class _StructDefn(_TypeExpr):
    @property
    def typestr(self) -> str:
        return self.name

@dataclass
class StructDictDefn(_StructDefn):
    name: str
    members: List[TypeAssign]
    
@dataclass
class StructDictVal(_Ast):
    name: str
    members_vals: List[StructDictAssign]


@dataclass
class IdentPath(_Ast, ast_utils.AsList):
    parts: List[str]


@dataclass
class EmitStmt(_Stmt):
    expr: _Expr


@dataclass
class FailStmt(_Stmt):
    expr: _Expr


class _Value(_Expr):
    pass


@dataclass
class String(_Value):
    value: str


@dataclass
class Integer(_Value):
    value: int
    
@dataclass
class Ident(_Ast):
    symbol: Token 

    def to_pascal(self) -> "Ident":
        return Ident(snake_to_pascal(str(self.symbol)))

    def to_snake(self) -> "Ident":
        return Ident(pascal_to_snake(str(self.symbol)))
    
    def __str__(self) -> str:
        return str(self.symbol)

## Transformer
class CWScriptToAST(Transformer):
    def contract_stmts(self, stmts):
        return stmts

    def struct_dict_assigns(self, x):
        return x

    def struct_tuple_assigns(self, x):
        return x

    def decl_enum_variants(self, x):
        return x

    def decl_map_keys(self, x):
        return x

    def type_assigns(self, x):
        return x
    
    def type_assign_and_sets(self, x):
        return x
    
    def fn_args(self, x):
        if x[0] is None:
            return []
        return x[0]

    def fn_call_args(self, x):
        return x

    def fn_body(self, x):
        return x

    def integer(self, x):
        return Integer(x[0])

    def string(self, x):
        return String(x[0])

    def infix_op(self, x):
        return x[0]

    def assign_op(self, x):
        return str(x[0])
   
    def ident_pascal(self, x):
        return Ident(x[0])
   
    def ident_snake(self, x):
        return Ident(x[0]) 