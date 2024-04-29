from datetime import datetime
from os.path import isfile
from types import FunctionType


class Logger:
    """
    Placeholders:
        %date% - Current date in format {DD.MM.YYYY}\n
        %time24% - Current time in format {HH:MM}\n
        %time12% - Current time in format {HH:MM am/pm}\n
        %type% - Entry type\n
        %text% - Entry text
    :param str _format: Entry format
    :raise TypeError:
    """

    def __init__(self, _format='%date% %time24% [%type%]: %text%'): ...
    def add_listener(self, listener: str | FunctionType):
        """
        Adding listener to logger
        :param listener: Listener
        :raise TypeError:
        """
        ...
    def custom(self, _type: str, text: str) -> None:
        """
        Creates a custom entry
        :param str _type: Entry type
        :param str text: Entry text
        :raise TypeError:
        """
        ...
    def debug(self, text: str) -> None:
        """
        Creates a debug entry
        :param text: Entry text
        :raise TypeError:
        """
        ...
    def info(self, text: str) -> None:
        """
        Creates an info entry
        :param text: Entry text
        :raise TypeError:
        """
        ...
    def warn(self, text: str) -> None:
        """
        Creates a warn entry
        :param text: Entry text
        :raise TypeError:
        """
        ...
    def error(self, text: str) -> None:
        """
        Creates an error entry
        :param text: Entry text
        :raise TypeError:
        """
        ...
    def fatal(self, text: str) -> None:
        """
        Creates a fatal entry
        :param text: Entry text
        :raise TypeError:
        """
        ...
