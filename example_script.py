# Python 3.8
from cryptopycode.cryptopycode import CryptoModule
import os


def example():
    """
    Just example for use crypto lib
    :return:
    """
    path = os.path.abspath(os.path.dirname(__name__))
    module = CryptoModule()
    # create_name this is open source py module with confidential information
    opened_path = os.path.join(path, 'secret.py')
    # read_name this is open encrypted py module with confidential information
    secured_path = os.path.join(path, 'secured.py')
    # encrypt, read secret.py and create secured.py
    module.create_secured_module(path_to_opened_module=opened_path, path_to_secured_module=secured_path,
                                 create_key=True, delete_source_opened_module=False)
    # decrypt, read secured.py and create opened.py
    module.create_opened_module(path_to_secured_module=secured_path, path_to_opened_module=opened_path)
    print('ok')


example()
