# Welcome to MAVSDK!
We've put together this assignment to help you get more familiar with MAVSDK and it's complicated structure of classes, functions, and use of `async`!

## Getting started
You already have the code last week when you downloaded the repository last week. Open back up VS Code or your IDE and head to `week-7-software-controls` folder to find the practice code files.

You should see all the 5 files in this assignment, which goes through setting up and using each of the 5 different plugins to MAVSDK. We'd suggest working through them in order. But read through the rest of this guide before starting.

## Installing Packages
No surprise here, but MAVSDK is not installed on every download of Python. So we'll need to install it (and some other packages) to use them.

Open up your VS Code (or your IDE) and open up the Terminal. Verify you're on the **bash** terminal (this should be the default).

Since you have Python 3 installed, you have access to pip3, which stands for "pip installs packages". How fun.

To install MAVSDK, type the following into the terminal and hit enter.
```
pip3 install mavsdk
```
If this gives you an error, saying that "Could not install packages due to an EnvironmentError: [Errno 13] Permission denied", try adding `--user` to the end of that command, so try
```
pip3 install mavsdk --user
```
which installs it for your computer user only, and not across the entire computer.

You will also need to install asyncio, which can be done with 
```
pip3 install asyncio
```
Nice and easy.

# MAVSDK
You'll find it very handy to have the [MAVSDK-Python API reference](http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/) open while working through the assignment. As you'll soon learn, a significant part of software engineering is looking through and understanding documentation for libraries and packages that you use in your code.

## Understanding the Documentation
While having the guide showing what functions and classes are available, it sure it intimidating given a massive dictionary. Let's go through the [Telemetry](http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/telemetry.html) page, which is probably by far the most confusing due to how long it is. It doesn't help that there is no table of contents on each page.

So first, the entries at the top that start with `class` are the possible return objects from the functions that are shown much further below. For example, the first class shown is `AccelerationFrd`; if you did a search in this page, you'll see that this class is actually an attribute (parameter) within the `Imu` class, which contains a bunch of other classes within.

The actual functions you can call off of telemetry can be found under the `class mavsdk.telemetry.Telemetry` 

Here, the functions have a "Yields" field that shows you what the function returns. For example, you'll see that the function `imu()`, `raw_imu()`, and `scaled_imu()` return the `Imu` object.

# Connecting to the Drone
As mentioned in lecture, this differs based on what computer (Windows vs MacOS) and how you're connecting ot the drone (radio, USB, or wifi).

To start, look through the Connection Strings section in the [Usage/Paradigms MAVSDK Guide](https://mavsdk.mavlink.io/v0.29.0/en/guide/general_usage.html#connection_string).

However, if you plan to have QGroundControl running so that you can monitor your drone (you should), and possibly takeover if anything goes wrong, there's a separate procedure for that. Now that you know what to look for, let's get the port numbers.

## QGround Control is Open
A prerequisite for this to work is that QGC should already be already connected to the drone.
1. Enable mavlink forwarding in QGroundControl
2. Application Settings > MAVLink > Enable MAVLink forwarding
3. Make note of the host name (especially the number after `localhost:`)
Set the connection string to 
`udp://:14445`
or whatever number was after your localhost name

For example:
```
await drone.connect(system_address="udp://:14445")
```

## Telemetry Radio / USB
The instruction below is for QGC **not** open. Use with caution.
### MacOS (usbserial)
1. Open up the Terminal app.
2. Type in and hit enter
```
ls /dev/tty.*
```
3. There should be one that’s usbserial. Copy that one.

An example:
```
await drone.connect(system_address="serial:///dev/tty.usbserial-0001")
```
### Windows (COM Port)
1. Open up the Device Manager settings in the Control Panel
2. Find and expand the Ports (COM & LPT) section
3. Find the Silicon Labs Radio and it’s COM port number

An example:
```
await drone.connect(system_address="serial:///COM1") 
```
## Wifi
The instruction below is also for QGC **not** open. Use with caution.
