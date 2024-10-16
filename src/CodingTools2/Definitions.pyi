
from .Inheritance import DataClass


class DefinitionSkeleton(DataClass): ...


class System(DefinitionSkeleton):
    EXIT: int
    ERROR: int
    REBOOT: int
    ...

class Index(DefinitionSkeleton):
    X: int
    Y: int
    Z: int
    ...

class Key(DefinitionSkeleton): ...

class ANSIKeys(DefinitionSkeleton):
    KEY: str
    @staticmethod
    def texture(key: int) -> str: ...
    ...

class ANSI(DefinitionSkeleton):
    class Texture(DefinitionSkeleton):
        CLEAR: str
        class Font(DefinitionSkeleton):
            BOLD: str
            THIN: str
            ITALIC: str
            UNDER_BAR: str
            BLINK: str
            FIRST_BLINK: str
            INVERT: str
            HIDE: str
            DelTHIN: str
            DelITALIC: str
            DelUNDER_BAR: str
            DelBLINK: str
            DelFIRST_BLINK: str
            DelINVERT: str
            DelHIDE: str
            ...

        class FontColor(DefinitionSkeleton):
            BLACK: str
            RED: str
            GREEN: str
            YELLOW: str
            BLUE: str
            MAGENTA: str
            CYAN: str
            GRAY: str
            WHITE: str
            ...

        class BackgroundColor(DefinitionSkeleton):
            BLACK: str
            RED: str
            GREEN: str
            YELLOW: str
            BLUE: str
            MAGENTA: str
            CYAN: str
            GRAY: str
            ...
