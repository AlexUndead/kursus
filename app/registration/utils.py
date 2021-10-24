from re import search

from .exceptions import ChangeToCyrillicUtilsExcept


def is_cyrillic(symbol:str = '') -> bool:
    return bool(search('[А-Яа-я]', symbol))


def change_to_cyrillic(number:str = '') -> str:
    result = ''
    cyrillic_sumbols = { #change name value
        'A': 'А',
        'B': 'В',
        'E': 'Е',
        'K': 'К',
        'M': 'М',
        'H': 'Н',
        'O': 'О',
        'P': 'Р',
        'C': 'С',
        'T': 'Т',
        'Y': 'У',
        'X': 'Х',
        '*': '*',
    }
    for symbol in number.upper():
        if not symbol.isnumeric() and not is_cyrillic(symbol):
            try:
                result += cyrillic_sumbols[symbol]
            except KeyError:
                ChangeToCyrillicUtilsExcept('Передан недопустимый символ')
        else:
            result += symbol

    return result
