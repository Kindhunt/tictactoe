import os
import yaml
from db import Database

LANGS_PATH = r'./tictactoe/TicTacToe/language/'

class Language:
    def __init__(self) -> None:
        self.languages: dict = {}
        self.update_languages()

    def get_string(self, string: str):
        lang = self.get_language()
        try:
            if lang in self.get_languages():
                return self.languages[lang][string]
            else:
                raise NotAvailable
        except KeyError:
            # en.yaml should always be available
            return self.get_default_string(string)
        except NotAvailable:
            # changing the language to basic and return his
            return self.get_default_string(string)

    def get_default_string(self, string: str) -> str:
        en_string = self.languages['en'].get(string)
        if en_string is None:
            return StringNotFound(f'Error: string "{string}" not found.')
        return en_string

    # reload available langs
    def update_languages(self):
        for filename in os.listdir(LANGS_PATH):
            if filename.endswith('.yaml'):
                language_name = filename[:-5]
                self.languages[language_name] = yaml.safe_load(
                    open(LANGS_PATH + filename, encoding='utf8')
                )

    def get_language(self):
        # import lang from db and return then
        # for test return en
        return 'en'
    
    # for generate keyboard
    def get_languages(self) -> list:
        to_return = []
        for lang in self.languages:
            if (self.languages[lang]['available']):
                to_return.append(lang)
        return to_return


languages = Language()

class StringNotFound(Exception):
    """
    if ru.yaml also gives an error and there is no localization at all
    """
    def __init__(self, *args: object) -> None:
        self.return_error_str(''.join(args))

    def return_error_str(self, string):
        return string

class NotAvailable(Exception):
    """
    if the user's language is not currently available
    """

    def __init__(self, *args: object) -> None:
        # !need to change user lang to ru!
        user_lang = 'en'
        return None