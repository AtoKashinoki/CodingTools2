

unsupported_operand_format: str
def unsupported_operand(
        operator: str, self_name: str, other_name: str
) -> str: ...
args_empty: str


class PreventExecution(SyntaxError):
    def __init__(self, __file__:str): ...
    ...


class Exit(Exception):
    def __init__(self): ...
    ...

