from proj import tasks
from celery import group
from jinja2 import Template
import redis

def task_loop():
    params = {
        'my_string': 'Test title',
        'my_list': [1,2,3,4,5,6],
    }
    res = group(tasks.render.s('1', params) for _ in range(100000)).apply_async()

def run():
    with open('test.html', 'r') as f:
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        r = redis.Redis(connection_pool=pool)
        r.hset('htmls', '1', f.read())
        task_loop()

if __name__ == '__main__':
    run()