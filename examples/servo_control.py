### E96A: Drones
### Examples
### Servo Control Example

# Make note of the following premises of the servo control:
    # The servo is connected to the 6th PWM pin on the flight controller (PWM6)
    # The servo is set up with RC Passthrough on Channel 8 (RC8)
    # The servo is "controlled" via trim, which adjusts where the center action is
    # This control method works best when the control stick/knob for servo on the radio transmitter is set to center

import asyncio
from mavsdk import System
from mavsdk.param import (ParamError,ParamResult)

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14445") # QGC mavlink forwarding

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered!")
            break

    await asyncio.sleep(2)

    print("Getting Disarmed Servo PWM")
    try:
        curr = await drone.param.get_param_int("PWM_MAIN_DIS6")
        print("Disarmed PWM",curr)
    except ParamError as err:
        print("Failed", err._result)

    await asyncio.sleep(2)

    print("-- Arming")
    await drone.action.arm()

    await asyncio.sleep(2)

    # Set the Trim values using Param
    # PX4 Parameter Reference http://docs.px4.io/master/en/advanced_config/parameter_reference.html
    # hint: notice that for RC8_TRIM in the reference, it is a float and is bounded from 800.0 to 2200.0

    print("Setting Servo Min")
    try:
        await drone.param.set_param_float("RC8_TRIM",800.0)
    except ParamError as err:
        print ("Failed", err._result)

    await asyncio.sleep(2)

    print("Setting Servo Max")
    try:
        await drone.param.set_param_float("RC8_TRIM",2200.0)
    except ParamError as err:
        print ("Failed", err._result)

    await asyncio.sleep(2)

    print("Setting Servo Mid")
    try:
        await drone.param.set_param_float("RC8_TRIM",1500.0)
    except ParamError as err:
        print ("Failed", err._result)

    await asyncio.sleep(2)

    print("-- Disarming")
    await drone.action.disarm()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())