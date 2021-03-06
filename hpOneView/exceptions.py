# -*- coding: utf-8 -*-

"""
exceptions.py
~~~~~~~~~~~~

This module implements exceptions HP OneView REST API
"""

__title__ = 'exceptions'
__version__ = "0.0.1"
__copyright__ = "(C) Copyright 2012-2013 Hewlett-Packard Development " \
                " Company, L.P."
__license__ = "MIT"
__status__ = "Development"

###
# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###


class HPOneViewException(Exception):
    def __init__(self, value):
        if type(value) is dict:
            self.details = value['details']
            self.errorCode = value['errorCode']
        else:
            raise Exception(value)


class HPOneViewInvalidResource(HPOneViewException):
    pass


class HPOneViewTimeout(HPOneViewException):
    pass
