

from .Inheritance import InheritanceSkeleton


class FunctionsSkeleton(InheritanceSkeleton): ...

class Convert(FunctionsSkeleton):
    @staticmethod
    def index_from(_position: tuple[int, int], length: int) -> int: ...
    @staticmethod
    def position_from(_index: int, _length: int) -> tuple[int, int]: ...
    ...
