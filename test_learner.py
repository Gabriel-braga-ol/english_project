from learner import Learner
import pytest

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

    assert learner.level == 'Iniciante'

def test_set_level():
    learner = Learner(
        'John',
        ["hello", "world"]
    )

    learner.set_level('Intermediário')

    assert learner.level == 'Intermediário'

def test_set_invalid_level_raises_error():
    learner = Learner(
        'John',
        ["hello", "world"]
    )

    with pytest.raises(ValueError):
        learner.set_level('Batata')

def test_create_learner_with_invalid_level_raises_error():
    with pytest.raises(ValueError):
        learner = Learner(
            'John',
            ["hello", "world"],
            'Batata'
        )

def test_get_known_word_count():
    learner = Learner(
        "John",
        ["hello", "world"]
    )

    assert learner.get_known_word_count() == 2

def test_knows_word_returns_true_for_known_word():
    learner = Learner(
        "John",
        ["hello", "python"]
    )

    assert learner.knows_word("python") is True

def test_knows_word_ignores_case_and_punctuation():
    learner = Learner(
        "John",
        ["python"]
    )

    assert learner.knows_word("PYTHON!") is True

def test_add_multiple_known_words():
    learner = Learner(
        "John",
        ["hello"]
    )

    learner.add_known_words(["python", "world"])

    assert learner.known_words == ["hello", "python", "world"]

def test_add_multiple_known_words_normalizes_and_avoids_duplicates():
    learner = Learner(
        "John",
        ["python"]
    )

    learner.add_known_words(["PYTHON!", "World"])

    assert learner.known_words == ["python", "world"]

def test_remove_multiple_known_words():
    learner = Learner(
        "John",
        ["From", "Started", "World"]
    )

    learner.remove_known_words(["from", "world"])

    assert learner.known_words == ["started"]