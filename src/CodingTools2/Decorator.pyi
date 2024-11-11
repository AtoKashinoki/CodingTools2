

from abc import ABC, abstractmethod
from typing import Callable


class DecoratorSkeleton(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @abstractmethod
    def __call__(self, func: Callable) -> Callable: ...
    ...


class Initializer(DecoratorSkeleton):
    __texture: str
    __args: tuple[any, ...]
    __kwargs: dict[str, any]

    @property
    def args(self) -> tuple[any, ...]: ...
    @property
    def kwargs(self) -> dict[str, any]: ...

    def __init__(self, *args, **kwargs): ...
    def __repr__(self) -> str: ...
    def __call__(self, func: Callable) -> Callable: ...

    ...