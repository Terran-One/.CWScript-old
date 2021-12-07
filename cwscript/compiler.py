import os
from os import PathLike, mkdir
from typing import List

from cwscript.lang.parser import parse_cwscript_src
from cwscript.lang.model import build_contract_model, ContractModel
from cwscript.lang.ast_nodes import FileCode, DeclContract, ContractDefn


class CWScriptCompiler:

    base_dir: PathLike
    src_files: List[PathLike]

    def __init__(self, project_name="untitled", base_dir=None, src_files=[]):
        self.project_name = project_name
        self.base_dir = base_dir
        self.src_files = src_files

    def _getpath(self, path):
        if self.base_dir is None:
            parent_dir = os.path.dirname(__name__)
            return os.path.join(parent_dir, path)
        return os.path.join(self.base_dir, path)

    def add_src_file(self, src_file_path: PathLike):
        with open(self._getpath(src_file_path), "r"):
            self.src_files.append(src_file_path)

    def compile(self, target_dir: PathLike):
        file_codes = []
        for s in self.src_files:
            with open(s, "r") as src_file:
                ast = parse_cwscript_src(src_file.read())
                file_codes.append(ast)
        
        contract_models = []
        for fc in file_codes:
            for stmt in fc.body:
                if isinstance(stmt, DeclContract):
                    contract_models.append(build_contract_model(stmt.defn))
        
        if len(contract_models) > 1:
            self.write_project(contract_models, target_dir)
        else:
            self.write_contract(contract_models[0], target_dir)

    def write_contract(self, contract_model: ContractModel, target_dir: PathLike):
        output_dir = self._getpath(target_dir)
        Generate