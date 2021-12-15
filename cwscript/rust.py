from typing import List, Union
from dataclasses import dataclass

@dataclass
class RustType:
    pass

@dataclass
class VariantStruct:
    name: str
    members: list

@dataclass
class VariantTuple:
    name: str
    members: list

@dataclass
class VariantUnit:
    name: str 


@dataclass
class RustEnum:

    name: str
    variants: List[Union["VariantStruct", "VariantTuple", "VariantUnit"]]
