"""
    CodingTools.Commands

This file contain command processes for developing programs.
"""

""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """

import os
import sys
from abc import abstractmethod
from .Inheritance import InheritanceSkeleton


""" Skeleton """


class CommandSkeleton(InheritanceSkeleton):
    """ Command class base """

    """ values """
    # constants
    KEYS: dict[str, str]
    COMMAND_NOT_FOUND: str = "Command not found."
    SUCCESS: str = "The process finished successfully."
    OVERWRITE = (
        "Do you want to overwrite it?\n"
        "[yes | no] -> "
    )

    # instants
    __args: tuple[str, ...]

    """ properties """

    """ processes """
    @abstractmethod
    def commands(self, _args: tuple[str, ...]) -> None:
        """ Call commands """
        return

    def command(self, _options: tuple[str, ...]) -> None:
        """ command function """
        return

    def __call__(self) -> None:
        """ Call command process """
        self.__args = tuple(sys.argv[1:])
        self.commands(self.__args)
        return

    def search_method(self, _name: str):
        """ Search and return method from self """
        return getattr(self, _name)

    def execute_command_function(self) -> str | None:
        """ Execute command function """
        command = self.__args[0]
        key = self.KEYS[command] if command in self.KEYS else None
        if key is None:
            print(self.COMMAND_NOT_FOUND)
            key = "help"
        self.search_method(key)(self.__args[1:])
        return key
    ...


""" Commands """

""" Initialize command """


class Initialize(CommandSkeleton):
    """ Initialize command """

    """ values """
    # constants
    KEYS: dict[str, str] = {
        "help": "help", "-h": "help",
        "toml": "toml",
        "module": "module",
    }

    # instances

    """ properties """

    """ processes """
    def commands(self, _args: tuple[str, ...]) -> None:
        self.execute_command_function()
        return

    """ commands """

    help_message: str = (
        "help\n"
        "   command\n"
        "       help, -h        : Show help of this command\n"
        "       toml            : Create toml file\n"
        "       pyi {options}   : Create pyi files\n"
    )
    def help(self, _options: tuple[str, ...]) -> None:
        """ Show help command """
        print(self.help_message)
        return

    pyproject = "pyproject.toml"
    pyproject_exists: str = f"{pyproject} file already exists.\n"
    toml_text: str = (
        '[build-system]\n'
        'requires = ["setuptools>=<SETUPTOOLS VERSION>"]\n'
        'build-backend = "setuptools.build_meta"\n'
        '\n\n'
        '[project]\n'
        'name = "<MODULE NAME>"\n'
        'version = "0.0.0"\n'
        'description = "<DESCRIPTION>"\n'
        '\n'
        'readme = "README.md"\n'
        'license = {file="LICENSE"}\n'
        '\n'
        'requires-python = ">=<PYTHON VERSION>"\n'
        'dependencies = [\n'
        ']\n'
        '\n'
        'authors = [\n'
        '   {name="<NAME>", email="<EMAIL>"}\n'
        ']\n'
        'classifiers = [\n'
        '   "Programming Language :: Python :: <PYTHON VERSION>",\n'
        '   "License :: OSI Approved :: <LICENSE>",\n'
        '   "Operating System :: Microsoft :: Windows :: <WINDOWS VERSION>"\n'
        ']\n'
        '\n\n'
        '[project.urls]\n'
        '"Homepage" = "<PAGE URL>"\n'
        '"Bug Tracker" = "<PAGE URL>"\n'
        '\n\n'
        '[project.scripts]\n'
    )

    def toml(self, _options: tuple[str, ...]) -> None:
        """ Create toml file command """
        if os.path.isfile(self.pyproject):
            message = self.pyproject_exists + self.OVERWRITE
            if not input(message) == "yes":
                return
            ...

        with open(self.pyproject, "w") as pyproject_toml:
            pyproject_toml.write(self.toml_text)
            ...

        print(self.SUCCESS)
        return

    def module(self, _options: tuple[str, ...]) -> None:
        """ Create module command """
        self.toml(_options[1:])

        if len(_options) > 1:
            module_name: str = _options[0]
            ...
        else:
            module_name = "None"
            ...


        src = "./src"
        if not os.path.isdir(src): os.mkdir(src)
        module_path: str = f"{src}/{module_name}"
        if not os.path.isdir(module_path): os.mkdir(module_path)

        with open(f"{module_path}/__init__.py", "w"): ...

        print(self.SUCCESS)
        return

    ...

initialize = Initialize()
