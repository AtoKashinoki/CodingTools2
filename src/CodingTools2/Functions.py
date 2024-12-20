"""
    CodingTools2.Functions

This file contain functions for developing programs.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports  """


import os
import sys
from .Definitions import Format, Os as DefOs
from .Inheritance import InheritanceSkeleton
from .Decorator import Initializer


""" Functions class skeleton """


class FunctionsSkeleton(InheritanceSkeleton):
    """ Functions class skeleton """
    ...


""" Os """


@Initializer()
class Os(FunctionsSkeleton):
    """ Functions about os """

    """ values """
    __name = os.name
    __command = DefOs[__name].Command

    """ properties """
    @property
    def name(self) -> str: return self.name
    @property
    def command(
            self
    ) -> DefOs.Windows.Command | DefOs.Linux.Command:
        return self.__command

    ...

Os: Os


""" Python """


class Python(FunctionsSkeleton):
    """ Functions about python """

    @staticmethod
    def run(_file: str) -> int:
        """ Run python file """
        python = Os.command.python
        path = "{}\\{}".format(os.getcwd(), _file)
        exit_code = os.system(python.format(path))
        return exit_code

    ...


""" Convert functions """


class Convert(FunctionsSkeleton):
    """ Convert functions """

    @staticmethod
    def index_from(_position: tuple[int, int], _length: int) -> int:
        """ Convert position to index """
        if not 0 <= _position[0] < _length: raise IndexError
        return _position[0] + _position[1] * _length

    @staticmethod
    def position_from(_index: int, _length: int) -> tuple[int, int]:
        """ Convert index to position """
        return _index % _length, _index // _length

    @staticmethod
    def private_member(_cls: object, _name: str) -> str:
        return Format.private_member.format(_cls, _name)

    ...


""" Generator functions """


class Generate(FunctionsSkeleton):
    """ Generator functions """

    @staticmethod
    def list_frame(_size: tuple[int, ...], _initial_value: int = 0) -> list:
        """ Generate list from size """
        return [
            _initial_value if len(_size) <= 1 else
            Generate.list_frame(_size[:-1], _initial_value)
            for _ in range(_size[-1])
        ]

    ...


""" Getter """


class Get(FunctionsSkeleton):
    """ Getter functions """

    @staticmethod
    def list_size(_list: list | tuple) -> tuple[int] | tuple[int, ...]:
        """ Return size of list """

        # recall function
        def size_getter(_list: list) -> list[int] | tuple[int, ...]:
            """ Return size of list """
            if not isinstance(_list, list):
                return []
            if len(_list) < 1:
                return [0]
            return size_getter(_list[0]) + [len(_list)]


        return tuple(size_getter(list(_list)))

    ...


""" Validator functions """


class Validate(FunctionsSkeleton):
    """ Validate functions """

    @staticmethod
    def number(_target: any) -> bool:
        return isinstance(_target, int) or isinstance(_target, float)

    ...
