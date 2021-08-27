### E96A: Drones
### Week 6 Python Practice
### Classes

# Feel free to comment out your code for other Parts you’re not currently working on.
# A quick way to comment out a lot of code is to select the lines and press Ctrl(Cmd) + /

###
### Part 1: Grid Bot
###

# believe it or not, you've learned enough to make a really simple text-based game at this point!
# the "game" we'll be making is one that we can move a "bot" around on a square Cartesian grid

# create the Bot class
# add two class variables b_x and b_y, the position of the bot, and set them both equal to 0, as we will make all bots spawn at the origin

# the __init__() takes one additional argument, which is its name
#   add an instance variable b_name and set that equal to the argument

# add a method called move() that takes in one argument (a string)
#   the valid moves are 'n','s','e', and 'w'
#   if the argument is invalid, the bot does not move
#   the method will update the position b_x and b_y accordingly
#   the method has no return value

# TODO: your code goes here

# now let's place this bot on a grid
# this grid is in the first quadrant of the Cartesian plane

# create the Grid class
# add a class variable called g_size which will be the size of the grid, and set it equal to 5 for now
# note: keep in mind that the valid grid spaces are 0, 1, 2, 3, 4, but not 5

# the __init__() takes one additional argument, which is the name for the bot
#   add an instance variable g_bot and create a new bot object with the name given in the argument

# add a method called updateSize() that takes in one argument (a int)
#   let's do some verification: if the argument is less than one, return false
#   else if the argument is positve, update g_size with the argument converted to an int and return true

# add a method called cleanUp() that takes in no arguments
#   this method checks if the bot is outside of the grid boundaries (< 0 or >= g_size)
#   if the bot is outside of the boundaries, move the bot back to the origin (almost like a Loki time loop >:))
#   tip: this isn't anything fancy, just reset b_x and b_y to 0
#   this method has no return value

# add a method called display() that takes in no arguments
#   this method prints out the grid and the bots
#   using a two for loops (nested), iterate through each spot of the 2D grid
#   hint: use range(), except be cautious of the y axis (since printing goes downwards, so something needs to be flipped)
#   if the bot is occupying the space, print the first letter of the bot's name and a space
#   tip: you can also use the [] brackets to access characters in a string
#   else, print a dot "•" and a space " " for each empty spot of the grid
#   this method has no return value

# TODO: your code goes here

# now let's play with it
# have the user enter a name for their bot, and create a variable p_game that is a Grid object
# create a variable p_move which stores the input from the user that prompts the valid moves, or 'q' to quit
# in a while loop that runs while p_move is not 'q'
#   move the bot
#   cleanUp the grid
#   display the grid
#   have the user enter a new move and store it into p_move

# TODO: your code goes here

# congrats! you've just made a simple game!
# do play around and mess around to try and catch some bugs (mistakes/errors)

###
### End
###