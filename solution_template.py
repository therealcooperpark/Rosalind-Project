#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def main():
    args = get_args()


if __name__ == '__main__':
    main()
