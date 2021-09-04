### E96A: Drones
### Week 7 Software Control
### Offboard

# MAVSDK-Python API, Offboard plugin http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/offboard.html

# Feel free to take a look at offboard_position_ned.py from the example folder for some tips

# in this practice, let's make our drone takeoff, and fly forward some distance via offboard, and land
# almost like an early test flight from the Ingenuity helicopter on Mars :)

# FYI "offboard" is named so since the control of the drone is done elsewhere off of the flight computer board, thus off-board

###
### Part 0: The setup
###

# you know the drill, import the necessary packages and connection url
import asyncio
from mavsdk import System
from mavsdk.action import ActionError
from mavsdk.offboard import (OffboardError, PositionNedYaw)
# notice how we specifically import classes and exceptions
# let's import another useful package, math
import math

url = "" # TODO: your code goes here
#url = "udp://:14445"

# let's define a variable move for how far the drone flies forward
# set move equal to 1
move = 1.0

# let's define another variable heading for which direction the drone flies forward
# set heading equal to 0 degrees (this is Yaw, where 0 is North, and turns clockwise)
# think of this as polar coordinates (move is radius, heading is angle)
heading = 0.0

# lastly, define an altitude for the drone to fly at
# set alt equal to 1 meter
alt = 1.0

###
### Part 1: The run() function
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

    # like in the takeoff_and_landing.py, let's check for a good GPS signal first
    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate ok")
            break

    # using the same try-except block from before, arm your drone (but do not takeoff)
    print("Arming drone")
    # TODO: your code goes here

    ###
    ### Part 2: The offboard
    ###

    # in order to command the drone via offboard, we need to start it
    # using another try-except block, try drone.offboard.start()
    # tip: as the API reference says, this raises an OffboardError if any issue arises
    print("Starting Offboard")
    # TODO: your code goes here

    # we'll be using the MAVSDK function set_position_ned() to move the drone
    # notice that the positive directions are North, East, and Down
    # also notice that we need to pass in a PositionNedYaw object to this function

    # let's first orient the drone in the direction we want to go, while staying in place
    # create a new PositionNedYaw object called pos0 with the proper arguments
    # hint: North and East are both 0, the Down = -alt, and Yaw = heading
    # TODO: your code goes here

    # call set_position_ned with pos0
    #   this will make the drone up and point in the proper direction
    # then using asyncio.sleep, pause the code for 10 seconds to let the drone reach its position
    # TODO: your code goes here

    # now let's make the drone move that distance
    # create another PositionNedYaw object called pos1
    # hint: it's trigonometry time- you'll need to use math.cos() and math.sin() for North and East
    #   hint: cos() and sin() functions take radian values, so convert them using math.radians()
    # hint: the other two values are the same, Down = -alt, and Yaw = heading
    # TODO: your code goes here

    # call set_position_ned with pos1
    # then using asyncio.sleep, pause the code for 10 seconds to let the drone reach its position
    # TODO: your code goes here

    # now we can make the drone land with offboard as well
    # create another PositionNedYaw object called pos2
    # hint: to land, North, East, and Down are all 0, and we can keep Yaw = heading
    # TODO: your code goes here

    # call set_position_ned with pos2
    # then using asyncio.sleep, pause the code for 10 seconds to let the drone reach its position
    # TODO: your code goes here

    # now that we're done, let's stop offboard
    # using another try-except block, try drone.offboard.stop()
    # tip: as the API reference says, this raises an OffboardError if any issue arises
    # now add a finally statement which disarms the drone
    print("Stopping Offboard")
    # TODO: your code goes here


# the main
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
    
###
### End
###