from pathlib import Path

from cwscript.lang.ast_nodes import _DeclStmt, _StateDefn, _QueryDefn
from cwscript.lang.ast_nodes import *
from cwscript.util.strings import camel_to_snake
from cwscript.template import contract_crate_templates as templates, render_to_file

class ContractModel:

    """Creates a logical representation of the contract which can be
    converted into code."""

    name: str
    errors: list
    events: list
    state: list
    instantiate: list
    exec: list
    query: list
    
    def __init__(self, name: str):
        self.name = name
        self.errors = []
        self.events = []
        self.state = []
        self.instantiate = []
        self.exec = []
        self.query = []
        self.query_responses = []

    def add_defn(self, defn) -> "ContractModel":
        if isinstance(defn, ErrorDefn):
            self.errors.append(defn)
        elif isinstance(defn, EventDefn):
            self.events.append(defn)
        elif isinstance(defn, _StateDefn):
            self.state.append(defn)
        elif isinstance(defn, InstantiateDefn):
            self.instantiate.append(defn)
        elif isinstance(defn, ExecDefn):
            self.exec.append(defn)
        elif isinstance(defn, _QueryDefn):
            self.query.append(defn)
        else:
            raise TypeError(f"definition not supported: {defn}")
        return self
    
    def compute_cg_model(self):
        """Create the codegen model."""

    def derive_inline_types(self):
        """Called after all definitions have been added. Types used inline
        should be added where appropriate."""

    def __repr__(self) -> str:
        res = f"""Contract ({self.name})
        errors: {len(self.errors)} 
        events: {len(self.events)}
        state types: {len(self.state)}
        exec fns: {len(self.exec)}
        query fns: {len(self.query)}
        """
        return res

    def write_as_crate(self, to: Path, crate_name: str = None):
        if crate_name is None:
            crate_name = camel_to_snake(self.name)
        
        # create output dir
        os.makedirs(to, exist_ok=True)
        os.makedirs(to / "src", exist_ok=True)
        os.makedirs(to / ".cargo", exist_ok=True)
        
        env = {
            "crate_name": crate_name,
            "model": self
        }
        
        for (name, templ) in templates.items():
            render_to_file(templ, to / name, **env)
        
        # # create Cargo.toml
        # render_to_file(templates["Cargo.toml"], to / "Cargo.toml", crate_name=crate_name)
        # # .gitignore
        # render_to_file(templates[".gitignore"], to / ".gitignore")
        # # rustfmt.toml
        # render_to_file(templates["rustfmt.toml"], to / "rustfmt.toml")
        # # .cargo/config
        # render_to_file(templates[".cargo/config"], to / ".cargo/config")
        
        # # write source files
        # render_to_file(templates["src/lib.rs"], to / "src/lib.rs", model=self) 
        # # write source files
        # render_to_file(templates["src/contract.rs"], to / "Cargo.toml", model=self) 


def build_contract_model(contract_defn: ContractDefn) -> ContractModel:
    model = ContractModel(contract_defn.name)
    for stmt in contract_defn.body:
        if isinstance(stmt, _DeclStmt):
            if isinstance(stmt, DeclInstantiate):
                model.add_defn(stmt.defn)
            else:
                for defn in stmt.defns:
                    model.add_defn(defn)
    model.derive_inline_types()
    return model
