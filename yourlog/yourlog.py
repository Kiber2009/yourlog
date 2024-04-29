from datetime import datetime
from types import FunctionType


class Logger:
    def __init__(self, _format='%date% %time24% [%type%]: %text%'):
        if not isinstance(_format, str):
            raise TypeError(f'_format must be str, not {str(type(_format))[8:-2]}')
        self.__listeners = []
        self.__format = _format

    def add_listener(self, listener: str | FunctionType):
        if not (isinstance(listener, str) or callable(listener)):
            raise TypeError(f'listener must be str | function, not {str(type(listener))[8:-2]}')
        self.__listeners.append(listener)

    def custom(self, _type: str, text: str):
        if not isinstance(_type, str):
            raise TypeError(f'Type must be str, not {str(type(_type))[8:-2]}')
        if not isinstance(text, str):
            raise TypeError(f'Text must be str, not {str(type(text))[8:-2]}')
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
            if callable(listener):
                listener(entry)
            else:
                with open(listener, 'a') as f:
                    f.write(entry + '\n')

    def debug(self, text: str):
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('DEBUG', text)

    def info(self, text: str):
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('INFO', text)

    def warn(self, text: str):
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('WARN', text)

    def error(self, text: str):
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('ERROR', text)

    def fatal(self, text: str):
        if not isinstance(text, str):
            raise TypeError(f'text must be str, not {str(type(text))[8:-2]}')
        self.custom('FATAL', text)
