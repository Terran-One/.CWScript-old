class Context:
    """`Context` is generic class that holds a node and a symbol table."""

    def __init__(self, node=None, symbols={}):
        self.node = node
        self.symbols = symbols


class Env:
    """The `Env` object holds a base object and manages the Context stack
    around it. You should pass `Env` instance around and not manage contexts.
    """

    def __init__(self, base=None, ctx_stack=[]):
        self.base = None
        self.ctx_stack = []

    def push(
        self,
        x,
    ):
        self.ctx_stack.append(x)

    def pop(self):
        return self.ctx_stack.pop()

    @property
    def top(self):
        return self.ctx_stack[-1]

    def lookup(self, symbol):
        for ctx in reversed(self.ctx_stack):
            if symbol in ctx.symbols:
                return ctx.symbols[symbol]
        raise KeyError(f"not found: {symbol}")

    @property
    def parent(self):
        try:
            return self.ctx_stack[-2]
        except IndexError:
            return None


class CodegenEnv(Env):
    """A subclass of env suited for code generation"""
