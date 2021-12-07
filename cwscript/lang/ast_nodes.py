from typing import List, Optional, Union
from dataclasses import dataclass

from lark import ast_utils, Transformer
from cwscript.lang.codegen import *


## AST Nodes
class _Ast(ast_utils.Ast):
    pass


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


@dataclass
class DeclError(_DeclStmt, ast_utils.AsList):
    defns: list


@dataclass
class EventDefn(_Ast, CGStructDefn):
    name: str
    members: Optional[List["TypeAssign"]]
    body: Optional[List[Union["_Stmt", "_Expr"]]]

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


# @dataclass
# class Struct(_Ast):
#     name: str
#     member_vals: str


class _QueryDefn(_Ast):
    pass


@dataclass
class DeclQuery(_DeclStmt, ast_utils.AsList):
    defns: List[_QueryDefn]


@dataclass
class QueryDefnFn(_QueryDefn):
    name: str
    args: str
    response_type: str
    body: str


@dataclass
class QueryDefnResponds(_QueryDefn):
    name: str
    args: str
    response_defn: str


class _TypeExpr(_Ast):
    pass


@dataclass
class TypeAssign(_Ast):
    name: str
    type: _TypeExpr

    def _gen_code(self, env) -> str:
        type_str = self.type.generate_code(env)
        return f"{self.name:s}: {type_str}"


@dataclass
class Typename(_TypeExpr):
    name: str

    def _gen_code(self, env) -> str:
        return self.name


@dataclass
class ParamzdTypeExpr(_TypeExpr):
    base_type: str
    param: str


@dataclass
class StructDictAssign(_Ast):
    name: str
    value: str


@dataclass
class InstantiateDefn(_Ast):
    args: str
    body: str


@dataclass
class DeclInstantiate(_DeclStmt):
    defn: InstantiateDefn


@dataclass
class TypeAssignAndSet(_Ast):
    type_assign: TypeAssign
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
class EnumVariantUnit(_Ast):
    name: str


@dataclass
class EnumVariantTuple(_Ast):
    name: str
    members: list


@dataclass
class DeclEnum(_DeclStmt):
    name: str
    variants: List[EnumVariant]


@dataclass
class EnumVariantDict(_Ast):
    name: str
    members: list


@dataclass
class DeclState(_DeclStmt, ast_utils.AsList):
    defns: list


@dataclass
class StructDictDefn(_DeclStmt):
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
