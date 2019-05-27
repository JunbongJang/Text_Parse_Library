"""
Author: Junbong Jang
Date: 10/7/2018

This is for the project 6 - Bayesian Networks
Current file constructs the bayesian network based on user input and performs sampling.
Option B is taken, so each node can have more than 2 parents.
"""
from random import random  # random number generator
import numpy as np  # for calculating variance and mean
import re

text_file_name = './assets/vocab-training-text.txt'
def parse_text_file():
    unknown_character = ' '
    with open(text_file_name, 'r', encoding='UTF-8') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    data = [(random(), line) for line in content]

    data.sort()
    with open('parsed-words.txt', 'w', encoding='UTF-8') as target:
        for _, line in data:
            target.write(line + '\n')


if __name__ == "__main__":
    parse_text_file()