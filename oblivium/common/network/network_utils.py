#!/usr/bin/env python3.6

import base64

from oblivium.common.network import constants


def string_to_base64(string):
    return base64.b64encode(string.encode(constants.DEFAULT_ENCODING))


def base64_to_string(byte):
    return base64.b64decode(byte).decode(constants.DEFAULT_ENCODING)
