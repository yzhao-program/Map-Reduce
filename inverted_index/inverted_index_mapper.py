#!/usr/bin/env python3

import sys
import os
import re

def inverted_index_mapper():

    for line in sys.stdin:

        file_path = os.environ["mapreduce_map_input_file"]

        file_id = re.findall(r'\w{1,}', file_path)[-2]

        if line.strip() == "":
            continue

        word_line = re.sub(r'([\W]|_){1,}', ' ', line)

        words = word_line.strip().split()

        for word in words:
            word_index = '\t'.join((word.lower(), file_id))
            print(word_index)

if __name__ == '__main__':
    inverted_index_mapper()