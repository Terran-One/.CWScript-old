import os
from typing import Any

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

from cwscript.util.context_env import Context, Env

parent_dir = os.path.dirname(__file__)
templates_dir = os.path.join(parent_dir, "templates")
j_env = Environment(loader=FileSystemLoader(templates_dir))
templates = {}
for t in j_env.list_templates():
    name = t[: t.find(".")]
    templates[name] = j_env.get_template(t)


class CGContext(Context):
    pass


class CGEnv(Env):
    pass


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


def render_template(template_name: str, **kwargs):
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
        return render_template("struct_defn.rs.jinja", ref=self, env=env)


def iis(test, *types) -> bool:
    """Returns `True` if `isinstance(test, t)` works for ANY `t` in `types`"""
    return any(isinstance(test, t) for t in types)
