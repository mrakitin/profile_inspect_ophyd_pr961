print(f'Loading {__file__}...')

durations = {}

import time as ttime
start = ttime.monotonic()

from ophyd import Device, Signal, Component as Cpt


class MyDev(Device):
    sig = Cpt(Signal)

duration = ttime.monotonic() - start  # seconds
durations[__file__] = duration
