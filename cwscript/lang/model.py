from cwscript.lang.ast_nodes import *


class ContractModel:

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

    @classmethod
    def parse(cls, contract_defn: "ContractDefn") -> "ContractModel":
        contract = cls()
        contract.name = contract_defn.name
        for stmt in contract_defn.body:
            if isinstance(stmt, _DeclStmt):
                if isinstance(stmt, DeclInstantiate):
                    contract.add_defn(stmt.defn)
                else:
                    for defn in stmt.defns:
                        contract.add_defn(defn)
        return contract

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

    def __repr__(self) -> str:
        res = f"""Contract ({self.name})
        errors: {len(self.errors)} 
        events: {len(self.events)}
        state types: {len(self.state)}
        exec fns: {len(self.exec)}
        query fns: {len(self.query)}
        """
        return res


def build_contract_model(contract_defn: ContractDefn) -> ContractModel:
    model = ContractModel(contract_defn.name)
    for stmt in contract_defn.body:
        if isinstance(stmt, _DeclStmt):
            if isinstance(stmt, DeclInstantiate):
                model.add_defn(stmt.defn)
            else:
                for defn in stmt.defns:
                    model.add_defn(defn)
    return model
