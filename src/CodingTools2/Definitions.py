"""
    CodingTools2.Definitions

This file contain definition constants for developing programs.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from .Inheritance import DataClass
from .Decorator import Initializer


""" Definition skeleton """


class DefinitionsSkeleton(DataClass):
    """ Definition values class skeleton """
    ...


""" Definitions """

""" System """


class System(DefinitionsSkeleton):
    """ System definitions """
    EXIT = 0
    ERROR = 1
    REBOOT = 2
    ...


@Initializer()
class Os(DefinitionsSkeleton):
    """ Os definitions """

    class Windows(DefinitionsSkeleton):
        """ Windows definitions """
        name = "nt"

        class Command(DefinitionsSkeleton):
            python = "python {}"
            clear = "cls"
            ...

        ...

    class Linux(DefinitionsSkeleton):
        """ Linux definitions """
        name = "posix"

        class Command(DefinitionsSkeleton):
            python = "python {}"
            clear = "clear"
            ...

        ...

    def __getitem__(
            self, key: str
    ) -> type[Windows | Linux]:
        """ Return os class """
        match key:
            case self.Windows.name:
                cls = self.Windows
            case self.Linux.name:
                cls = self.Linux
            case _:
                raise KeyError(key)
        return cls

    ...


""" string """


class Format(DefinitionsSkeleton):
    """ Format definitions """
    private_member: str = "_{}{}"
    repr_base: str = "{}{}"
    ...


class Sep(DefinitionsSkeleton):
    """ Sep definitions """
    or_ = " or "
    ...


class Operator(DefinitionsSkeleton):
    """ Operator definitions """
    add = "+"
    sub = "-"
    mul = "*"
    div = "/"
    floor = "//"
    mod = "%"
    pow = "**"
    eq = "=="
    ne = "!="
    lt = "<"
    le = "<="
    gt = ">"
    ge = ">="
    ...


""" calculate """


class Calculate(DefinitionsSkeleton):
    """ Calculate definitions """
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


""" Number """


class Number(DefinitionsSkeleton):
    INF = float('inf')
    ...


""" Index and Key """


class Index(DefinitionsSkeleton):
    """ Index definitions """
    X, Y, Z = range(3)
    ...


class Key(DefinitionsSkeleton):
    """ Key definitions """
    ...


""" ANSI """


class ANSIKeys(DefinitionsSkeleton):
    """ ANSI keys definitions """
    KEY = "\033["

    """ return ansi texture key """
    @staticmethod
    def texture(key: int) -> str: return f"{ANSIKeys.KEY}{key}m"
    ...


class ANSI(DefinitionsSkeleton):
    """ ANSI definitions """

    """ Texture """
    class Texture(DefinitionsSkeleton):
        """ Texture definitions """

        """ Clear """
        CLEAR = ANSIKeys.texture(0)

        """ Font """
        class Font(DefinitionsSkeleton):
            """ Font definitions """
            BOLD = ANSIKeys.texture(1)
            THIN = ANSIKeys.texture(2)
            ITALIC = ANSIKeys.texture(3)
            UNDER_BAR = ANSIKeys.texture(4)
            BLINK = ANSIKeys.texture(5)
            FIRST_BLINK = ANSIKeys.texture(6)
            INVERT = ANSIKeys.texture(7)
            HIDE = ANSIKeys.texture(8)
            DelTHIN = ANSIKeys.texture(22)
            DelITALIC = ANSIKeys.texture(23)
            DelUNDER_BAR = ANSIKeys.texture(24)
            DelBLINK = ANSIKeys.texture(25)
            DelFIRST_BLINK = ANSIKeys.texture(26)
            DelINVERT = ANSIKeys.texture(27)
            DelHIDE = ANSIKeys.texture(28)
            ...

        """ Font color definitions """
        class FontColor(DefinitionsSkeleton):
            """ Font color definitions """
            BLACK = ANSIKeys.texture(30)
            RED = ANSIKeys.texture(31)
            GREEN = ANSIKeys.texture(32)
            YELLOW = ANSIKeys.texture(33)
            BLUE = ANSIKeys.texture(34)
            MAGENTA = ANSIKeys.texture(35)
            CYAN = ANSIKeys.texture(36)
            GRAY = ANSIKeys.texture(37)
            WHITE = ANSIKeys.texture(39)
            Clear = ANSIKeys.texture(39)
            ...

        """ Background color definitions """
        class BackgroundColor(DefinitionsSkeleton):
            """ Background color definitions """
            BLACK = ANSIKeys.texture(40)
            RED = ANSIKeys.texture(41)
            GREEN = ANSIKeys.texture(42)
            YELLOW = ANSIKeys.texture(43)
            BLUE = ANSIKeys.texture(44)
            MAGENTA = ANSIKeys.texture(45)
            CYAN = ANSIKeys.texture(46)
            GRAY = ANSIKeys.texture(47)
            ...

        ...

    ...


""" Msvcrt """


class Msvcrt(DefinitionsSkeleton):
    """ msvcrt definitions """

    class Key(DefinitionsSkeleton):
            """ msvcrt ord keys definitions """

            """ special keys """
            Special = 224
            BackSpace = 8
            BS = BackSpace
            Enter = 13
            Space = 32
            Ins = 82
            Del = 83

            """ number keys """
            n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 = range(48, 48+10)

            """ alphabet keys """
            A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = \
                range(65, 65+26)
            a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = \
                range(97, 97+26)

            """ symbol keys """
            s1, s2, s3, s4, s5, s6, s7, s8, s9 = range(33, 33+9)
            Comma, Hyphen, Dot, Slash = range(44,44+ 4)
            Colon, SemiColon = range(58, 58+2)
            At = 64
            BracketT, BackSlash, BracketE = range(91, 91+3)

            """ Arrow keys """
            Top, Left, Right, Bottom = 72, 75,  77, 80

            ...

    """ alphabet datas definitions """
    alphabet: str = (
        "A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "I",
        "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x", "y", "z",
    )

    alphabet_keys: tuple[int] = tuple([
        Key.A, Key.B, Key.C, Key.D, Key.E, Key.F, Key.G, Key.H, Key.I,
        Key.J, Key.K, Key.L, Key.M, Key.N, Key.O, Key.P, Key.Q, Key.R,
        Key.S, Key.T, Key.U, Key.V, Key.W, Key.X, Key.Y, Key.Z,
        Key.a, Key.b, Key.c, Key.d, Key.e, Key.f, Key.g, Key.h, Key.i,
        Key.j, Key.k, Key.l, Key.m, Key.n, Key.o, Key.p, Key.q, Key.r,
        Key.s, Key.t, Key.u, Key.v, Key.w, Key.x, Key.y, Key.z,
    ])

    alphabet_dict: dict[int, str] = \
        dict(zip(alphabet_keys, alphabet))

    alphabet_rev_dict: dict[int, str] = \
        dict(zip(alphabet, alphabet_keys))

    ...

