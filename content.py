from datetime import date

class Content:
    
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.created_date = date.today()

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def get_date(self):
        return self.created_date

    def get_word_count(self):
        sentence = self.text.split()
        return len(sentence)

    def get_known_word_count(self, known_words):
        words = self.text.split()
        count = 0
        for word in words:
            lowercase_word = word.lower().strip('.,!?')
            if lowercase_word in known_words:
                count += 1
        
        return count

    def get_comprehensibility_score(self, known_words):
        known_word_count = self.get_known_word_count(known_words)
        total_words = self.get_word_count()

        if total_words == 0:
            return 0
        
        score = (known_word_count / total_words) * 100

        return round(score, 2)

    def get_difficulty(self, known_words):
        score = self.get_comprehensibility_score(known_words)

        if score >= 90:
            return 'Easy'
        elif score >= 80:
            return 'Ideal'
        elif score >= 60:
            return 'Challenging'
        else:
            return 'Hard'

    def get_unknown_word_count(self, known_words):
        total_words = self.get_word_count()
        known_word_count = self.get_known_word_count(known_words)

        unknown_words = total_words - known_word_count

        return unknown_words
        
