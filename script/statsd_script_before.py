import random
import time

while True:
    random.seed()
    random_sleep_interval = random.randint(5, 15)
    print('Got random interval to sleep: {}'.format(random_sleep_interval))
    time.sleep(random_sleep_interval)
