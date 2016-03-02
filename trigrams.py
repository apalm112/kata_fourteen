"""Docstring here."""


import io


def trigrams_input(input_file):
    """Function to input and read file."""
    sherlock = io.open(input_file)
    return sherlock.read()

def trigram(sherlock_string):
    sherlock_list = sherlock_string.split()
    # first_trigram_key = ' '.join(sherlock_list[:2])
    # first_trigram_val = sherlock_list[2]
    # trigram_dict = {first_trigram_key: first_trigram_val}
    trigram_dict = {}

    for index, current_word in enumerate(sherlock_list[:-1]):
        if index == 0:
            continue
        previous_word = sherlock_list[index -1]
        trigram_key = ' '.join([previous_word, current_word])
        word_list = trigram_dict.setdefault(trigram_key, [])
        next_word = sherlock_list[index + 1]
       # trigram_dict[' '.join([previous_word, current_word])] = [next_word]  # this does the same as line 23.
        word_list.append(next_word)

    return trigram_dict
