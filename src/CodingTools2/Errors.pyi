

args_empty: str


class PreventExecution(SyntaxError):
    def __init__(self, __file__:str): ...
    ...


class Exit(Exception):
    def __init__(self): ...
    ...

