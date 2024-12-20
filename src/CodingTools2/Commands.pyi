
from abc import abstractmethod
from typing import Callable
from .Inheritance import InheritanceSkeleton


class CommandSkeleton(InheritanceSkeleton):
    KEYS: dict[str, str]
    COMMAND_NOT_FOUND: str
    RUN: str
    SUCCESS: str
    OVERWRITE: str
    __args: tuple[str, ...]
    @abstractmethod
    def commands(self, _args: tuple[str, ...]) -> None: ...
    def command(self, _options: tuple[str, ...]) -> None: ...
    def __call__(self) -> None: ...
    def search_method(self, _name: str) -> Callable: ...
    def execute_command_function(self) -> str | None: ...
    ...


class Initialize(CommandSkeleton):
    KEYS: str
    def commands(self, _args: tuple[str, ...]) -> None: ...
    help_message: str
    def help(self, _options: tuple[str, ...]) -> None: ...
    pyproject: str
    pyproject_exists: str
    toml_text: str
    def toml(self, _options: tuple[str, ...]) -> None: ...
    def module(self, _options: tuple[str, ...]) -> None: ...
    ...
