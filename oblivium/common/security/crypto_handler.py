#!/usr/bin/env python3.6

from Crypto.PublicKey import RSA
from oblivium.common.security import constants
from oblivium.common.security.random_handler import RandomHandler


class CryptoHandler:

    @staticmethod
    def from_bytes_to_int(byte):
        return int.from_bytes(byte, byteorder=constants.BYTE_ORDER)

    @staticmethod
    def from_int_to_bytes(integer):
        return integer.to_bytes(10, byteorder=constants.BYTE_ORDER)

    @staticmethod
    def from_bytes_to_string(byte):
        return byte.decode(constants.DEFAULT_ENCODING)

    @staticmethod
    def from_string_to_bytes(string):
        return string.encode(constants.DEFAULT_ENCODING)

    @staticmethod
    def from_int_to_string(integer):
        return str(integer)

    @staticmethod
    def from_string_to_int(string):
        return int(string)

    @staticmethod
    def generate_rsa_key_pair():
        return RSA.generate(
                constants.RSA_KEY_SIZE,                # key size
                RandomHandler.get_random_generator(),  # random number generation function
                constants.RSA_PUBLIC_EXPONENT          # public RSA exponent
        )

    @staticmethod
    def encrypt_with_key(key, data):  # TODO proper testing
        return key.encrypt(data)

    @staticmethod
    def decrypt_with_key(key, data):  # TODO proper testing
        return key.decrypt(data)

    @staticmethod
    def import_key(key):
        return RSA.importKey(key)

    @staticmethod
    def calculate_v(k, pub_key, xb):
        k_int = CryptoHandler.from_bytes_to_int(k)
        xb_int = CryptoHandler.from_bytes_to_int(xb)
        v = (xb_int + (k_int ^ pub_key.e)) % pub_key.n
        v_str = CryptoHandler.from_int_to_string(v)
        v_byte = CryptoHandler.from_string_to_bytes(v_str)
        return v_byte

    @staticmethod
    def encrypt_m(v, pub_key, priv_key, x, m):
        v_str = CryptoHandler.from_bytes_to_string(v)
        v_int = CryptoHandler.from_string_to_int(v_str)
        x_int = CryptoHandler.from_bytes_to_int(x)
        k = pow(v_int - x_int, priv_key.d, pub_key.n)
        m_byte = CryptoHandler.from_string_to_bytes(m)
        m_int = CryptoHandler.from_bytes_to_int(m_byte)
        ml = m_int + k
        ml_str = CryptoHandler.from_int_to_string(ml)
        ml_byte = CryptoHandler.from_string_to_bytes(ml_str)
        return ml_byte

    @staticmethod
    def decrypt_m(m, k):
        m_str = CryptoHandler.from_bytes_to_string(m)
        m_int = CryptoHandler.from_string_to_int(m_str)
        k_int = CryptoHandler.from_bytes_to_int(k)
        mb_int = m_int - k_int
        return mb_int
