#!/usr/bin/env python3.6

# Encodings
BYTE_ORDER = "big"
DEFAULT_ENCODING = "utf-8"

# RSA Protocol Specs
RSA_KEY_SIZE = 1024              # Key size
RSA_PUBLIC_EXPONENT = 65537      # Public exponent (e)

# Random message generation Specs
NUMBER_OF_RANDOM_BYTES = 128     # Number of random bytes generated for (xi) random messages
MAX_GENERATION_LIMIT = 2 ** 200  # Limit value to be used for number generation
