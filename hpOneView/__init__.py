#!/usr/bin/env python3
"""
HP OneView Library
~~~~~~~~~~~~~~~~~~~~~

hpOneView is a library for interfacing with HP OneView Management Appliance.
"""

__title__ = 'hpOneView'
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

import sys
if sys.version_info < (3, 2):
    raise Exception("Must use Python 3.2 or later")

from hpOneView.common import *
from hpOneView.connection import *
from hpOneView.servers import *
from hpOneView.activity import *
from hpOneView.networking import *
from hpOneView.security import *
from hpOneView.settings import *
from hpOneView.exceptions import *
from hpOneView.search import *


def main():
    parser = argparse.ArgumentParser(add_help=True, description='Usage')
    parser.add_argument('-a', '--appliance', dest='host', required=True,
            help='HP OneView Appliance hostname or IP')
    parser.add_argument('-u', '--user', dest='user', required=True,
            help='HP OneView Username')
    parser.add_argument('-p', '--pass', dest='passwd', required=True,
            help='HP OneView Password')
    parser.add_argument('-c', '--certificate', dest='cert', required=False,
            help='Trusted SSL Certificate Bundle in PEM '
                            '(Base64 Encoded DER) Format')
    parser.add_argument('-r', '--proxy', dest='proxy', required=False,
            help='Proxy (host:port format')
    args = parser.parse_args()
    con = connection(args.host)
    if args.proxy:
        con.set_proxy(args.proxy.split(':')[0], args.proxy.split(':')[1])
    if args.cert:
        con.set_trusted_ssl_bundle(args.cert)
    credential = {'userName': args.user, 'password': args.passwd}
    con.login(args.host, credential)
    con.logout()

if __name__ == '__main__':
    import sys
    import argparse
    sys.exit(main())

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
