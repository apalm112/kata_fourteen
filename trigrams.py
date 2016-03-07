"""Generate new text from given text using a trigram algorithm."""


import io
import sys
import random


def main(text_file, length):
    """Return new text from given text file and length parameter."""
    text = trigrams_input(text_file)
    trigram_dict = make_trigrams(text)
    new_text = make_new_text(trigram_dict, length)
    return new_text


def trigrams_input(file_path):
    """Function to input and read file."""
    text_file = io.open(file_path)
    text = text_file.read()
    text_file.close()
    return text


def make_trigrams(text):
    """Return dictionary of trigrams from given long string."""
    words = text.split()
    trigram_dict = {}

    for index, word in enumerate(words):
        if index < 2:
            continue
        trigram_key = ' '.join(words[index - 2:index])
        word_list = trigram_dict.setdefault(trigram_key, [])
        word_list.append(word)

    return trigram_dict


def make_new_text(trigram_dict, length):
    """Return a long string of new text assembled by trigrams."""
    key = random.choice(list(trigram_dict.keys()))
    output_words = key.split(' ')

    while len(output_words) < length:
        last_two = ' '.join(output_words[-2:])
        if last_two not in trigram_dict:
            last_two = random.choice(list(trigram_dict.keys()))
        new_word = random.choice(trigram_dict[last_two])
        output_words.append(new_word)

    return ' '.join(output_words)


if __name__ == '__main__':
    try:
        text_file = sys.argv[1]
        length = int(sys.argv[2])
        if length < 3:
            raise ValueError('Output length must be at least 3.')
        else:
            new_text = main(text_file, length)
            print(new_text)

    except IndexError:
        print('Too few arguments given. Correct usage:\n'
              '> python trigrams.py <filename> <length>')
