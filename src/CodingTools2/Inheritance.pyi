
from abc import ABC
from typing import KeysView, ItemsView, Iterable, ValuesView


class InheritanceSkeleton(ABC): ...


class DataClass(InheritanceSkeleton):
    __value_types: set
    __protect_values: set[str]

    @property
    def value_types(self) -> set: ...

    def __init__(self, **kwargs): ...
    def add_value_type(self, _type: type) -> 'DataClass': ...

    def __values(self) -> dict: ...
    def __repr__(self) -> str: ...
    def keys(self) -> KeysView: ...
    def values(self) -> ValuesView: ...
    def items(self) -> ItemsView: ...
    def __getitem__(self, key: str) -> any: ...
    def __getitems__(
            self,
            keys: tuple[str] | list[str] | set[str]
    ) -> any: ...
    def __setitem__(self, key: str, value: any) -> None: ...
    def __setitems__(
            self,
            keys: tuple[str] | list[str] | set[str],
            values: tuple[any] | list[any] | set[any],
    ) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __delitems__(
            self,
            keys: tuple[str] | list[str] | set[str]
    ) -> None: ...
    def __iter__(self) -> Iterable: ...

    def __unsupported_operand(self, operator: str, other) -> str: ...
    def __add__(self, other: 'DataClass' | dict) -> 'DataClass': ...
    def __iadd__(self, other: 'DataClass' | dict) -> 'DataClass': ...
    def __sub__(
            self, other: 'DataClass' | dict | tuple | list | set
    ) -> 'DataClass': ...
    def __isub__(
        self, other: 'DataClass' | dict | tuple | list | set
        ) -> 'DataClass': ...
    def __eq__(self, other: 'DataClass' | dict) -> bool: ...
    def __ne__(self, other: 'DataClass' | dict) -> bool: ...
    def __lt__(self, other: 'DataClass' | dict) -> bool: ...
    def __gt__(self, other: 'DataClass' | dict) -> bool: ...
    def __contains__(self, key: str) -> bool: ...

    ...
