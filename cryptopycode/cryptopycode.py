from cryptography.fernet import Fernet
import json
import ast
import os


class CryptoModule(object):
    """
    Class for encrypt and decrypt the python module with confidential information
    """

    def __init__(self, debug: bool = False, log: bool = False) -> None:
        """
        Init
        :param debug: enable debug
        :param log: enable log
        :return: none
        """
        self.path_to_crypto = os.path.join(os.path.abspath(os.path.dirname(__name__)), "")
        self.debug = debug
        self.log = log

    def _write_key(self) -> None:
        """
        Create the key and save it to the file 'crypto.key'
        :return: none
        """
        key = Fernet.generate_key()
        with open(self.path_to_crypto + 'crypto.key', 'wb') as key_file:
            key_file.write(key)

    def _load_key(self) -> bytes:
        """
        Load the key from the file 'crypto.key'
        :return: bytes
        """
        return open(self.path_to_crypto + 'crypto.key', 'rb').read()

    def _encrypt(self, decrypted_data: bytes, key: bytes) -> bytes:
        """
        Encrypt data
        :param decrypted_data: Input decrypted data
        :param key: Input key
        :return: bytes
        """
        f = Fernet(key)
        return f.encrypt(decrypted_data)

    def _decrypt(self, encrypted_data: bytes, key: bytes) -> bytes:
        """
        Decrypt data
        :param encrypted_data: Input encrypted data
        :param key: Input key
        :return: bytes
        """
        f = Fernet(key)
        return f.decrypt(encrypted_data)

    def return_secured_module(self, path_to_secured_module: str) -> dict:
        """
        Return the decrypted python secured module
        :param path_to_secured_module: Path to source secured python module
        :return: dict
        """
        # Load the key
        key = self._load_key()

        # Read the file
        file = open(path_to_secured_module, 'rb')
        encrypted_data = file.read()

        # Ger split string
        split_str = self._load_key()[-4:]

        # Get data
        all_data = encrypted_data.split(split_str)

        # Decryption process
        out_dict = {}

        for data in all_data[0:-1]:
            decrypted_data = self._decrypt(data, key)

            tree = ast.parse(decrypted_data)
            for node in tree.body:
                out_dict.update({node.targets[0].id: ast.literal_eval(node.value)})

        return out_dict

    def create_secured_module(self, path_to_opened_module: str, path_to_secured_module: str, create_key: bool = True,
                              delete_source_opened_module: bool = False) -> None:
        """
        Create the encrypted python secured module
        :param path_to_opened_module: Path to source opened python module
        :param path_to_secured_module: Path to out secured python module
        :param create_key: Create the key or not
        :param delete_source_opened_module: Delete source python module or not
        :return: none
        """
        # Write the key
        if create_key:
            self._write_key()

        key = self._load_key()

        file = open(path_to_opened_module, 'rb')

        tree = ast.parse(file.read())

        # Create the empty file
        __empty_file = open(path_to_secured_module, 'wb')
        __empty_file.close()

        # Take the last 4 symbols for split
        split_str = self._load_key()[-4:]

        # Encryption process
        with open(path_to_secured_module, 'ab') as file:
            for node in tree.body:
                # if dict type
                if type(ast.literal_eval(node.value)) == dict:
                    _values = json.dumps(ast.literal_eval(node.value), ensure_ascii=False, indent=2).encode('utf-8')
                # if other type
                else:
                    _values = json.dumps(ast.literal_eval(node.value), ensure_ascii=False).encode('utf-8')
                # Encrypt
                _name = bytes(node.targets[0].id, encoding='utf-8')
                _ = _name + b' = ' + _values
                encrypted_data = self._encrypt(_, key)
                file.write(encrypted_data + split_str)

        # Delete source python module
        if delete_source_opened_module:
            os.remove(path_to_opened_module)

    def create_opened_module(self, path_to_secured_module: str, path_to_opened_module: str) -> None:
        """
        Create the decrypted python opened module
        :param path_to_secured_module: Path to source secured python module
        :param path_to_opened_module: Path to out opened python module
        :return: none
        """
        # Load the key
        key = self._load_key()

        # Read the file
        file = open(path_to_secured_module, 'rb')
        encrypted_data = file.read()

        # Get split string
        split_str = self._load_key()[-4:]

        # Get data
        all_data = encrypted_data.split(split_str)

        # Decryption process
        with open(path_to_opened_module, 'wb') as file:
            for data in all_data[0:-1]:
                decrypted_data = self._decrypt(data, key)
                file.write(decrypted_data + b'\n')
