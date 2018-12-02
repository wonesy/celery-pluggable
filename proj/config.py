broker_config = {
    'redis': {
        'broker': 'redis',
        'host': 'localhost',
        'port': 6379,
        'vhost': None,
    },
    'rabbitmq': {
        'broker': 'pyamqp',
        'host': 'guest@localhost',
        'port': 5672,
        'vhost': None,
    }
}