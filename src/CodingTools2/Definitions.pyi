
from typing import Callable
from .Inheritance import DataClass


class DefinitionsSkeleton(DataClass): ...


class System(DefinitionsSkeleton):
    EXIT: int = 0
    ERROR: int = 1
    REBOOT: int = 2
    ...

class Os(DefinitionsSkeleton):
    class Windows(DefinitionsSkeleton):
        name: str = "nt"
        class Command(DefinitionsSkeleton):
            python: str = "python {}"
            clear: str = "cls"
            ...
        ...
    class Linux(DefinitionsSkeleton):
        name: str = "posix"
        class Command(DefinitionsSkeleton):
            python: str = "python {}"
            clear: str = "clear"
            ...
        ...

    def __getitem__(self, key: str): ...
    ...

Os = Os()

class Format(DefinitionsSkeleton):
    private_member: str = "_{}{}"
    repr_base: str = "{}{}"
    ...

class Sep(DefinitionsSkeleton):
    or_: str = " or "
    ...

class Operator(DefinitionsSkeleton):
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

class Calculate(DefinitionsSkeleton):
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

class Index(DefinitionsSkeleton):
    X, Y, Z = range(3)
    ...

class Key(DefinitionsSkeleton): ...

class ANSIKeys(DefinitionsSkeleton):
    KEY: str = "\033["
    @staticmethod
    def texture(key: int) -> str: ...
    ...

class ANSI(DefinitionsSkeleton):
    class Texture(DefinitionsSkeleton):
        CLEAR: str
        class Font(DefinitionsSkeleton):
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

        class FontColor(DefinitionsSkeleton):
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

        class BackgroundColor(DefinitionsSkeleton):
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

class Msvcrt(DefinitionsSkeleton):
    class Key(DefinitionsSkeleton):
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

