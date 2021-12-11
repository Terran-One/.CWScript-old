from cwscript import CWScriptCompiler
from cwscript.codegen import ContractCodegen

from cwscript.lang.ast import *
from cwscript.lang.parser import parse_cwscript_src

ast = parse_cwscript_src(open("examples/cw20-base/cw20base.cws", "r").read())
for cd in ast.collect_type(ContractDefn):
    codegen = ContractCodegen(cd)
    print(codegen.gen_contract())
