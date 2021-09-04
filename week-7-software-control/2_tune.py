### E96A: Drones
### Week 7 Software Control
### Tune

# MAVSDK-Python API, Tune plugin http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/tune.html

# Note: (no pun intended), but as you might have realized, this "tune" is about music, not calibrating your drone!

# Feel free to take a look at tune.py from the example folder for some tips

# in this practice, let's make the drone play a song, and then have it play a song when it moves fast

###
### Part 0: The setup
###

# let's import the necessary packages
# 1. asyncio
# 2. System from mavsdk
# 3. SongElement, TuneDescription, and TuneError from mavsdk.tune
#   notice from tune.py we can list them using parenthesis

# TODO: your code goes here

# let's copy over the drone connection string from 1_telemetry.py

url = "" # TODO: your code goes here
#url = "udp://:14445"

###
### Part 1: A song
###

# create an empty list called song
# using the MAVSDK SongElement, add elements
# if you don't have a music background and have no idea whats going on
#   use this basic example

song = []
song.append(SongElement.NOTE_C)
song.append(SongElement.NOTE_E)
song.append(SongElement.NOTE_G)
song.append(SongElement.NOTE_E)
song.append(SongElement.NOTE_C)

# TODO: your code goes here

# create a variable called tempo, and set it to your song's tempo
# let's use 120 bpm (beats per minute) if you don't know what this is

tempo = 120

###
### Part 2: Play the song
###

# create an async function called play_song() that takes in one variable, the MAVSDK system, no return value
#   create a variable called tune_description that creates a MAVSDK TuneDescription object using our song and tempo

async def play_song(drone):
    # TODO: your code goes here

#   using await, call the MAVSDK play_tune with our tune_description
#   hint: since this is a function under tune, we'll need to call it off of the MAVSDK system object passed in
#   place this call inside a try and except block, in case the request fails (likely due to improper song list)
#       if play_tune raises an exception, print out that an error occured

    # TODO: your code goes here

###
### Part 3: Conditionally play
###

# copy over your monitor_vel_xyz() function from 1_telemetry.py
#   now have it also play the song in addition to printing out the value when a velocity exceeds 1
#   tip: calling it through await should suffice

# TODO: your code goes here

###
### Part 4: The central function
###

# like last time, let's make a function called run that connects to the drone and runs the functions

async def run():

    # connect to the drone

    drone = System()
    await drone.connect(system_address=url)
    
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    # now unlike last time, we don't need to set the rate for our play_song function, since we don't receive data
    
    # let's just have the drone simply do the play_song first
    await play_song(drone)

    # once you've verified that this works, comment out await play_song(drone) above
    # also comment out the loop.run_until_complete(run()) below

    # let's see our new monitor_vel_xyz in action
    # for this we'll need to use asyncio.ensure_future (uncomment out the line below)

    # await drone.telemetry.set_rate_odometry(10)
    # asyncio.ensure_future(monitor_vel_xyz(drone))

    
# since we are not "subscribing" to information, we don't need to call asyncio.ensure_future
# instead, we simply call it to run until completion

loop = asyncio.get_event_loop()
# comment out the line below for monitor_vel_xyz
loop.run_until_complete(run())

# uncomment the code below for monitor_vel_xyz
# asyncio.ensure_future(run())
# loop.run_forever()

###
### End
###

# be sure to test out both functions of your code!