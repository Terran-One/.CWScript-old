from cwscript.util.context_env import Context, Env
from cwscript.template import codegen_templates as templates
from cwscript.lang.ast import _QueryDefn
from cwscript.lang.ast import *
from cwscript.util.strings import pascal_to_snake, snake_to_pascal 

class CGContext(Context):
    pass

class CGEnv(Env):
    pass

class ContractCodegen:
    
    def __init__(self, contract_defn: ContractDefn):
        self.defn = contract_defn
        self.errors = self.defn.collect_type(ErrorDefn)    
        self.events = self.defn.collect_type(EventDefn)
        self.instantiate = self.defn.collect_type(InstantiateDefn)
        self.exec = self.defn.collect_type(ExecDefn)
        self.query = self.defn.collect_type(QueryDefnFn)
        self.query.extend(x.to_query_defn_fn() for x in self.defn.collect_type(QueryDefnResponds))
        self.structs = self.defn.collect_type(StructDictDefn)
        self.enums = self.defn.collect_type(StructDictDefn)
    
    def gen_contract(self) -> str:
        return templates['contract'].render(contract=self)


class ICodegen:
    """Interface to allow for code generation.
    Note the pattern:

        1. `generate_code()` is the public interface and is already implemented
            for you. Modify `_gen_code()` to define what code to generate.
        2. `_gen_code()` and `_verify` are private, don't call them directly
            from within a foreign class. Use `generate_code()` which calls
            both `_verify()` and `_gen_code()`.
        3. You can subclass `ICodegen.VerifyError`.
    """

    class VerificationError(Exception):
        """Error during verification"""

    class GenerationError(Exception):
        """Error during code-generation"""

    def _gen_code(self, env: CGEnv) -> str:
        raise NotImplementedError(f"_gen_code() not implemented for {self.__class__}")

    def _verify(self, env: CGEnv):
        """Perform checks for validity, raise an Exception."""
        pass

    def generate_code(self, env: CGEnv) -> str:
        """Generate code for this node."""
        env.push(self)
        self._verify(env)
        code = self._gen_code(env)
        env.pop()
        assert code is not None
        return code


def render(template_name: str, **kwargs):
    template = templates[template_name]
    return template.render(**kwargs)

class CGStructDefn(ICodegen):
    """Subclass inside a StructDefn-like `_Ast` node to add codegen."""

    def _verify(self, env: CGEnv):
        if self.members is None:
            self.members = []
        if self.body is None:
            self.body = []

    def _gen_code(self, env: CGEnv) -> str:
        return render("struct_defn", struct=self, env=env)

def iis(test, *types) -> bool:
    """Returns `True` if `isinstance(test, t)` works for ANY `t` in `types`"""
    return any(isinstance(test, t) for t in types)
