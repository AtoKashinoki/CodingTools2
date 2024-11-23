"""
    CodingTools2.Type

This file contain types for developing programs.
"""
from turtledemo.forest import doit2

from Tools.scripts.win_add2path import modify

""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from typing import Callable
from copy import deepcopy
from .Errors import Message
from .Functions import (
    Generate, Get,
    Validate,
)
from .Definitions import (
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
            raise TypeError(Message.args_empty.format(
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

    # Arithmetic

    @staticmethod
    def calculate(
            _list1: list | tuple, _list2: list | tuple,
            calculate: Callable
    ) -> list | list[int, ...]:
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
                raise TypeError(Message.different_size)
            return

        elif isinstance(other, tuple) or isinstance(other, list):
            if self.size != Get.list_size(other):
                raise TypeError(Message.different_size)
            return

        raise TypeError(Message.unsupported_operand(
            operator,
            self.__class__.__name__, other.__class__.__name__
        ))

    def reform_cal_data(self, other) -> tuple | list:
        """ Reform data for using in calculation """
        if Validate.number(other):
            other = Vector(size=self.size, initial_value=other).data
            ...
        elif isinstance(other, Vector):
            other = other.data
            ...
        return other

    def __add__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.mul)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.add,
        ))

    def __iadd__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self + other

    def __radd__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self + other

    def __sub__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.sub)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.sub,
        ))

    def __isub__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self - other

    def __rsub__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return Vector(other) - self

    def __mul__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
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
        other = self.reform_cal_data(other)
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

    def __floordiv__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.floor)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.floor,
        ))

    def __ifloordiv__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return self // other

    def __rfloordiv__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        return Vector(other) // self

    def __mod__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
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

    def __pow__(
            self,
            power: 'Vector' or tuple or list or int or float,
            modulo=None
    ) -> 'Vector':
        power = self.reform_cal_data(power)
        self.validate_calculator(power, Operator.pow)
        return Vector(self.calculate(
            self.__data, power,
            Calculate.pow,
        ))

    def __ipow__(
            self, power: 'Vector' or tuple or list or int or float,
            modulo=None
    ) -> 'Vector':
        return self ** power

    def __rpow__(
            self, power: 'Vector' or tuple or list or int or float,
            modulo=None
    ) -> 'Vector':
        return Vector(power) ** power

    def __neg__(self) -> 'Vector':
        return self * -1

    # Comparison

    def __eq__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.eq)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.eq,
        ))

    def __ne__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.ne)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.ne,
        ))

    def __lt__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.lt)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.lt,
        ))

    def __le__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.le)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.le,
        ))

    def __gt__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        other = self.reform_cal_data(other)
        self.validate_calculator(other, Operator.gt)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.gt,
        ))

    def __ge__(
            self, other: 'Vector' or tuple or list or int or float
    ) -> 'Vector':
        self.reform_cal_data(other)
        self.validate_calculator(other, Operator.ge)
        return Vector(self.calculate(
            self.__data, other,
            Calculate.ge,
        ))

    def eq_data(self, other: 'Vector' or tuple or list) -> bool:
        """ Return self.data == other.data """
        if isinstance(other, Vector):
            other = other.data
            ...
        return self.data == tuple(other)

    """ container """

    def __getitem__(self, key: int) -> any:
        return self.__data[key]

    def __setitem__(self, key: int, value: any) -> None:
        self.__data[key] = value
        return

    def __delitem__(self, key: int) -> None:
        del self.__data[key]
        return

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self):
        return iter(self.__data)

    def __contains__(self, data: any) -> bool:
        return data in self.__data

    ...


class Vector1D(Vector):
    """ Vector class of 2 dimension """

    """ processes """

    # instance
    def __init__(
            self,
            _data:
                tuple[int, int] | list[int, int] | tuple | list | 'Vector1D'
                = None,
            length: int = None,
            initial_value: int = 0,
    ):
        """ Initialize vector data """
        if _data is None and length is None:
            raise TypeError(Message.args_empty)

        if _data is None:
            _data = [initial_value for _ in range(length)]
            ...
        elif length is None:
            length = len(_data)
            ...

        super().__init__(_data, (length,))
        return

    """ operators """

    def __add__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d + other
                for d in self.data
            ])

        return Vector1D([
            d1 + d2
            for d1, d2 in zip(self.data, other)
        ])

    def __sub__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d - other
                for d in self.data
            ])

        return Vector1D([
            d1 - d2
            for d1, d2 in zip(self.data, other)
        ])

    def __mul__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d * other
                for d in self.data
            ])

        return Vector1D([
            d1 * d2
            for d1, d2 in zip(self.data, other)
        ])

    def __truediv__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d / other
                for d in self.data
            ])

        return Vector1D([
            d1 / d2
            for d1, d2 in zip(self.data, other)
        ])

    def __floordiv__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d // other
                for d in self.data
            ])

        return Vector1D([
            d1 // d2
            for d1, d2 in zip(self.data, other)
        ])

    def __mod__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d % other
                for d in self.data
            ])

        return Vector1D([
            d1 % d2
            for d1, d2 in zip(self.data, other)
        ])

    def __pow__(
            self, power: 'Vector' or int or float, modulo=None
    ) -> 'Vector1D':
        if Validate.number(power):
            return Vector1D([
                d ** power
                for d in self.data
            ])

        return Vector1D([
            d1 ** d2
            for d1, d2 in zip(self.data, power)
        ])

    # Comparison

    def __eq__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d == other
                for d in self.data
            ])

        return Vector1D([
            d1 == d2
            for d1, d2 in zip(self.data, other)
        ])

    def __ne__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d != other
                for d in self.data
            ])

        return Vector1D([
            d1 != d2
            for d1, d2 in zip(self.data, other)
        ])

    def __lt__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d < other
                for d in self.data
            ])

        return Vector1D([
            d1 < d2
            for d1, d2 in zip(self.data, other)
        ])

    def __le__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d <= other
                for d in self.data
            ])

        return Vector1D([
            d1 <= d2
            for d1, d2 in zip(self.data, other)
        ])

    def __gt__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d > other
                for d in self.data
            ])

        return Vector1D([
            d1 > d2
            for d1, d2 in zip(self.data, other)
        ])

    def __ge__(self, other: 'Vector1D' or int or float) -> 'Vector1D':
        if Validate.number(other):
            return Vector1D([
                d >= other
                for d in self.data
            ])

        return Vector1D([
            d1 >= d2
            for d1, d2 in zip(self.data, other)
        ])

    ...
