import os
import sys

from black import FileMode, format_str
from lark import Lark, ast_utils

import cwscript.lang.ast
from cwscript.lang.ast import CWScriptToAST, _Ast

this_module = sys.modules[__name__]
grammar_path = os.path.join(os.path.dirname(__file__), "grammar.lark")
grammar_file = open(grammar_path)
grammar = grammar_file.read()
cws_parser = Lark(grammar, start="file_code")
transformer = ast_utils.create_transformer(cwscript.lang.ast, CWScriptToAST())


def parse_cwscript_src(text: str) -> _Ast:
    parse_tree = cws_parser.parse(text)
    ast = transformer.transform(parse_tree)
    with open("ast.py", "w") as astfile:
        astfile.write(format_str(str(ast), mode=FileMode()))
    return ast
