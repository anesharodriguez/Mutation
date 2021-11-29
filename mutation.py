#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-11-22
Purpose: Project
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Show mutation genes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number_line = 1
    line = []
    for fh in args.file:
        line.append(fh.rstrip())
        number_line += -1
    print(f'{line[0]} has {abs(number_line)} mutated genes: {line[1:]}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
