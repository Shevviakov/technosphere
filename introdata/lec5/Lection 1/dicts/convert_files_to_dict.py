# -*- coding: utf-8 -*-

import sys
import unicodedata
import argparse
import pickle
from collections import defaultdict

TRANSLATE_PUNCTUATION = dict.fromkeys(i for i in xrange(sys.maxunicode) if not unicodedata.category(unichr(i)).startswith('L'))
TRANSLATE_OTHER = dict.fromkeys((36, 43, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 60, 61, 62, 124, 126, 94, 96))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Input files, comma-separated")
    args = parser.parse_args()
    files = args.input.split(',')

    vocab = defaultdict(int)

    for filename in files:
        with open(filename, 'rb') as f:
            for line in f:
                try:
                    words = line.decode('cp1251').split(u' ')
                except UnicodeDecodeError:
                    words = line.decode('utf-8').split(u' ')
                for word in words:
                    word_parsed = word.translate(TRANSLATE_PUNCTUATION).translate(TRANSLATE_OTHER).lower().strip()
                    if word_parsed:
                        try:
                            word_parsed.encode('ascii')
                        except ValueError:
                            vocab[word_parsed] += 1

    pickle.dump(dict(vocab), open('dictionary.p', 'wb+'))