from text_utils import normalize_word, extract_words
import pytest

@pytest.mark.parametrize(
    "input_word, expected_word",
    [
        ("Python.", "python"),
        ("HELLO!", "hello"),
        ("Now,", "now"),
        ("Really?", "really"),
        ("(Python)", "python"),
        ('"Hello!"', "hello"),
        ("'Hello'", "hello"),
        ("don't", "don't"),
    ]
)
def test_normalize_word(input_word, expected_word):
    assert normalize_word(input_word) == expected_word

@pytest.mark.parametrize(
    "text, expected",
    [
        ("February 4, 2004", ["february"]),
        ("123 456", []),
    ]
)
def test_extract_words_ignores_numbers(text, expected):
    assert extract_words(text) == expected



