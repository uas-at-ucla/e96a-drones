### E96A: Drones
### Software Control
### Action

# MAVSDK-Python API, Action plugin http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/action.html

# Feel free to take a look at takeoff_and_land.py, goto.py and the more complex telemetry_takeoff_and_land.py from the example folder for some tips

# in this practice, we'll have your drone fly to specific GPS coordinates
# hint: this will be useful in the autonomous delivery portion of the Final Competition!
# since we won't get a large enough field to fly, you'll just have to trust that this process works :)
#   a.k.a. you won't be able to test this 3_action.py specifically :(

###
### Part 0: The setup
###

# you know the drill, import the necessary packages and connection url
import asyncio
from mavsdk import System
from mavsdk.action import ActionError

url = "" # TODO: your code goes here
#url = "udp://:14445"

# let's create variables to store our GPS coordinates (longitude and latitude)
# let's imagine we can fly anywhere with no restrictions

# first stop: the entrance of Royce Hall 
#   L: 34.0724561, E: -118.4427272 (34°04'20.8"N 118°26'31.9"W)
#   tip: store the decimal values as Long1 and East1
lat1 = 34.0724561
lon1 = -118.4427272

# second stop: the entrance to Bplate
#   L: 34.071772, E: -118.449726
#   notice how close the values are to the coordinates of Royce
lat2 = 34.071772
lon2 = -118.449726

# let's define the altitude the drone will fly
fly_alt = 10.0 # meters

###
### Part 1: The run() function
###

# since there's nothing that'll run concurrently, we'll have everything in the run() function
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

    # since the MAVSDK goto_location() uses AMSL altitude (based on mean sea level), we need to get that value
    # using telemetry, we can obtain the necessary info
    # tip: this needs to be obtained before the drone takes off
    async for terrain_info in drone.telemetry.home():
        abs_alt = terrain_info.absolute_altitude_m
        break

    # set the takeoff altitude using the MAVSDK function set_takeoff_altitude
    # hint: don't forget the await
    # like the examples, consider putting print statements whenever you tell the drone to do something, so you can monitor it

    # TODO: your code goes here

    # now let's try to arm and takeoff using a try-except block
    #   if either fails (throws exception), kill() the drone as a safety measure
    try:
        # TODO: your code goes here
    except ActionError:
        drone.action.kill()

    # let's wait a few seconds (3) for the drone to stabilize and finish it's takeoff
    await asyncio.sleep(3)

    # fly to Royce Hall using the goto_location() function
    # hint: don't forget to add the fly_alt to the abs_alt, or else you'll be flying at ground level
    # put this in a try-except block as well
    # if it catches an ActionError, send the return_to_launch() command to bring the drone back

    # TODO: your code goes here

    # if you're feeling fancy, copy over your play_song code here so the drone plays the song when it arrives

    # now fly to Bplate using the same code to fly to Royce Hall, including the try-except block
    # don't forget to change the variable names lol

    # TODO: your code goes here

    # let's land the drone here and disarm it

    # TODO: your code goes here


# the main
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
    
###
### End
###

