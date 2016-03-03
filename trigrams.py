"""Docstring here."""


import io
import sys
import random


def main(text_file, length):
    """Docstring."""
    text = trigrams_input(text_file)
    trigram_dict = trigram(text)
    new_text = make_trigrams(trigram_dict, length)
    return new_text


def trigrams_input(input_file):
    """Function to input and read file."""
    sherlock = io.open(input_file)
    return sherlock.read()


def trigram(sherlock_string):
    """Docstring goes here."""
    sherlock_list = sherlock_string.split()
    # first_trigram_key = ' '.join(sherlock_list[:2])
    # first_trigram_val = sherlock_list[2]
    # trigram_dict = {first_trigram_key: first_trigram_val}
    trigram_dict = {}

    for index, current_word in enumerate(sherlock_list[:-1]):
        if index == 0:
            continue
        previous_word = sherlock_list[index - 1]
        trigram_key = ' '.join([previous_word, current_word])
        word_list = trigram_dict.setdefault(trigram_key, [])
        next_word = sherlock_list[index + 1]
        # trigram_dict[' '.join([previous_word, current_word])] = [next_word]  # this does the same as line 23.
        word_list.append(next_word)

    return trigram_dict


def make_trigrams(trigram_dict, length):
    key = random.choice(list(trigram_dict.keys()))
    output_list = key.split(' ')
    while len(output_list) < length:
        last_two = ' '.join([output_list[-2], output_list[-1]])
        if last_two not in trigram_dict:
            last_two = random.choice(list(trigram_dict.keys()))
        new_word = random.choice(trigram_dict[last_two])
        output_list.append(new_word)

    return ' '.join(output_list)


if __name__ == '__main__':
    print(sys.argv)
    text_file = sys.argv[1]
    length = int(sys.argv[2])
    new_text = main(text_file, length)
    print(new_text)
