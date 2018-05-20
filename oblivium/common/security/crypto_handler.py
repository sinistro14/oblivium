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
    def calculate_v(x_b, n, e, k):
        """
        Calculate value v, v = (x_b + k^e) mod N

        :param x_b: random value, correspondent to chosen b
        :param k: random value
        :param n: modulus value, public_key.n
        :param e: public exponent e, public_key.e
        :return: value v
        """
        v = (x_b + pow(k, e)) % n
        return v

    @staticmethod
    def encrypt_m(v, n, d, x, m):
        """
        Encrypt available message m,
        k_n = (v - x_n)^d mod N
        m'n = m_n + (k_n)

        :param v: blinded value v, v = (x_b + k^e) mod N
        :param n: modulus value, public_key.n
        :param d: private exponent d, secret_key.d
        :param x: random generated value
        :param m: original message
        :return: encrypted message m
        """
        k = pow(v - x, d, n)
        ml = m + k
        return ml

    @staticmethod
    def decrypt_m(m, k):
        """
        Decrypt message m'b,
        m_b = m'b - k

        :param m: encrypted message m'b, m'n = m_n + (k_n)
        :param k: random value
        :return: decrypted message m_b
        """
        return m - k
