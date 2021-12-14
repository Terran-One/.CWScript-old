import os
from os import PathLike
from typing import List
from pathlib import Path

from cwscript.lang.parser import parse_cwscript_src
from cwscript.lang.ast import ContractDefn
from cwscript.model import ContractModel
from cwscript.util.strings import *
from cwscript.template import contract_crate_templates as templates, render_to_file


class CWScriptCompiler:

    base_dir: Path
    src_files: List[Path]

    def __init__(self, project_name="untitled", base_dir=None, src_files=[]):
        self.project_name = project_name
        self.base_dir = base_dir
        self.src_files = src_files

    def _getpath(self, path):
        if self.base_dir is None:
            this_dir = Path(os.path.dirname(__name__))
            return this_dir / path
        return self.base_dir / path

    def add_src_file(self, src_file_path: PathLike):
        with open(self._getpath(src_file_path), "r"):
            self.src_files.append(src_file_path)


    def generate_crate(
        self,
        contract_model: ContractModel,
        target_dir: PathLike,
        crate_name: str = None,
    ):
        if crate_name is None:
            crate_name = camel_to_snake(contract_model.name)
        out_dir = self._getpath(target_dir)

        # create output dir
        os.makedirs(out_dir, exist_ok=True)
        os.makedirs(out_dir / "src", exist_ok=True)
        os.makedirs(out_dir / ".cargo", exist_ok=True)

        # create Cargo.toml
        render_to_file(
            templates["Cargo.toml"], out_dir / "Cargo.toml", crate_name=crate_name
        )
        # .gitignore
        render_to_file(templates[".gitignore"], out_dir / ".gitignore")
        # rustfmt.toml
        render_to_file(templates["rustfmt.toml"], out_dir / "rustfmt.toml")
        # .cargo/config
        render_to_file(templates[".cargo/config"], out_dir / ".cargo/config")
