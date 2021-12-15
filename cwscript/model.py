from dataclasses import dataclass, field

from cwscript.lang.ast import *
from cwscript.lang.ast import _Ast
from cwscript.util.strings import *
from cwscript.util.context_env import *

from rust import *

class _Model:
    parent = None

    def set_parent(self, parent):
        self.parent = parent
        return self

    @classmethod
    def from_ast(cls, ast: _Ast):
        raise NotImplementedError(f"{cls.__name__}.from_ast() not implemented")
    
    def validate(self) -> List[Exception]:
        raise NotImplementedError(f"{self.__class__.__name__} not implemented")


class ModelEnv(Env):
    pass

class ContractErrors(_Model):

    def __init__(self, ast: List[ErrorDefn], env=None):
        if env is None:
            env = ModelEnv()
        self.env = env

class ContractModel(_Model):

    """Creates a logical representation of the contract which can be
    converted into code."""

    def __init__(self, ast: ContractDefn, env=None):
        exec_fn = ast.collect_type(ExecDefn)
        pass

    def validate(self) -> List[Exception]:
        pass

class InterfaceModel(_Model):
    pass

@dataclass
class RustEnum:

    name: str
    variants: list = field(default_factory=list)

@dataclass
class RustStruct:
    name: str
    

@dataclass
class ErrorModel(_Model):
    
    name: str = None
    variant: str = None
    members: list = None

    @classmethod
    def from_ast(cls, ast: ErrorDefn):
        res = cls()
        name = str(ast.defn.name)
        variant = EnumVariantStruct
        members = None
        if iis(cls, EnumVariantStruct):
            members = []
        elif iis(cls, EnumVariantTuple):
            pass
        return cls(name, variant, members)

