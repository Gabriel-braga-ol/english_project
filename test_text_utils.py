from text_utils import normalize_word
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

