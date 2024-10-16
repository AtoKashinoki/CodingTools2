
from abc import ABC


class InheritanceSkeleton(ABC): ...


class DataClass(InheritanceSkeleton):
    __value_types: set[type]
    @property
    def value_types(self) -> set[type]: ...
    def __init__(self, **kwargs): ...
    def __values(self) -> dict: ...
    def keys(self): ...
    def __getitem__(self, key: str) -> any: ...
    def __setitem__(self, key: str, value:) -> None: ...
    def __repr__(self) -> str: ...
