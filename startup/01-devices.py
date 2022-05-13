print(f'Loading {__file__}...')

import time as ttime
start = ttime.monotonic()

my_dev = MyDev('', name='my_dev')

duration = ttime.monotonic() - start  # seconds
durations[__file__] = duration
