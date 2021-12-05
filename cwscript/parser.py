import os
import sys

from lark import Lark, ast_utils, Transformer, v_args
from lark.tree import Meta

from cwscript._ast import *

this_module = sys.modules[__name__]
grammar_path = os.path.join(os.path.dirname(__file__), "grammar.lark")
grammar_file = open(grammar_path)
grammar = grammar_file.read()

def parse(text: str):
    cws_parser = Lark(grammar, start="start")
    tree = cws_parser.parse(text)
    transformer = ast_utils.create_transformer(this_module, CWScriptToAST())
    return transformer.transform(tree)
