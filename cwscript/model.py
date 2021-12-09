from typing import List
from pathlib import Path
from dataclasses import dataclass

from cwscript.lang.ast import _DeclStmt, _StateDefn, _QueryDefn
from cwscript.lang.ast import *
from cwscript.util.strings import *
from cwscript.template import contract_crate_templates as templates, render_to_file

class Visibility:
    PRIVATE = 0
    PUBLIC = 1
    
class BaseModel:
    pass
    
class TypeExprModel(BaseModel):
    pass

@dataclass
class TypeAssignModel(BaseModel):
    name: str
    type: str

class TypeAssignAndSetModel(BaseModel):
    name: str
    type: TypeExprModel
    value: str

class StmtModel(BaseModel):
    pass
    
@dataclass
class StructDefnModel(TypeExprModel):
    class Variant:
        DICT = 2
        TUPLE = 1
        UNIT = 0
    
    @dataclass    
    class MemberModel:
        name: str
        type: str

    name: str
    variant: Variant
    members: List[MemberModel]

@dataclass
class EnumDefnModel(TypeExprModel):
    name: str
    variants: List[StructDefnModel]

    
@dataclass
class ErrorDefnModel(StructDefnModel):
    body: List[StmtModel]
    
    def to_struct_defn(self) -> StructDefnModel:
        pass

@dataclass
class EventDefnModel(StructDefnModel):
    
    def to_struct_defn(self) -> StructDefnModel:
        pass
    
class StateDefnModel(BaseModel):
    pass

@dataclass
class ItemDefnModel(StateDefnModel):
    key: str
    type: TypeExprModel
     
@dataclass
class MapKeyDefnModel(BaseModel):
    key: str
    type: TypeExprModel

@dataclass
class MapDefnModel(StateDefnModel):
    prefix: str
    keys: MapKeyDefnModel
    type: TypeExprModel


@dataclass
class MsgDefnModel(BaseModel):
    
    name: str
    args: List[TypeAssignModel]
    ret_type: TypeExprModel
    body: List[StmtModel]
   
    # msg definition
    def to_struct_defn(self) -> StructDefnModel:
        pass
   
    # msg handler
    def to_fn(self):
        pass


@dataclass
class InstantiateDefnModel(MsgDefnModel):
    pass
@dataclass
class ExecDefnModel(MsgDefnModel):
    pass
    
@dataclass
class QueryDefnModel(MsgDefnModel):
    pass

class ContractModel:

    """Creates a logical representation of the contract which can be
    converted into code."""

    name: str
    defns: list

    @property
    def errors(self) -> List[ErrorDefn]:
        return self.defns_of(ErrorDefnModel)

    @property
    def events(self) -> List[EventDefnModel]:
        return self.defns_of(EventDefnModel)
    
    @property
    def instantiate(self):
        return self.defns_of(InstantiateDefnModel)
    
    @property
    def exec(self):
        return self.defns_of(ExecDefnModel)
    
    @property
    def query(self):
        return self.defns_of(QueryDefnModel)
    
    @classmethod
    def from_ast(cls, contract_defn: ContractDefn):
        return cls(contract_defn.name, contract_defn.body)

    def __repr__(self) -> str:
        res = f"""Contract ({self.name})
        errors: {len(self.errors)} 
        events: {len(self.events)}
        state types: {len(self.state)}
        exec fns: {len(self.exec)}
        query fns: {len(self.query)}
        """
        return res