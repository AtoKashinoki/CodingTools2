"""
    CodingTools2.Type

This file contain types for developing programs.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from typing import Callable
from copy import deepcopy
from CodingTools2.Errors import (
    args_empty,
    different_size,
    unsupported_operand,
)
from CodingTools2.Functions import (
    Generate, Get,
    Validate,
)
from CodingTools2.Definitions import (
    Format, Sep,
    Operator, Calculate,
)

""" Types """


class Vector(object):
    """ Vector contain class """

    """ values """

    # instance
    __data: list = None
    __size: tuple = None

    """ properties """
    @property
    def data(self) -> tuple: return tuple(self.__data)
    @property
    def size(self) -> tuple: return self.__size

    """ processes """
    # class
    @classmethod
    def zeros(cls, _size: tuple[int, int]) -> 'Vector':
        return cls(size=_size)

    @classmethod
    def ones(cls, _size: tuple[int, int]) -> 'Vector':
        return cls(size=_size, initial_value=1)

    # instance
    def __init__(
            self,
            _data: list = None,
            size:tuple[int, ...] = None,
            initial_value: int | float = 0,
    ):
        """ Initialize vector data """
        if _data is None and size is None:
            raise TypeError(args_empty.format(
                self.__class__.__name__,
                Sep.or_.join(("data", "size"))
            ))

        if _data is None:
            _data = Generate.list_frame(size, initial_value)
            ...
        elif size is None:
            size = Get.list_size(_data)
            ...

        self.__data = deepcopy(_data)
        self.__size = size
        return

    def __repr__(self) -> str:
        return Format.repr_base.format(
            self.__class__.__name__,
            self.__data,
        )

    """ operators """
    @staticmethod
    def calculate(
            _list1: list | tuple, _list2: list | tuple,
            calculate: Callable
    ) -> list:
        """ Calculate a list """
        return [
            calculate(d1, d2) if not isinstance(d1, list) else
            Vector.calculate(d1, d2, calculate)
            for d1, d2 in zip(_list1, _list2)
        ]

    def validate_calculator(
            self,
            other: 'Vector' or tuple or list,
            operator: str
    ) -> None:
        """ Validate if it can be calculated """
        if isinstance(other, Vector):
            if self.size != other.size:
                raise TypeError(different_size)
            return

        elif isinstance(other, tuple) or isinstance(other, list):
            if self.size != Get.list_size(other):
                raise TypeError(different_size)
            return

        raise TypeError(unsupported_operand(
            operator,
            self.__class__.__name__, other.__class__.__name__
        ))

    def __add__(self, other: 'Vector' or tuple or list) -> 'Vector':
        self.validate_calculator(other, Operator.add)
        return Vector(self.calculate(
            self.__data, list(other),
            Calculate.add,
        ))

    def __iadd__(self, other: 'Vector' or tuple or list) -> 'Vector':
        return self + other

    def __radd__(self, other: 'Vector' or tuple or list) -> 'Vector':
        return Vector(other) + self

    def __sub__(self, other: 'Vector' or tuple or list) -> 'Vector':
        self.validate_calculator(other, Operator.sub)
        return Vector(self.calculate(
            self.__data, list(other),
            Calculate.sub,
        ))

    def __isub__(self, other: 'Vector' or tuple or list) -> 'Vector':
        return self - other

    def __rsub__(self, other: 'Vector' or tuple or list) -> 'Vector':
        return Vector(other) - self

    def __mul__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        if Validate.number(other):
            return Vector(self.calculate(
                self.__data,
                Vector(size=self.size, initial_value=other).data,
                Calculate.mul,
            ))

        self.validate_calculator(other, Operator.mul)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.mul,
        ))

    def __imul__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self * other

    def __rmul__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self * other

    def __truediv__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        if Validate.number(other):
            return Vector(self.calculate(
                self.__data,
                Vector(size=self.size, initial_value=other).data,
                Calculate.div,
            ))

        self.validate_calculator(other, Operator.div)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.div,
        ))

    def __itruediv__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self / other

    def __rtruediv__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return Vector(other) / self

    def __mod__(self, other: 'Vector' or tuple or list or int or float) -> 'Vector':
        if Validate.number(other):
            return Vector(self.calculate(
                self.__data,
                Vector(size=self.size, initial_value=other).data,
                Calculate.mod,
            ))

        self.validate_calculator(other, Operator.mod)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.mod,
        ))

    def __imod__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self % other

    def __rmod__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return Vector(other) % self

    ...
