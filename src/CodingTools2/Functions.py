"""
    CodingTools2.Functions

This file contain functions for developing programs.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports  """


from .Inheritance import InheritanceSkeleton


""" Functions class skeleton """


class FunctionsSkeleton(InheritanceSkeleton):
    """ Functions class skeleton """
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

    ...

