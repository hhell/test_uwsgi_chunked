
from __future__ import division, absolute_import, print_function, unicode_literals


import sys
import json


def _dbg(message):
    sys.stderr.write("\n ======= {}\n".format(message))
    sys.stderr.flush()


def try_uwsgi_body_gen():
    try:
        import uwsgi
    except Exception:
        return
    while True:
        chunk = uwsgi.chunked_read()
        _dbg("chunked_read -> {!r}".format(chunk))
        if chunk is None or chunk == b'' or chunk == '':
            return
        yield chunk


def try_uwsgi_body(**kwargs):
    return b''.join(try_uwsgi_body_gen(**kwargs))


def application(env, start_response):
    body = env['wsgi.input'].read()
    if not body:
        body = try_uwsgi_body()
    body_len = len(body)
    body = body.decode('utf-8', errors='replace')
    start_response('200 OK', [('Content-Type', 'application/json')])
    resp_data = json.dumps(dict(body_len=body_len, body=body)).encode('utf-8')
    _dbg("Response: {}".format(resp_data))
    return [resp_data]
