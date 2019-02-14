
import sys
import json


def application(env, start_response):
    body = env['wsgi.input'].read()
    body_len = len(body)
    body = body.decode('utf-8', errors='replace')
    start_response('200 OK', [('Content-Type','application/json')])
    resp_data = json.dumps(dict(body_len=body_len, body=body)).encode('utf-8')
    sys.stderr.write("Response: {}\n".format(resp_data))
    return [resp_data]
