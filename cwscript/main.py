from cwscript import CWScriptCompiler
from cwscript.codegen import ContractCodegen

from cwscript.lang.ast import *
from cwscript.lang.parser import parse_cwscript_src
from cwscript.model import ContractModel

ast = parse_cwscript_src(open("examples/cw20-base/cw20base.cws", "r").read())
for contract in ast.collect_type(ContractDefn):
    contract_model = ContractModel.from_ast(contract)
    print(contract_model)
