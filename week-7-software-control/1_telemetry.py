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
### Part 2: One return value
###

# create an async function called print_distance_sensor() that takes in one variable, the MAVSDK system
#   get the distance sensor measurements using the MAVSDK distance_sensor() function
#   hint: use the async for with a variable called dist
#   hint: the MAVSDK system object contains a telemetry object within, which can call the function
#   print out the value in this format
#       dist: #
#   hint: string concatenation, and don't forget the str() conversion

# TODO: your code goes here

###
### Part 3: Multiple return values
###

# create an async function called monitor_acc_frd() that takes in one variable, the MAVSDK system
#   get the acceleration measurements using the MAVSDK AccelerationFrd() function
#   hint: use the async for in the same way as Part 2, with a variable called acc
#   using conditionals, check if any of forward_m_s2, right_m_s2, or down_m_s2 exceeds 2
#       if it does, print out the direction and value
#       for example: "Yeeted to the right at 3.21 m/s^2"
#   tip: Note the orientation, and which direction is negative
#       for example, top is negative in this case, since forward, down, and right are positive

# TODO: your code goes here

###
### Part 4: The program
###

# now create a variable called drone, which is a MAVSDK System object
# using await, call connect() and set parameter system_address equal to the url

drone = System()
drone.connect(system_address=url)
# notice that we do not include await here, since that is only used inside an asyc function

# call the ensure_future function from asyncio, and pass in the function
# do this twice for both of the functions
# this starts up both of the functions to do their asynchronous tasks
# tip: don't forget to pass in the MAVSDK System object, in this case named drone

asyncio.ensure_future(print_distance_sensor(drone))
asyncio.ensure_future(monitor_acc_frd(drone))

# now the final step, tell asyncio to keep running until the program is terminated

asyncio.get_event_loop().run_forever()

    # also, if you've looked at telemetry.py, you noticed there there is this 
    # if __name__ == "__main__": conditional
    # that is used for code that should only run if it is the main program, so it does not run if it is imported somewhere else
    # you probably won't need to use that, since you can easily copy and paste the functions you want to use from here (instead of importing this file)

###
### End
###

# now you can connect your drone (propellers off!), run this program, and move it around to see the values change
# jerk it around to see if your acceleration monitor is working correctly!