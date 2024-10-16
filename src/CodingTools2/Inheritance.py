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


""" Skeleton """


class InheritanceSkeleton(ABC):
    """ Inheritance class base """
    ...


""" Inheritance classes """


class DataClass(InheritanceSkeleton):
    """ DataClass base """

    """ values """
    __value_types: set[type] = {str, int, float, bool, tuple, list, dict, set}

    """ properties """
    @property
    def value_types(self) -> set[type]: return self.__value_types

    def __init__(self, **kwargs):
        """ Initialize values """
        [setattr(self, key, value) for key, value in kwargs.items()]
        self.__value_types = DataClass.__value_types
        return

    def __values(self) -> dict:
        """ Return validated attributes """
        return {
            key: value
            for __ins_cls__ in (self, self.__class__)
            for key, value in __ins_cls__.__dict__.items()
            if isinstance(value, tuple(self.__value_types))
            if 0 ==  sum([
                key[1:len(name)+1] ==  name
                for name in (self.__class__.__name__, DataClass.__name__)
            ])
        }

    def keys(self):
        """ Return attributes keys"""
        return self.__values().keys()

    def __getitem__(self, key: str) -> any:
        """ Get data from data class """
        return self.__values()[key]

    def __setitem__(self, key: str, value) -> None:
        """ Set data in  data class """
        self.__values()[key] = value
        return

    def __repr__(self) -> str:
        return "{}".format(self.__values())
