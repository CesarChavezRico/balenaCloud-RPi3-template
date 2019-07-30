
import serial

import sys
import time

import pendulum


print(sys.version_info)

errors = 0
while True:
    try:
        print('Core container running @ {0}'.format(pendulum.now('America/Chihuahua')))
    except Exception as e:
        errors += 1
        print('In while - Error: {0}'.format(e.__str__()))

    time.sleep(10)
    continue
