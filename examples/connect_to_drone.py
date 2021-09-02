### E96A: Drones
### Examples
### Connect to Drone

import asyncio
from mavsdk import System

async def connectToDrone():
    drone = System()
    ## Radio Telemetry
    # MacOS
    await drone.connect(system_address="serial:///dev/tty.usbserial-0001") # check in Terminal
    # Windows
    await drone.connect(system_address="serial:///COM1") # check in Control Panel
    # Mavlink Forward
    await drone.connect(system_address="udp://:14445") # check in QGC

    ## Wifi
    # MacOS and Windows
    await drone.connect(system_address="udp://:14445") # TODO
    # Mavlink Forward
    await drone.connect(system_address="udp://:14445") # check in QGC
