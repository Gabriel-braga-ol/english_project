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

    assert learner.known_words == ['hello', 'world']

def test_add_known_word():
    learner = Learner(
        'John',
        ['Hello', 'World']
    )

    learner.add_known_word('Python')

    assert learner.known_words == ['hello', 'world', 'python']

def test_add_duplicate_known_word():
    learner = Learner(
        'John',
        ['Hello', 'Python']
    )

    learner.add_known_word('Python')

    assert learner.known_words == ['hello', 'python']

def test_add_known_word_ignores_case():
    learner = Learner(
        'John',
        ['Python']
    )

    learner.add_known_word('python')

    assert learner.known_words == ['python']

def test_known_words_are_normalized_on_creation():
    learner = Learner(
        'John',
        ['Python', 'HELLO!', 'World']
    )

    assert learner.known_words == ["python", "hello", "world"]

def test_known_words_do_not_have_duplicates_on_creation():
    learner = Learner(
        'John',
        ['Python', 'Hello', 'python']
    )

    assert learner.known_words == ["python", "hello"]

def test_remove_known_word():
    learner = Learner(
        'John',
        ["i", "really", "python"]
    )

    learner.remove_known_word('python')

    assert learner.known_words == ["i", "really"]

def test_remove_known_word_ignores_case_and_punctuation():
    learner = Learner(
        'John',
        ["i", "python"]
    )

    learner.remove_known_word('PYTHON!')

    assert learner.known_words == ['i']

def test_learner_level():
    learner = Learner(
        'John',
        ["hello", "world"]
    )

    assert learner.level == 'Beginner'