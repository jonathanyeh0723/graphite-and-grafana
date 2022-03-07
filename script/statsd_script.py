import random
import statsd
import time

HOST = 'localhost'
PORT = 8125

client = statsd.StatsClient(HOST, PORT)

while True:
    random.seed()
    random_sleep_interval = random.randint(5, 15)
    print('Got random interval to sleep: {}'.format(random_sleep_interval))

    time.sleep(random_sleep_interval)
    client.incr('statsd_script.sleep_calls')
