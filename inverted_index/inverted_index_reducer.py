#!/usr/bin/env python3

import sys

def inverted_index_reducer():

    word_index_dict = {}

    for line in sys.stdin:

        if line.strip() == "":
            continue

        word_index_list = line.strip().split("\t")

        word_key = word_index_list[0]
        file_id = word_index_list[1]

        word_index_dict.setdefault(word_key, set())
        word_index_dict[word_key].add(file_id)

    for key in word_index_dict:
        all_files_id = '\t'.join((word_index_dict[key]))
        word_all_files = '\t'.join((key, all_files_id))
        print(word_all_files)

if __name__ == '__main__':
    inverted_index_reducer()