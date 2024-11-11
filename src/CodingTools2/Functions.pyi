

from .Inheritance import InheritanceSkeleton
from .Definitions import Os as DefOs


class FunctionsSkeleton(InheritanceSkeleton): ...

class Os(FunctionsSkeleton):
    __name: str
    __command: DefOs.Windows | DefOs.Linux
    @property
    def name(self) -> str: ...
    @property
    def command(
            self
    ) -> DefOs.Windows.Command | DefOs.Linux.Command: ...
    ...

Os = Os()

class Python(FunctionsSkeleton):
    @staticmethod
    def run(_file: str) -> int: ...
    ...

class Convert(FunctionsSkeleton):
    @staticmethod
    def index_from(_position: tuple[int, int], length: int) -> int: ...
    @staticmethod
    def position_from(_index: int, _length: int) -> tuple[int, int]: ...
    @staticmethod
    def private_member(_cls: object, _name: str) -> str: ...
    ...
