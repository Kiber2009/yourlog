from datetime import datetime
from typing import Callable

DEBUG = 10
INFO = 20
WARN = 30
ERROR = 40
FATAL = 50


class Logger:
    def __init__(self, _format='%date% %time24% [%type%]: %text%'):
        if not isinstance(_format, str):
            raise TypeError(f'_format must be str, not {_format.__class__.__name__}')
        self.__listeners = []
        self.__format = _format

    def add_listener(self, listener: str | Callable, min_level=0):
        if not (isinstance(listener, str) or callable(listener)):
            raise TypeError(f'listener must be str | Callable, not {listener.__class__.__name__}')
        self.__listeners.append([listener, min_level])
        return listener

    def custom(self, _type: str, text: str, level=100):
        if not isinstance(_type, str):
            raise TypeError(f'_type must be str, not {_type.__class__.__name__}')
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {text.__class__.__name__}')
        entry = self.__format
        dt = datetime.now()
        while '%type%' in entry:
            entry = entry.replace('%type%', _type)
        while '%text%' in entry:
            entry = entry.replace('%text%', text)
        while '%date%' in entry:
            entry = entry.replace('%date%', dt.strftime('%d.%m.%Y'))
        while '%time12%' in entry:
            entry = entry.replace('%time12%', dt.strftime('%I:%M%p'))
        while '%time24%' in entry:
            entry = entry.replace('%time24%', dt.strftime('%H:%M'))
        for listener in self.__listeners:
            if level >= listener[1]:
                if callable(listener[0]):
                    listener[0](entry)
                else:
                    with open(listener[0], 'a') as f:
                        f.write(entry + '\n')
        return entry

    def debug(self, text: str):
        return self.custom('DEBUG', text, level=DEBUG)

    def info(self, text: str):
        return self.custom('INFO', text, level=INFO)

    def warn(self, text: str):
        return self.custom('WARN', text, level=WARN)

    def error(self, text: str):
        return self.custom('ERROR', text, level=ERROR)

    def fatal(self, text: str):
        return self.custom('FATAL', text, level=FATAL)
