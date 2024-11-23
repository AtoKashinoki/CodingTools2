"""
    CodingTools2.Inheritance

This file contain classes for developing programs.
"""


""" Prevent execute this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from abc import ABC, abstractmethod
from copy import deepcopy
from typing import KeysView, ValuesView, ItemsView, Iterable
from .Errors import Message


""" Skeleton """


class InheritanceSkeleton(ABC):
    """ Inheritance class base """
    ...


""" Inheritance classes """


class DataClass(InheritanceSkeleton):
    """ DataClass base """

    """ values """
    __value_types: set = {str, int, float, bool, tuple, list, dict, set}
    __protect_values: set[str] = {
        "__module__",
        "__main__",
        "__annotations__",
        "__slotnames__",
    }

    """ properties """
    @property
    def value_types(self) -> set: return self.__value_types

    """ processes """

    """ Initialize """
    def __init__(self, **kwargs):
        """ Initialize values """
        if not len(kwargs) == 0:
            self.__setitems__(*zip(*kwargs.items()))
            ...
        self.__value_types = DataClass.__value_types
        self.__protect_values = DataClass.__protect_values
        return

    def add_value_type(self, _type: type) -> 'DataClass':
        self.__value_types.add(_type)
        return self

    """ dictionary methods"""
    def __values(self) -> dict:
        """ Return validated attributes """
        return {
            key: value
            for __ins_cls__ in (self.__class__, self)
            for key, value in __ins_cls__.__dict__.items()
            if isinstance(value, tuple(self.__value_types))
            if 0 ==  sum([
                key[1:len(name)+1] ==  name
                for name in (self.__class__.__name__, DataClass.__name__)
            ])
            if key not in self.__protect_values
        }

    def __repr__(self) -> str:
        return "{}{}".format(
            self.__class__.__name__,
            self.__values(),
        )

    def keys(self) -> KeysView:
        """ Return attributes keys """
        return self.__values().keys()

    def values(self) -> ValuesView:
        """ Return attributes values """
        return self.__values().values()

    def items(self) -> ItemsView:
        """ Return attributes items """
        return self.__values().items()

    def __getitem__(self, key: str) -> any:
        """ Get data from data class """
        return self.__values()[key]

    def __getitems__(
            self,
            keys: tuple[any] | list[any] | set[any]
    ) -> any:
        """ Get datas from data class """
        values = self.__values()
        return tuple(
            values[key]
            for key in keys
        )

    def __setitem__(self, key: str, value: any) -> None:
        """ Set data in  data class """
        setattr(self, key, value)
        return

    def __setitems__(
            self,
            keys: tuple[str] | list[str] | set[str],
            values: tuple[any] | list[any] | set[any]
    ) -> None:
        """ Set datas in data class """
        [
            setattr(self, key, value)
            for key, value in zip(keys, values)
        ]
        return

    def __delitem__(self, key: str) -> None:
        """ Delete data from data class """
        delattr(self, key)
        return

    def  __delitems__(self, keys: tuple[str] | list[str] | set[str]) -> None:
        """ Delete datas from data class """
        [
            delattr(self, key)
            for key in keys
            if key in self.__dict__
        ]
        return

    def __len__(self) -> int:
        return len(self.__values())

    def __iter__(self) -> Iterable:
        return iter(self.keys())

    """ operators """

    def __unsupported_operand(self, operator: str, other) -> str:
        """ Return unsupported operand type """
        return Message.unsupported_operand(
                operator,
                self.__class__.__name__,
                other.__class__.__name__,
            )

    def __add__(self, other: 'DataClass' or dict) -> 'DataClass':
        if not (isinstance(other, DataClass) or isinstance(other, dict)):
            raise TypeError(self.__unsupported_operand(
                "+", other
            ))
        new = deepcopy(self)
        new.__setitems__(*zip(*other.items()))
        return new

    def __iadd__(self, other: 'DataClass' or dict) -> 'DataClass':
        return self + other

    def __sub__(
            self, other: 'DataClass' or dict or tuple or list or set
    ) -> 'DataClass':
        if not (
            isinstance(other, DataClass) or
            isinstance(other, dict) or
            isinstance(other, tuple) or
            isinstance(other, list) or
            isinstance(other, set)
        ):
            raise TypeError(self.__unsupported_operand(
                "-", other
            ))
        new = deepcopy(self)
        if isinstance(other, DataClass) or isinstance(other, dict):
            other = other.keys()
            ...
        new.__delitems__(other)
        return new

    def __isub__(
            self, other: 'DataClass' or dict or tuple or list or set
    ) -> 'DataClass':
        return self - other

    def __eq__(self, other: 'DataClass' or dict) -> bool:
        if not (isinstance(other, DataClass) or isinstance(other, dict)):
            raise TypeError(self.__unsupported_operand(
                "==", other
            ))
        return 0 == sum([
            not self.__getitem__(key) == value
            for key, value in other.items()
        ])

    def __ne__(self, other: 'DataClass' or dict) -> bool:
        if not (isinstance(other, DataClass) or isinstance(other, dict)):
            raise TypeError(self.__unsupported_operand(
                "!=", other
            ))
        return not self == other

    def __lt__(self, other: 'DataClass' or dict) -> bool:
        if not (isinstance(other, DataClass) or isinstance(other, dict)):
            raise TypeError(self.__unsupported_operand(
                "<", other
            ))
        values = self.__values()
        return 0 == sum([
            key not in values
            for key in other.keys()
        ])
    
    def __gt__(self, other: 'DataClass' or dict) -> bool:
        if not (isinstance(other, DataClass) or isinstance(other, dict)):
            raise TypeError(self.__unsupported_operand(
                ">", other
            ))
        keys = other.keys()
        return 0 == sum([
            key not in keys
            for key in self.__values()
        ])

    def __contains__(self, key: str) -> bool:
        return key in self.__values().keys()

    ...
