"""
    CodingTools2.Functions

This file contain functions for developing programs.
"""
from fileinput import lineno

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


""" ANSI functions """


class ANSI(FunctionsSkeleton):
    """ ANSI functions """
    ...


""" Convert functions """


class Convert(FunctionsSkeleton):
    """ Convert functions """
    @staticmethod
    def pyi_from_py(_py_text: str) -> str:
        """ Convert pyi text from py text """
        keys = ("class ", "def ", "@", )

        pass

        return
    ...
