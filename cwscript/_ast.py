from typing import List
from dataclasses import dataclass

from lark import Lark, ast_utils, Transformer, v_args
from lark.tree import Meta

class _Ast(ast_utils.Ast):
    pass

class _Stmt(_Ast):
    pass

@dataclass
class ContractBlock(_Ast, ast_utils.AsList):
    statements: List[_Stmt]
