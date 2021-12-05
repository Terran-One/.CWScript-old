from typing import List, Union
from dataclasses import dataclass

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


@dataclass
class ContractDefnCode(_Ast, ast_utils.AsList):
    children: List[_ContractStmt]


@dataclass
class ContractDefn(_Ast):
    name: str
    body: ContractDefnCode


@dataclass
class ErrorDefn(_Ast):
    name: str
    args: str = None
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
class FnArgs(_Ast, ast_utils.AsList):
    children: list


@dataclass
class DeclFnArg(_Ast):
    name: str
    type_expr: str


class _StateDefn(_Ast):
    pass


@dataclass
class ItemDefn(_StateDefn):
    key: str
    type_expr: str


@dataclass
class TypeExpr(_Ast):
    body: str


@dataclass
class MapDefn(_StateDefn):
    base_key: str
    keys: list
    value: TypeExpr


@dataclass
class FnBody(_Ast, ast_utils.AsList):
    children: List[Union[_Stmt, _Expr]]


@dataclass
class ExecDefn(_Ast):
    name: str
    args: FnArgs
    body: FnBody


## Transformer
class CWScriptToAST(Transformer):
    @v_args(inline=True)
    def start(self, x):
        return x
