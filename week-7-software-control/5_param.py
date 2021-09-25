### E96A: Drones
### Week 7 Software Control
### Param

# MAVSDK-Python API, Param plugin http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/param.html
# PX4 Parameter Reference http://docs.px4.io/master/en/advanced_config/parameter_reference.html

# in this practice, let's look at two examples of setting specific parameters using the Param plugin
# first, is to set new PID values using Param, instead of through QGC
# second, is to control the servo in a strangely convoluted way, since PX4 doesn't exactly have a good way to do so yet
# note: we will not be flying the drone in this practice

###
### Part 0: The setup
###

# you know the drill, import the necessary packages and connection url
import asyncio
from mavsdk import System
from mavsdk.param import ParamError

url = "" # TODO: your code goes here
#url = "udp://:14445"

# copy over one set of your PID roll rate controller values you've saved when tuning your drone
rkK = # TODO: your code goes here
rkI = # TODO: your code goes here
rkD = # TODO: your code goes here

###
### Part 1: Updating PID
###

# let's make an async function called update_pid() that takes in one variable, the MAVSDK system, no return value
async def update_pid(drone):
    # Look through the PX4 Parameter Reference to lookup the names of the parameters for the PID rate controller roll
    # JK, that list is massive
    # the parameter names for roll K, I, and D gains are
    #   MC_ROLLRATE_K
    #   MC_ROLLRATE_I
    #   MC_ROLLRATE_D
    # tip: these might look familiar, as they were listed on the QGC Tuning panel as well

    # now let's set the parameters
    # since our values are floats, we will use the set_param_float() function instead
    # just to be safe, let's also put it into a try-except block to catch if anything goes wrong
    # if setting all three were successful, print out "PID updated"
    # TODO: your code goes here

###
### Part 2: The run() function
###

# like last time, there's no separate function needed, so we can just put everything in one main function
async def run():
    # connect to the drone, as usual
    drone = System()
    await drone.connect(system_address=url)
    
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    # update the PID by calling update_pid
    # hint: don't forget the await
    # TODO: your code goes here
    
# the main
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
    
###
### End
###

# To see an implementation of using the Param class to control a servo,
# see servo_control.py from the example folder
