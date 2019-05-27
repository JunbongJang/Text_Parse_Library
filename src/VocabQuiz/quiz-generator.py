"""
Author: Junbong Jang
Date: 5/22/2019

This is created to help myself learn more vocabs for GRE test.
This will present me one word at a time until the end and test myself whether I know the word or not.
"""

import re
import random

with open("gre_vocab_list.txt", encoding='utf8') as file:  # Use file to refer to the file object
    one_vocab_per_line = file.read().replace(",", "\n", 1000)
    raw_vocab_list = one_vocab_per_line.split('\n')
    trimmed_vocab_list = list(map(lambda vocab: vocab.strip(), raw_vocab_list))
    vocab_list = list(filter(lambda vocab: vocab != '', trimmed_vocab_list))   # remove empty string
    vocab_list = list(filter(lambda vocab: re.search("^[0-9]+/[0-9]", vocab) is None, vocab_list))  # remove dates
    random.shuffle(vocab_list)
    for vocab in vocab_list:
        print()
        print(vocab)