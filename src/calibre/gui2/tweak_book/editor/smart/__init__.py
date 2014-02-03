#!/usr/bin/env python
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2014, Kovid Goyal <kovid at kovidgoyal.net>'

class NullSmarts(object):

    def __init__(self, editor):
        pass

    def get_extra_selections(self, editor):
        return ()

