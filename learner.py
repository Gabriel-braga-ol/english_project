from text_utils import normalize_word

class Learner:
    def __init__(self, name, known_words):
        self.name = name
        normalized_known_words = []

        for known_word in known_words:
            normalized_known_word = normalize_word(known_word)
            normalized_known_words.append(normalized_known_word)

        self.known_words = normalized_known_words

    def add_known_word(self, word):
        normalized_known_words = []

        for known_word in self.known_words:
            normalized_known_word = normalize_word(known_word)
            normalized_known_words.append(normalized_known_word)

        normalized_word = normalize_word(word)

        if normalized_word not in normalized_known_words:
            self.known_words.append(normalized_word)