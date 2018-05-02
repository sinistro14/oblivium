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
        t = k_int ^ pub_key.e
        xb_int = int.from_bytes(xb, byteorder='big')
        v = (t + xb_int) % pub_key.n
        return v.to_bytes(len(str(v)), 'big')

