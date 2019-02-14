#!/bin/sh

if [ ! -d ./.env ]; then
    virtualenv .env
    . ./.env/bin/activate
    pip install -U uwsgi==2.0.18 requests
else
    . ./.env/bin/activate
fi

exec uwsgi --http11-socket [::]:9090 --wsgi-file wsgi.py "$@"
