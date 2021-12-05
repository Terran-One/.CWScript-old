import os
from ast_nodes import *
from lark import Lark, Transformer

grammar_path = os.path.join(os.path.dirname(__file__), "grammar.lark")
grammar_file = open(grammar_path)
grammar = grammar_file.read()


class CWScriptTransformer(Transformer):
    def contract_block(self, args):
        return Contract(args[0], args[1:])

    def error_def_grouped(self, args):
        # print(args)
        pass

    def state_def_grouped(self, args):
        # print(args)
        pass

    def arg_def(self, args):
        return {"ident": args[0], "type": args[1]}

    def fn_args(self, args):
        return FnArgs(args)

    def instantiate_def(self, args):
        fn_args = args[0]
        fn_body = args[1]
        a = InstantiateDef(fn_args, fn_body)
        print(a)
        return a


def parse(text: str):
    cws_parser = Lark(grammar, start="start")
    tree = cws_parser.parse(text)
    return CWScriptTransformer().transform(tree)
