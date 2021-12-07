from typing import List, Union
from dataclasses import dataclass
from collections import namedtuple

from lark import ast_utils, Transformer, v_args
from lark.tree import Meta

## AST Nodes
class _Ast(ast_utils.Ast):
    pass


class _Stmt(_Ast):
    pass


class _Expr(_Ast):
    pass


@dataclass
class FileCode(_Ast, ast_utils.AsList):
    statements: list


class _ContractStmt(_Ast):
    pass


class DeclTypes:
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
    statements: List[_ContractStmt]


@dataclass
class DeclContract(_Ast):
    defn: ContractDefn


@dataclass
class ErrorDefn(_Ast):
    name: str
    args: list = None
    body: str = None


@dataclass
class DeclError(_Ast, ast_utils.AsList):
    children: list


@dataclass
class EventDefn(_Ast):
    name: str
    args: str = None
    body: str = None


@dataclass
class DeclEvent(_Ast, ast_utils.AsList):
    children: list


@dataclass
class DeclExec(_Ast, ast_utils.AsList):
    exec_defns: str


@dataclass
class EventDefn(_Ast):
    name: str
    args: str
    body: str = None


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
    else_if_clause: str
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
    symbol: str
    type: _TypeExpr


@dataclass
class Typename(_TypeExpr):
    name: str


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


class _Value(_Expr):
    pass


## Transformer
class CWScriptToAST(Transformer):
    @v_args(inline=True)
    def contract_stmts(self, *stmts):
        return stmts

    def decl_map_keys(self, x):
        return x

    def type_assigns(self, x):
        return x
    
    def fn_call_args(self, x):
        return x

    def fn_body(self, x):
        return x

    def integer(self, x):
        return int(x[0])

    def string(self, x):
        return str(x[0])

    def infix_op(self, x):
        return x[0]

    def assign_op(self, x):
        return str(x[0])
