# Welcome to MAVSDK!
We've put together this assignment to help you get more familiar with MAVSDK and it's complicated structure of classes, functions, and use of `async`!

## Getting started
You already have the code last week when you downloaded the repository last week. Open back up VS Code or your IDE and head to `week-7-software-controls` folder to find the practice code files.

You should see all the 5 files in this assignment, which goes through setting up and using each of the 5 different plugins to MAVSDK. We'd suggest working through them in order.

# MAVSDK
You'll find it very handy to have the [MAVSDK-Python API reference](http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/) open while working through the assignment. As you'll soon learn, a significant part of software engineering is looking through and understanding documentation for to libraries and packages that your code uses.

## Connecting to the Drone
As mentioned in lecture, this differs based on what computer (Windows vs MacOS) and how you're connecting ot the drone (radio, USB, or wifi).

To start, look through the Connection Strings section in the [Usage/Paradigms MAVSDK Guide](https://mavsdk.mavlink.io/v0.29.0/en/guide/general_usage.html#connection_string).

However, if you plan to have QGroundControl running so that you can monitor your drone (you should), and possibly takeover if anything goes wrong, there's a separate procedure for that. Now that you know what to look for, let's get the port numbers.

### QGround Control is Open
1. Enable mavlink forwarding in QGroundControl
2. Application Settings > MAVLink > Enable MAVLink forwarding
3. Make note of the host name (especially the number after `localhost:`)
Set the connection string to 
`udp://:14445`
or whatever number was after your host name

For example:
```
await drone.connect(system_address="udp://:14445")
```

### Telemetry Radio / USB
The instruction below is for QGC **not** open. Use at your own caution.
#### MacOS (usbserial)
1. Open the Terminal app.
2. Type in and hit enter
```
ls /dev/tty.*
```
3. There should be one that’s usbserial. Copy that one.
An example:
```
await drone.connect(system_address="serial:///dev/tty.usbserial-0001")
```
#### Windows (COM Port)
1. Open Device Manager (in Control Panel)
2. Expand the Ports (COM & LPT)
3. Find the Silicon Labs Radio and it’s COM port number

An example:
```
await drone.connect(system_address="serial:///COM1") 
```
### Wifi
The instruction below is also for QGC **not** open. Use at your own caution.
