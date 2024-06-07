from typing import Callable

DEBUG = 10
INFO = 20
WARN = 30
ERROR = 40
FATAL = 50


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
    def __init__(self, _format: str='%date% %time24% [%type%]: %text%'): ...

    def add_listener(self, listener: str | Callable, min_level: int=0): ...

    def custom(self, _type: str, text: str, level: int=100) -> str: ...

    def debug(self, text: str) -> str: ...

    def info(self, text: str) -> str: ...

    def warn(self, text: str) -> str: ...

    def error(self, text: str) -> str: ...

    def fatal(self, text: str): ...
