### E96A: Drones
### Week 7 Software Control
### Telemetry

# MAVSDK-Python API, Telemetry plugin http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/telemetry.html

# Feel free to take a look at telemetry.py from the example folder for some tips

###
### Part 0: Importing the necessary packages
###

# let's import the necessary packages
# 1. asyncio
# 2. System from mavsdk

# TODO: your code goes here 

###
### Part 1: The Setup
###

# create a variable called url that holds the connection string to the drone
# the idea of putting it up here is to have an easy access to change
# you can have multiple, and comment out the ones you're not using
# (i.e. have one ready for with QGC, and another for without)

url = "" # TODO: your code goes here
#url = "udp://:14445"

###
### Part 2: Distance Sensor
###

# create an async function called print_distance_sensor() that takes in one variable, the MAVSDK system, no return value
#   get the distance sensor measurements using the MAVSDK distance_sensor() function
#   hint: use the async for with a variable called dist
#   tip: in the API reference, notice how the function returns the DistanceSensor object
#       the value we want is current_distance_m, so what we want is dist.current_distance_m
#   print out the value in this format
#       dist: #
#   hint: string concatenation, and don't forget the str() conversion

async def print_distance_sensor(drone):
    # TODO: your code goes here

###
### Part 3: Odometry
###

# create an async function called monitor_vel_xyz() that takes in one variable, the MAVSDK system, no return value
#   get the acceleration measurements using the MAVSDK odometry() function
#   hint: use the async for in the same way as Part 2, with a variable called odom
#   tip: in the API reference, notice how the function returns the Odometry object
#       the values that we're interested in are the velocity_body, which contain x_m_s, y_m_s, z_m_s
#       hint: the XYZ coordinates in PX4: positive X is forward, Y is right, and Z is down 
#   using conditionals, check if any of x_m_s, y_m_s, or z_m_s exceeds 1 m/s
#       if it does, print out the direction and value
#       for example: "Zoomin to the right at 3.21 m/s^2"
#   tip: Note the orientation, and which direction is negative
#       for example, top is negative in this case, since forward, down, and right are positive

async def monitor_vel_xyz(drone):
    # TODO: your code goes here

###
### Part 4: The central function
###

# since the functions to connect and start up the drone is also done in async, we need to put them in a function as well
# definte an async function called run()

async def run():

    # now create a variable called drone, which is a MAVSDK System object
    # using await, call connect() and set parameter system_address equal to the url

    drone = System()
    await drone.connect(system_address=url)

    # let's add some code to let us know if the drone has connected
    # using async for, we check the connection of the drone in the Core plugin
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break
    # break is a keyword that lets us jump out of a loop

    # before we start up the call to our telemetry, let's set the rate at which the drone will transmit the telemetry messages
    # use the set_rate_... functions to set both of the telemetry rates we're using.
    # note: some functions in MAVSDK may appear to not work if you don't set the rate, as the drone would otherwise not publish the data
    # the parameter is in hertz, or essentially how many times it is sent per second
    # let's set the odometry at 10 hz, and the distance sensor at 5

    await drone.telemetry.set_rate_odometry(10) # odometry will not be received if you don't set this
    await drone.telemetry.set_rate_distance_sensor(5)

    # call the ensure_future function from asyncio, and pass in the function
    # do this twice for both of the functions
    # this starts up both of the functions to do their asynchronous tasks
    # tip: don't forget to pass in the MAVSDK System object, in this case named drone

    asyncio.ensure_future(print_distance_sensor(drone))
    asyncio.ensure_future(monitor_acc_frd(drone))

# now outside of all functions, this is the first thing the program runs
# call the ensure_future function from asyncio on the central function

asyncio.ensure_future(run())

# now the next step, tell asyncio to keep running until the program is terminated

asyncio.get_event_loop().run_forever()

    # also, if you've looked at telemetry.py, you noticed there there is this 
    # if __name__ == "__main__": conditional
    # that is used for code that should only run if it is the main program, so it does not run if it is imported somewhere else
    # you can use that, but is probably not necessary, since you can easily copy and paste the functions you want to use from here (instead of importing this file)

###
### End
###

# now you can connect your drone (propellers off!), run this program, and move it around to see the values change
# jerk it around to see if your velocity monitor is working correctly!