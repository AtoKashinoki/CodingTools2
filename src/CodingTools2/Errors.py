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


""" messages """


unsupported_operand_format: str = \
    "unsupported operand type(s) for {}: '{}' and '{}'"

def unsupported_operand(
        operator: str, self_name: str, other_name: str
) -> str:
    return unsupported_operand_format.format(
        operator, self_name, other_name
    )

args_empty = (
    "{} class args cannot be empty.\n"
    "   Need to provide either {}."
)
different_size = "Cannot be calculated due to different sizes"


""" errors """


class Exit(Exception):
    """ Exit the program """

    def __init__(self):
        """ Initialize message """
        super().__init__("Exit the program.")
        return

    ...
