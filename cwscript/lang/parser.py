import os
import sys

from lark import Lark, ast_utils
from black import FileMode, format_str

import cwscript.lang.ast_nodes
from cwscript.lang.ast_nodes import _Ast, CWScriptToAST


this_module = sys.modules[__name__]
grammar_path = os.path.join(os.path.dirname(__file__), "grammar.lark")
grammar_file = open(grammar_path)
grammar = grammar_file.read()
cws_parser = Lark(grammar, start="file_code")
transformer = ast_utils.create_transformer(cwscript.lang.ast_nodes, CWScriptToAST())


def parse_cwscript_src(text: str) -> _Ast:
    parse_tree = cws_parser.parse(text)
    ast = transformer.transform(parse_tree)
    with open("ast.py", "w") as astfile:
        astfile.write(format_str(str(ast), mode=FileMode()))
    return ast
