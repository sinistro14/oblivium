#!/usr/bin/env python3.6

from Crypto.PublicKey import RSA
from oblivium.common.security import constants
from oblivium.common.security.random_handler import RandomHandler


class CryptoHandler:

    @staticmethod
    def generate_rsa_key_pair():
        return RSA.generate(
                constants.RSA_KEY_SIZE,                      # key size
                RandomHandler.get_random_bytes_generator(),  # random number generation function
                constants.RSA_PUBLIC_EXPONENT                # public RSA exponent
        )

    @staticmethod
    def import_key(key):
        return RSA.importKey(key)

    @staticmethod
    def calculate_v(k, pub_key, xb): #encrypt the random k and blind it with x_b
        v = (xb + pow(k, pub_key.e)) % pub_key.n
        return v

    @staticmethod
    def encrypt_m(v, pub_key, priv_key, x, m): #get a value for k and add it to the original message
        k = pow(v - x, priv_key.d, pub_key.n)
        ml = m + k
        return ml

    @staticmethod
    def decrypt_m(m, k): #unblind the the right message with k
        mb_int = m - k
        return mb_int
