import pytest


TEXT = [('trigrams.txt',
    'This is a line of text\n'
    'Here is a second line of text\n'
    'And a third line of text.')
]

@pytest.mark.parametrize('file_in, out', TEXT)
def test_input(file_in, out):
    from trigrams import trigams_input
    assert trigrams_input(file_in) == out

