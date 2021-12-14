from cwscript.lang.ast import *
from cwscript.util.strings import *
from cwscript.util.context_env import *

class _Model:

    @classmethod
    def from_ast(cls, ast: _Ast):
        raise NotImplementedError(f"{cls.__name__}.from_ast() not implemented")
    
    def validate(self) -> List[Exception]:
        raise NotImplementedError(f"{self.__class__.__name__} not implemented")


class ModelEnv(Env):
    pass

class ContractModel(_Model):

    """Creates a logical representation of the contract which can be
    converted into code."""

    @classmethod
    def from_ast(cls, ast: ContractDefn, env: ModelEnv):
        # inherit from parents, from left to right
        error_defns = ast.collect_type(ErrorDefn)
        return cls()

    def validate(self) -> List[Exception]:
        pass

class InterfaceModel(_Model):
    pass

class ErrorModel(_Model):

    @classmethod
    def from_ast(cls, ast: ErrorDefn):
        return cls()