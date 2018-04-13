#!/usr/bin/env python3.6

import base64
import pickle

from oblivium.common.network import constants


#  TODO not in use, delete later
def string_to_base64(string):
    return base64.b64encode(string.encode(constants.DEFAULT_ENCODING))


#  TODO not in use, delete later
def base64_to_string(byte):
    return base64.b64decode(byte).decode(constants.DEFAULT_ENCODING)


def object_to_base64(obj):
    return base64.b64encode(pickle.dumps(obj))


def base64_to_object(byte):
    return pickle.loads(base64.b64decode(byte))
