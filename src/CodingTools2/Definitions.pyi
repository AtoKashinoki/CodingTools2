
from typing import Callable
from .Inheritance import DataClass


class DefinitionSkeleton(DataClass): ...


class System(DefinitionSkeleton):
    EXIT: int = 0
    ERROR: int = 1
    REBOOT: int = 2
    ...

class Os(DefinitionSkeleton):
    class Windows(DefinitionSkeleton):
        name: str = "nt"
        class Command(DefinitionSkeleton):
            python: str = "python {}"
            clear: str = "cls"
            ...
        ...
    class Linux(DefinitionSkeleton):
        name: str = "posix"
        class Command(DefinitionSkeleton):
            python: str = "python {}"
            clear: str = "clear"
            ...
        ...

    def __getitem__(self, key: str): ...
    ...

Os = Os()

class Format(DefinitionSkeleton):
    private_member: str = "_{}{}"
    repr_base: str = "{}{}"
    ...

class Sep(DefinitionSkeleton):
    or_: str = " or "
    ...

class Operator(DefinitionSkeleton):
    add: str = "+"
    sub: str = "-"
    mul: str = "*"
    div: str = "/"
    floor: str = "//"
    mod: str = "%"
    pow: str = "**"
    eq = "=="
    ne = "!="
    lt = "<"
    le = "<="
    gt = ">"
    ge = ">="
    ...

class Calculate(DefinitionSkeleton):
    add = lambda x, y: x + y
    sub = lambda x, y: x - y
    mul = lambda x, y: x * y
    div = lambda x, y: x / y
    floor = lambda x, y: x // y
    mod = lambda x, y: x % y
    pow = lambda x, y: x ** y
    eq = lambda x, y: x == y
    ne = lambda x, y: x != y
    lt = lambda x, y: x < y
    le = lambda x, y: x <= y
    gt = lambda x, y: x > y
    ge = lambda x, y: x >= y
    ...

class Index(DefinitionSkeleton):
    X, Y, Z = range(3)
    ...

class Key(DefinitionSkeleton): ...

class ANSIKeys(DefinitionSkeleton):
    KEY: str = "\033["
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
            Clear: str
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

        ...

    ...

class Msvcrt(DefinitionSkeleton):
    class Key(DefinitionSkeleton):
        BackSpace = 8
        BS = BackSpace
        Enter = 13
        Space = 32
        Del = 83

        n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 = range(48, 48 + 10)

        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = \
            range(65, 65 + 26)
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = \
            range(97, 97 + 26)

        s1, s2, s3, s4, s5, s6, s7, s8, s9 = range(33, 33 + 9)
        Comma, Hyphen, Dot, Slash = range(44, 44 + 4)
        Colon, SemiColon = range(58, 58 + 2)
        At = 64
        BracketT, BackSlash, BracketE = range(91, 91 + 3)

        Top, Left, Right, Bottom = 72, 75, 77, 80
        ...

    alphabet: str
    alphabet_keys: tuple[int]
    alphabet_dict: dict[int, str]
    alphabet_rev_dict: dict[int, str]

    ...

