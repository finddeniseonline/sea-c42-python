#!/usr/bin/env python

"""
code that tests the break_me.py functions
"""

import pytest  # used for the exception testing


import break_me


def test_name_error():
    try:
        break_me.exhibit_name_error()
    except NameError:
        assert(True)
    finally:
        assert(False)

def test_attribute_error():
    try:
        break_me.exhibit_attribute_error:
    except ValueError:
        assert(True)
    finally:
        assert(False)

def test_type_error():
    try:
        break_me.exhibit_type_error:
    except TypeError:
        assert(True):
    finally:
        assert(False)