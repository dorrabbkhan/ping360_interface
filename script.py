"""
Simple script that communicates with the Ping360 and prints output
"""
from brping import Ping360
import time

# initialize and connect to ping360
myPing = Ping360()
myPing.connect_serial("/dev/ttyUSB0", 115200)

# initialize the ping360
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)

# execute infinitely
while True:

    # read data
    data = myPing.transmit()

    # if data found, print it
    if data:
        print(data)
    else:
        print("Failed to get distance data")

    # sleep for a sec
    time.sleep(1)