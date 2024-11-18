"""
    CodingTools2.Type

This file contain types for developing programs.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from CodingTools2.Errors import args_empty
from CodingTools2.Functions import Generate, Get
from CodingTools2.Definitions import Format, Sep


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
            initial_value: int = 0,
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

        self.__data = _data
        self.__size = size
        return

    def __repr__(self) -> str:
        return Format.repr_base.format(
            self.__class__.__name__,
            self.__data,
        )

    ...
