"""Implementation of a rudimentary type system with Hilden-Milner type inference."""

from kanren import *
from dataclasses import dataclass

t0 = var("t0")
t1 = var("t1")
t2 = var("t2")
t3 = var("t3")
t4 = var("t4")
t5 = var("t5")
t6 = var("t6")
t7 = var("t7")

types = {
    "foo": t0,
    "f": t1,
    "g": t2,
    "x": t3,
    "if f(x == 1) then g(x) else 20": t4,
    "f(x == 1)": t5,
    "x == 1": t6,
    "g(x)": t7,
    "20": "Int",
}


@unifiable
@dataclass
class IfExpr:
    predicate: str
    a: str
    b: str

    def __repr__(self):
        return f"{{ {self.a!r},{self.b!r} }}"

    def __call__(self):
        return lall(eq(a, b))


@unifiable
@dataclass
class Func:
    args: list
    result: str

    def __repr__(self):
        return (
            "(" + ",".join(repr(arg) for arg in self.args) + ") -> " + repr(self.result)
        )


predicate = var("predicate")
a = var("a")
b = var("b")

func = Relation()
if_expr = Relation()
fact(
    if_expr,
)


x = run(
    0,
    t0,
    eq(t6, "Bool"),  # == operator -> Bool
    eq(t1, Func([t5], t6)),  # f: fn defn
    eq(t3, "Int"),  # infer t3 as Int
    eq(t2, Func([t3], t7)),  # g: fn defn
    eq(t0, Func([t1, t2, t3], t4)),  # fn defn
    eq(t4, IfExpr(t5, t7, "Int")),  # define
    eq(IfExpr(predicate, a, b), IfExpr("Bool", a, b)),
    # eq(IfExpr(predicate, a, b), IfExpr("Bool", a, a)),
    # eq(IfExpr(predicate, a, b), IfExpr("Bool", b, b)),
)
print(x)
