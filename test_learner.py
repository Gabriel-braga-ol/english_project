from learner import Learner

def test_learner_name():
    learner = Learner(
        'John',
        ['Hello', 'World']
    )

    assert learner.name == 'John'

def test_learner_known_words():
    learner = Learner(
        'John',
        ['Hello', 'World']
    )

    assert learner.known_words == ['Hello', 'World']

def test_add_known_word():
    learner = Learner(
        'John',
        ['Hello', 'World']
    )

    learner.add_known_word('Python')

    assert learner.known_words == ['Hello', 'World', 'python']

def test_add_duplicate_known_word():
    learner = Learner(
        'John',
        ['Hello', 'Python']
    )

    learner.add_known_word('Python')

    assert learner.known_words == ['Hello', 'Python']

def test_add_known_word_ignores_case():
    learner = Learner(
        'John',
        ['Python']
    )

    learner.add_known_word('python')

    assert learner.known_words == ['Python']
