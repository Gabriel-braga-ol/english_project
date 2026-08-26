from text_utils import normalize_word

class Learner:
    def __init__(self, name, known_words):
        self.name = name
        self.known_words = []

        for known_word in known_words:
            self.add_known_word(known_word)

    def add_known_word(self, word):
        normalized_word = normalize_word(word)

        if normalized_word not in self.known_words:
            self.known_words.append(normalized_word)