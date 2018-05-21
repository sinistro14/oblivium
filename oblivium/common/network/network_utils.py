#!/usr/bin/env python3.6

import base64
import pickle


def object_to_base64(obj):
    return base64.b64encode(pickle.dumps(obj))


def base64_to_object(byte):
    return pickle.loads(base64.b64decode(byte))
