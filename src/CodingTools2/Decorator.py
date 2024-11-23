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
from time import time
from typing import Callable, ClassVar
from Inheritance import DataClass


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

    def __repr__(self) -> str:
        return self.__texture.format(self.__args, self.__kwargs)

    def __call__(self, func: Callable) -> Callable:
        """ Return instance """
        return func(*self.__args, **self.__kwargs)

    ...


""" Tester """


class Test(DataClass):
    """ Tester decorators """

    class Repeat(DecoratorSkeleton):
        """ Repeat tester """

        """ values """
        # class
        __process_number: int = 0
        # instance
        __number_of_times: int = None

        def __init__(self, _number_of_times: int) -> None:
            """ Initialize settings """
            self.__number_of_times: int = _number_of_times
            return

        @classmethod
        def start_process(cls):
            cls.__process_number += 1
            return

        @classmethod
        def end_process(cls):
            cls.__process_number -= 1
            return

        def __call__(self, _func: Callable) -> Callable:
            """ Decorate a function """

            """ Decorator """
            def wrapper(*args, **kwargs) -> any:
                """ Run repeating test """
                self.start_process()
                print(
                    f"[{self.__process_number}] "
                    f"Repeat for {self.__number_of_times} times..."
                )

                results = tuple(
                    _func(*args, **kwargs)
                    for _ in range(self.__number_of_times)
                )

                print(f"[{self.__process_number}] Success.")
                self.end_process()
                return results

            return wrapper

    class Time(DecoratorSkeleton):
        """ Time tester """

        """ values """
        __target: Callable = None

        def __init__(self, _func) -> None:
            """ Set target function """
            self.__target = _func
            return

        def __call__(self, *args, **kwargs) -> any:
            """ Run time test wrapper """

            """ run """
            start = time()
            result = self.__target(*args, **kwargs)
            end = time()

            """ result """
            print(f"Run time: {end-start}")

            return result

        ...

    class BlankLine(DecoratorSkeleton):
        """ Print BlankLine """

        """ values """
        __func: Callable = None

        """ processes """
        def __init__(self, _func: Callable) -> None:
            """ Set target function """
            self.__func = _func
            return

        def __call__(self, *args, **kwargs) -> any:
            """ Add BlankLine wrapper """
            result = self.__func(*args, **kwargs)
            print()
            return result

    ...
