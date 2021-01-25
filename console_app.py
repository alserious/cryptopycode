# Python 3.8
from cryptopycode.cryptopycode import CryptoModule
import argparse
import sys
import os


def create_parser():
    parser = argparse.ArgumentParser(description='Script for encryption and decryption python file')
    parser.add_argument('name', '-n', '--name ', help='file name', default='secret.py', type=str)
    parser.add_argument('path', '-p', '--path', help='path to file',
                        default=os.path.join(os.path.abspath(os.path.dirname(__name__)), ""), type=str)
    parser.add_argument('key', '-k', '--key', help='encrypt or decrypt', choices=[""])
    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    module = CryptoModule()
    print(namespace)

    if namespace.key == 'encrypt':
        path_opened = os.path.join(namespace.path, namespace.name)
        path_secured = os.path.join(namespace.path, "secured_" + namespace.name)
        module.create_secured_module(path_to_opened_module=path_opened, path_to_secured_module=path_secured)

    elif namespace.key == 'decrypt':
        path_secured = os.path.join(namespace.path, namespace.name)
        path_opened = os.path.join(namespace.path, "opened_" + namespace.name)
        module.create_opened_module(path_to_secured_module=path_secured, path_to_opened_module=path_opened)


main()
