"""
Author: Junbong Jang
Date: 5/22/2019

This is created to help myself learn more vocabs for GRE test.
This will present me one word at a time until the end and test myself whether I know the word or not.
"""

import re
import random


def getVocabList():
    with open("gre_vocab_list.txt", encoding='utf8') as file:  # Use file to refer to the file object
        one_vocab_per_line = file.read().replace(",", "\n", 1000)
        raw_vocab_list = one_vocab_per_line.split('\n')
        trimmed_vocab_list = list(map(lambda vocab: vocab.strip(), raw_vocab_list))
        vocab_list = list(filter(lambda vocab: vocab != '', trimmed_vocab_list))   # remove empty string
        vocab_list = list(filter(lambda vocab: re.search("^[0-9]+/[0-9]", vocab) is None, vocab_list))  # remove dates
        random.shuffle(vocab_list)
    return vocab_list


import webbrowser
def openWebBrowser(query):
    webbrowser.open_new_tab('https://www.dictionary.com/browse/' + query)


if __name__ == "__main__":
    vocab_list = getVocabList()
    for index, vocab in enumerate(vocab_list):
        print(f'{index}: {vocab}')
        openWebBrowser(vocab)
        if index % 10 == 0 and index != 0:
            user_answer = input("Would you like to continue?\n")
            print('--------------------------------------------')
