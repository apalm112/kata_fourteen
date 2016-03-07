"""This module tests functions from trigrams.py."""

import pytest


TEXT = [('trigrams.txt',
         ('This is a line of text\n'
          'This is a second text line\n'
          'Here is a third text line.\n')
         )]

TRIGRAM = [
    ('I wish I', {'I wish': ['I']}),
    ('I wish I may I wish I might', {
        'I wish': ['I', 'I'],
        'wish I': ['may', 'might'],
        'may I': ['wish'],
        'I may': ['I']}),
    ('a a a', {'a a': ['a']}),
    ('a a', {}),
    ('a', {}),
    ('', {})
]


DUMMY_DICT = {
    'I wish': ['I', 'I'],
    'wish I': ['may', 'might'],
    'may I': ['wish'],
    'I may': ['I']
}


LENGTH = [
    (DUMMY_DICT, 200),
    (DUMMY_DICT, 100),
    (DUMMY_DICT, 50),
    (DUMMY_DICT, 20),
    (DUMMY_DICT, 3),
]


@pytest.mark.parametrize('file_in, out', TEXT)
def test_input(file_in, out):
    """Test trigrams_input function to ensure correct text output."""
    from trigrams import trigrams_input
    assert trigrams_input(file_in) == out


@pytest.mark.parametrize('trigram_key, trigram_value', TRIGRAM)
def test_trigram(trigram_key, trigram_value):
    """"Test trigram function to ensure correct dictionary output."""
    from trigrams import make_trigrams
    assert make_trigrams(trigram_key) == trigram_value


@pytest.mark.parametrize('input_dict, length', LENGTH)
def test_trigram_length(input_dict, length):
    """Test make_new_text function to ensure correct length of output."""
    from trigrams import make_new_text
    result_text = make_new_text(input_dict, length)
    result_list = result_text.split(' ')
    assert len(result_list) == length
