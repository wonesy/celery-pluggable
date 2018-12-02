from __future__ import absolute_import, unicode_literals
from typing import List
from proj.app import celery
import redis
import jinja2

pool = redis.ConnectionPool(host='localhost', port=6379, db=0, max_connections=1)
r = redis.Redis(connection_pool=pool)

@celery.task
def render(key, params):
    print("here")
    raw_html = r.hget('htmls', key)
    print(raw_html)
    t = jinja2.Template(str(raw_html))
    return t.render(params)

@celery.task
def add(x, y):
    print('fast task')
    return x + y