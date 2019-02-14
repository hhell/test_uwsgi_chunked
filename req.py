#!./.env/bin/python

from __future__ import division, absolute_import, print_function, unicode_literals

import sys
import time
import requests


addr = 'http://localhost:9090/some/url/'
if len(sys.argv) >= 2:
    addr = sys.argv[1]


def gen():
    yield b'a' * 100 + b'=' + b'b' * 100
    time.sleep(0.5)
    yield b'c' * 100 + b'=' + b'd' * 100
    time.sleep(0.5)
    yield b'e' * 100 + b'=' + b'f' * 100


resp = requests.post(
    addr,
    headers={'content-type': 'application/x-www-form-urlencoded'},
    data=gen(),
    verify=False,
)
print(resp)
print(resp.content)
