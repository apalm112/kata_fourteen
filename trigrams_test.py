import pytest


TEXT = [('trigrams.txt', 'This is a line of text\nThis is a second text line\nHere is a third text line.\n')]

TRIGRAM = [('I wish I', {'I wish': ['I']}),
                   ('I wish I may I wish I might',
                   {'I wish': ['I', 'I'],
                   'wish I': ['may', 'might'],
                   'may I': ['wish'],
                   'I may': ['I']
                   })]

@pytest.mark.parametrize('file_in, out', TEXT)
def test_input(file_in, out):
    from trigrams import trigrams_input
    assert trigrams_input(file_in) == out

@pytest.mark.parametrize('trigram_key, trigram_value', TRIGRAM)
def test_trigram(trigram_key, trigram_value):
    from trigrams import trigram
    assert trigram(trigram_key) == trigram_value

