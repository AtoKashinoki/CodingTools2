"""
    CodingTools2.Errors

This file contain error classes for developing programs.
"""


""" Prevent execute this file """


class PreventExecution(SyntaxError):
    """ Prevent execute this file """

    def __init__(self, __file__: str):
        """ Initialize message """
        path = __file__.split("\\")
        super().__init__(f"'{path[-1]}' file is not executable.")
        return

    ...

if __name__ == '__main__':
    raise PreventExecution(__file__)

