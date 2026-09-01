from content import Content
from learner import Learner
import pytest

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

@pytest.mark.parametrize(
        'known_count, expected_difficulty',
        [
            (9, 'Easy'),
            (8, 'Ideal'),
            (6, 'Challenging'),
            (4, 'Hard')
        ]
)


def test_difficulty(known_count, expected_difficulty):
    known_words = [
        'i',
        'really',
        'like',
        'python',
        'now',
        'until',
        'last',
        'week',
        'we',
        'hated'
    ]

    content = Content(
        'Teste',
        'I really like python now, until last week we hated'
    )

    assert content.get_difficulty(known_words[:known_count]) == expected_difficulty

def test_comprehensibility_score_with_learner():
    content = Content(
        'Teste',
        'I really like Python'
    )

    learner = Learner(
        'John',
        ['i', 'python']
    )

    assert content.get_comprehensibility_score(learner.known_words) == 50

def test_get_unknown_words():
    known_words = [
        'i',
        'really',
        'python'
    ]

    content = Content(
        'Teste',
        'I really like learning Python'
    )

    assert content.get_unknown_words(known_words) == ["like", "learning"]

def test_get_known_words():
    known_words = [
        'i',
        'really',
        'python'
    ]

    content = Content(
        'Teste',
        'I really like learning Python'
    )

    assert content.get_known_words(known_words) == ["i", "really", "python"]

def test_comprehensibility_score_increases_after_learning_word():
    content = Content(
        'Teste',
        'I really like learning Python'
    )

    learner = Learner(
        'John',
        ["i", "really", "python"]
    )

    assert content.get_comprehensibility_score(learner.known_words) == 60

    learner.add_known_word('learning')

    assert content.get_comprehensibility_score(learner.known_words) == 80

def test_content_has_topic():
    content = Content(
        "Roman Empire",
        "The Roman Empire was one of the largest empires in history.",
        "história"
    )

    assert content.get_topic() == "história"

def test_content_matches_learner_interest():
    content = Content(
        "Roman Empire",
        "The Roman Empire was one of the largest empires in history.",
        "história"
    )

    interests = ["história", "tecnologia"]

    assert content.matches_interests(interests) is True

def test_content_not_matches_learner_interest():
    content = Content(
        "Roman Empire",
        "The Roman Empire was one of the largest empires in history.",
        "história"
    )

    interests = ["ciência", "tecnologia"]

    assert content.matches_interests(interests) is False

def test_content_without_topic_does_not_match_interests():
    content = Content(
        "Roman Empire",
        "The Roman Empire was one of the largest empires in history.",
    )

    interests = ["ciência", "tecnologia"]

    assert content.matches_interests(interests) is False