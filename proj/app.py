from __future__ import absolute_import, unicode_literals
from celery import Celery, task
from proj.config import broker_config

def build_broker_uri(broker:str):
    broker = broker_config.get(broker)
    b = broker.get("broker")
    h = broker.get("host")
    p = broker.get("port")
    v = broker.get("virutal")
    if v:
        return f'{b}://{h}:{p}/{v}/'
    else:
        return f'{b}://{h}:{p}//'

celery = Celery('proj',
             broker=build_broker_uri('rabbitmq'),
             backend='redis://localhost',
             include=['proj.tasks'])

celery.conf.update(
    result_expires=3600,
    task_routes={
        'proj.tasks.add': {'queue': 'priority'},
        'proj.tasks.render': {'queue': 'default'},
    }
)

if __name__ == '__main__':
    pass
