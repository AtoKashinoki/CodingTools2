"""
    CodingTools.Decorator

This file contain decorator functions for developing programs.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from .Errors import PreventExecution
    raise PreventExecution(__name__)


""" imports """


from abc import ABC, abstractmethod
from typing import Callable


""" decorator class skeleton  """


class DecoratorSkeleton(ABC):
    """ Decorator class base """

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize decorator """
        return

    @abstractmethod
    def __call__(self, func: Callable) -> Callable:
        """ Decorate a function """
        return NotImplemented
    ...


""" decorators """


class Initializer(DecoratorSkeleton):
    """ Initializer decorator """

    """ values """
    # class
    __texture: str = "__init__({}, {})"
    # instance
    __args: tuple[any, ...]
    __kwargs: dict[str, any]

    """ properties """
    @property
    def args(self) -> tuple[any, ...]: return self.__args
    @property
    def kwargs(self) -> dict[str, any]: return self.__kwargs

    """ processes """
    # instance
    def __init__(self, *args, **kwargs) -> None:
        """ Setting initializer values """
        self.__args = args
        self.__kwargs = kwargs
        return

    def __repr__(self):
        return self.__texture.format(self.__args, self.__kwargs)

    def __call__(self, func: Callable) -> Callable:
        """ Return instance """
        return func(*self.__args, **self.__kwargs)

    ...
