def normalize_word(word):
    normalize_word = word.lower().strip(".,!?()\"'")
    return normalize_word

def extract_words(text):
    sentence = text.split()
    words = []
    for word in sentence:
        normalized_word = normalize_word(word)
        if not normalized_word.isdigit():
            words.append(normalized_word)

    return words