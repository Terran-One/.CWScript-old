from dataclasses import dataclass
import os
from typing import Any

from cwscript.util.context_env import Context, Env
from cwscript.template import codegen_templates as templates
class CGContext(Context):
    pass


class CGEnv(Env):
    pass

@dataclass
class CGContractModel:
    
    # msg.rs
    instantiate_msg = []
    execute_msgs = []
    query_msgs = []
    query_responses = []
   
    # state.rs
    items = []
    maps = []
    
    # errors.rs
    errors = []
    
    # events.rs
    events = [] 
    
    # contract.rs
    instantiate_fn = []
    execute_fns = []
    query_fns = []
    


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
