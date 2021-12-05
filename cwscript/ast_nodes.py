from dataclasses import dataclass


@dataclass
class Contract:
    name: str
    body: str


@dataclass
class FnArgs:
    arglist: str


@dataclass
class InstantiateDef:
    fn_args: FnArgs
    fn_body: str
