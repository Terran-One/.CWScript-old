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


class _QueryDefn(_Ast):
    pass


@dataclass
class QueryDefnFn(_Ast):
    name: str
    args: str
    response_type: str
    body: str


@dataclass
class QueryDefnResponds(_Ast):
    name: str
    args: str
    response_defn: str

@dataclass
class ResponseDefn(_Ast)

class _TypeExpr(_Ast):
    pass


@dataclass
class TypeAssign(_Ast):
    symbol: str
    type: _TypeExpr


@dataclass
class Typename(_Ast):
    name: str


@dataclass
class ParamzdTypeExpr(_TypeExpr):
    base_type: str
    param: str


## Transformer
class CWScriptToAST(Transformer):
    @v_args(inline=True)
    def contract_stmts(self, *stmts):
        return stmts

    def decl_fn_arg(self, x):
        return (x[0], x[1])

    def map_key_defn(self, x):
        return (x[0], x[1])

    def fn_call_args(self, x):
        return x

    def fn_args(self, x):
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
