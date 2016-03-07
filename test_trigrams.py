"""This module tests functions from trigrams.py."""

import pytest

SHERLOCK_SMALL_FILENAME = 'sherlock_small.txt'

SHERLOCK_SMALL_TEXT = (
    'One night--it was on the twentieth of March, 1888--I was\n'
    'returning from a journey to a patient (for I had now returned to\n'
    'civil practice), when my way led me through Baker Street. As I\n'
    'passed the well-remembered door, which must always be associated\n'
    'in my mind with my wooing, and with the dark incidents of the\n'
    'Study in Scarlet, I was seized with a keen desire to see Holmes\n'
    'again, and to know how he was employing his extraordinary powers.\n'
    'His rooms were brilliantly lit, and, even as I looked up, I saw\n'
    'his tall, spare figure pass twice in a dark silhouette against\n'
    'the blind. He was pacing the room swiftly, eagerly, with his head\n'
    'sunk upon his chest and his hands clasped behind him. To me, who\n'
    'knew his every mood and habit, his attitude and manner told their\n'
    'own story. He was at work again. He had risen out of his\n'
    'drug-created dreams and was hot upon the scent of some new\n'
    'problem. I rang the bell and was shown up to the chamber which\n'
    'had formerly been in part my own.\n'
)


TEXT = [('simple_text.txt',
         ('This is a line of text\n'
          'This is a second text line\n'
          'Here is a third text line.\n')),
        (SHERLOCK_SMALL_FILENAME, SHERLOCK_SMALL_TEXT)
        ]

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
