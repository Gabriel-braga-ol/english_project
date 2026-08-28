from text_utils import normalize_word

class Learner:
    PERMITTED_LEVELS = ["Iniciante", "Intermediário", "Avançado"]

    def __init__(self, name, known_words, level='Iniciante'):
        self.name = name
        self.set_level(level)
        self.known_words = []

        for known_word in known_words:
            self.add_known_word(known_word)

    def add_known_word(self, word):
        normalized_word = normalize_word(word)

        if normalized_word not in self.known_words:
            self.known_words.append(normalized_word)

    def remove_known_word(self, word):
        normalized_word = normalize_word(word)

        if normalized_word in self.known_words:
            self.known_words.remove(normalized_word)

    def set_level(self, level):
        if level not in Learner.PERMITTED_LEVELS:
            raise ValueError('Nível inválido')
       
        self.level = level

    def get_known_word_count(self):
        return len(self.known_words)

    def knows_word(self, word):
        normalized_word = normalize_word(word)
        return normalized_word in self.known_words