### E96A: Drones
### Python Practice
### Loops

# Feel free to comment out your code for other Parts you’re not currently working on.
# A quick way to comment out a lot of code is to select the lines and press Ctrl(Cmd) + /

###
### Part 1: for a while
###

# using range(), create a for loop that prints out the even numbers sequentially from 10 to 2 (inclusive)
# tip: when using range that counts down, you need to specify the step

# TODO: your code goes here

# using a counter variable, create a while loop that prints out the even numbers sequentially from 10 to 2

# TODO: your code goes here

# as you can see, while both get the same job done, one approach (for) is better than the other
# this is one of the principles of python, where there should just be one proper approach to handle a task

###
### Part 2: Triangle
###

# using for loops, print out this:
#   * * * * *
#   * * * *
#   * * * 
#   * *
#   *
# note: there is a space between each star
# hint: think of the main (outer) for loop as each line, and the inner loop prints out the star loop many times
# tip: use the arguments inside print() to help you out, such as the "end" argument

# TODO: your code goes here

###
### Part 3: Collatz Conjecture
###

# consider a simple function:
#   for a given number,
#   if the number is even, divide it by two
#   if the number is odd, triple it and add one
# surprisingly, such as simple formula leads to some very interesting mathematical analysis
# the Collatz Conjecture (which is still unproven!) states that this process will eventually reach the number 1, regardless of which positive integer is chosen initially

# create a function called collatz that takes in one input (integer)
# the function returns the result of the function on the input
# tip: since the function might involve division, consider converting the return value to an int

# TODO: your code goes here

# now have the user enter a positive number (integer)
# create a list with the user entered number
# using a while loop, call the collatz function you have made and append the result to the list until the result is 1
# once outside the loop, print the length and maximum value from the list
# you can also print out the list if you're curious to see the progression
# hint: use len() to get the length, max() for maximum value (and fyi, min() gets the smallest value)
#   for example, print(len(list_var)) and print(max(list_var))

# TODO: your code goes here

###
### End
###