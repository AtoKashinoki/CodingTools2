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


""" Definition skeleton """


class DefinitionSkeleton(DataClass):
    """ Definition values class skeleton """
    ...


""" Definitions """

""" System """


class System(DefinitionSkeleton):
    """ System definitions """
    EXIT = 0
    ERROR = 1
    REBOOT = 2
    ...


""" Index and Key """


class Index(DefinitionSkeleton):
    """ Index definitions """
    X, Y, Z = range(3)
    ...


class Key(DefinitionSkeleton):
    """ Key definitions """
    ...


""" ANSI """


class ANSIKeys(DefinitionSkeleton):
    """ ANSI keys definitions """
    KEY = "\033["

    """ return ansi texture key """
    @staticmethod
    def texture(key: int) -> str: return f"{ANSIKeys.KEY}{key}m"
    ...


class ANSI(DefinitionSkeleton):
    """ ANSI definitions """

    """ Texture """
    class Texture(DefinitionSkeleton):
        """ Texture definitions """

        """ Clear """
        CLEAR = ANSIKeys.texture(0)

        """ Font """
        class Font(DefinitionSkeleton):
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
        class FontColor(DefinitionSkeleton):
            """ Font color definitions """
            BLACK = ANSIKeys.texture(30)
            RED = ANSIKeys.texture(31)
            GREEN = ANSIKeys.texture(32)
            YELLOW = ANSIKeys.texture(33)
            BLUE = ANSIKeys.texture(34)
            MAGENTA = ANSIKeys.texture(35)
            CYAN = ANSIKeys.texture(36)
            GRAY = ANSIKeys.texture(37)
            WHITE = ANSIKeys.texture(38)
            ...

        """ Background color definitions """
        class BackgroundColor(DefinitionSkeleton):
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

