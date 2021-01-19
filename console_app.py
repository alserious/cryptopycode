from cryptopycode.cryptopycode import CryptoModule
import argparse
import sys
import os


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name')
    parser.add_argument('-p', '--path')

    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    print(namespace)

    print("Hi, {}!".format(namespace.path))


main()
