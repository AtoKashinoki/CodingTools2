"""
    CodingTools2

This file contain CodingTools2 processes.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" import CodingTools2 processes """


try:
    from . import Definitions
    ...
except ImportError as error:
    Definitions = ImportError(error)
    ...


try:
    from . import Inheritance
    ...
except ImportError as error:
    Inheritance = ImportError(error)
    ...


try:
    from . import Functions
    ...
except ImportError as error:
    Functions = ImportError(error)
    ...

