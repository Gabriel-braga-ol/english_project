from content import Content


def test_word_count_with_four_words():
    content = Content(
        'Teste',
        'I really like Python'
    )

    assert content.get_word_count() == 4

def test_word_count_with_empty_text():
    content = Content(
        'Teste',
        ''
    )

    assert content.get_word_count() == 0

def test_unknown_word_count():
    known_words = [
        'i',
        'python'
    ]

    content = Content(
        'Teste',
        'I really like Python'
    )

    assert content.get_unknown_word_count(known_words)

def test_known_word_count():
    known_words = [
        'i',
        'python'
    ]

    content = Content(
        'Teste',
        'I really like Python'
    )

    assert content.get_known_word_count(known_words) == 2

def test_comprehensibility_score():
    known_words = [
        'i',
        'python'
    ]

    content = Content(
        'Teste',
        'I really like Python'
    )

    assert content.get_comprehensibility_score(known_words) == 50

def test_get_difficulty():
    known_words = [
        'i',
        'python',
        'now',
        'like',
    ]

    content = Content(
        'Teste',
        'I really like Python now'
    )

    assert content.get_difficulty(known_words) == 'Ideal'