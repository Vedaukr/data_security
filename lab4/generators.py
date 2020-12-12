import random
import string

class Generator:
    def __init__(self, path=None):
        if path:
            self.data = self._load_data_from_file(path)
    
    def _load_data_from_file(self, path):
        passwords = list()
        with open(path) as file:
            for line in file:
                passwords.append(line.strip())
        return passwords

    def generate(self):
        pass

class TopPasswordsGenerator(Generator):
    def generate(self):
        return random.choice(self.data)

class HumanLikeGenerator(Generator):
    WORD_RULES = {
        'i': '1',
        'e': '3',
        'for': '4',
        'a': '@',
        'b': '8',
        's': '5',
        'm': '^^',
        'o': '0' 
    }
    def generate(self):
        first_word = self._replace_letters(random.choice(self.data))
        second_word = self._replace_letters(random.choice(self.data))
        return first_word + " " + second_word
    
    def _replace_letters(self, password):
        for key in self.WORD_RULES.keys():
            password = password.replace(key, self.WORD_RULES[key])
        return password

class RandomPasswordGenerator(Generator):
    SPECIAL_SYMBOLS = "!@#$%^&*()[] "
    MIN_LEN = 8
    MAX_LEN = 24

    def generate(self):
        length = random.randint(self.MIN_LEN, self.MAX_LEN)
        possible_symbols = self.SPECIAL_SYMBOLS + string.ascii_letters + string.digits
        return ''.join(random.choices(possible_symbols, k=length))
    