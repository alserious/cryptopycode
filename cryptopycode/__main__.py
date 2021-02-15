# Python 3.8
from .cryptopycode import CryptoModule
import argparse
import sys
import os


def create_parser():
    parser = argparse.ArgumentParser(prog='cryptopycode', usage='%(prog)s [options]',
                                     description='Script for encryption and decryption python file.')
    parser.add_argument('-n', '--name', help='file name', type=str, dest='name', default='secret.py')
    parser.add_argument('-p', '--path', help='path to file', type=str, dest='path',
                        default=os.path.join(os.path.abspath(os.path.dirname(__name__)), ""))
    parser.add_argument('-k', '--key', help='encrypt or decrypt python module', type=str, dest='key',
                        choices=['encrypt', 'decrypt'])
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    module = CryptoModule()

    if namespace.key == 'encrypt':
        path_opened = os.path.join(namespace.path, namespace.name)
        secured = "secured_" + namespace.name
        path_secured = os.path.join(namespace.path, secured)
        module.create_secured_module(path_to_opened_module=path_opened, path_to_secured_module=path_secured)
        print(f'Created file: {secured}')

    elif namespace.key == 'decrypt':
        path_secured = os.path.join(namespace.path, namespace.name)
        opened = "opened_" + namespace.name
        path_opened = os.path.join(namespace.path, opened)
        module.create_opened_module(path_to_secured_module=path_secured, path_to_opened_module=path_opened)
        print(f'Created file: {opened}')
