#!/usr/bin/env python3.6

from Crypto.PublicKey import RSA
from oblivium.common.security import constants
from oblivium.common.security.random_handler import RandomHandler

class CryptoHandler:

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
    def amazing_function(k, key, xb):
        pub_key = CryptoHandler.import_key(key)
        k_int = int.from_bytes(k, byteorder='big')
        xb_int = int.from_bytes(xb, byteorder='big')
        v = (k_int ^ pub_key.e + xb_int) % pub_key.n
        v_str = str(v)
        v_byte = v_str.encode('utf-8')
        return v_byte

    @staticmethod
    def amazing_function_1(v, publickey, privatekey, x, m):
        v_str = v.decode('utf-8')
        v_int = int(v_str)
        x_int = int.from_bytes(x, byteorder='big')
        k = (v_int - x_int) ^ privatekey.d % publickey.n
        m_byte = m.encode('utf-8')
        m_int = int.from_bytes(m_byte, byteorder='big')
        ml = m_int + k
        ml_str = str(ml)
        ml_byte = ml_str.encode('utf-8')
        return ml_byte

    @staticmethod
    def amazing_function_2(m, k):
        m_str = m.decode("utf-8")
        m_int = int(m_str)
        k_int = int.from_bytes(k, byteorder='big')
        mb_int = m_int - k_int
        return mb_int



