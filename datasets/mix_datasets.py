#!/usr/bin/python
from __future__ import print_function, unicode_literals

import os
import shutil
from random import sample
from sys import argv


def main(perc_left, left, right, out):
    left_files = os.listdir(left)
    right_files = os.listdir(right)
    max_len = min(len(left_files), len(right_files))
    left_files = left_files[:max_len]
    right_files = right_files[:max_len]


    left_sampled = map(lambda x: os.path.join(left, x), sample(left_files, int(perc_left * max_len)))
    right_sampled = map(lambda x: os.path.join(right, x), sample(right_files, int((1 - perc_left) * max_len)))

    os.makedirs(out)
    files_in = left_sampled + right_sampled
    for f in files_in:
        shutil.copy2(f, out)


if __name__ == '__main__':
    if len(argv) != 5:
        print('Usage: python mix_datasets.py <left %> <left_dir> <right_dir> <output_dir>')
        exit(-1)

    main(float(argv[1]), argv[2], argv[3], argv[4])
