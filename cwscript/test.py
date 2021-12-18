from antlr4 import *
from cwscript.antlr.CWScriptLexer import CWScriptLexer
from cwscript.antlr.CWScriptListener import CWScriptListener
from cwscript.antlr.CWScriptParser import CWScriptParser

class PrintContractListener(CWScriptListener):
    def enterContractDefn(self, ctx: CWScriptParser.ContractDefnContext):
        print(ctx.name, ctx.parent)
        return super().enterContractDefn(ctx)

def main():
    lexer = CWScriptLexer(FileStream("examples/antlr.cws"))
    stream = CommonTokenStream(lexer)
    parser = CWScriptParser(stream)
    tree = parser.sourceFile()
    printer = PrintContractListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()