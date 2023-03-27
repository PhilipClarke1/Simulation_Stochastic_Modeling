"""
Write a simulation to estimate the probability of winning at passe dix 

Roll three six-sided dice and the player wins if the sum is > 10
"""

# Basic strategy: write a simulate() that plays one round of
# the game and returns True if the player wins and False otherwise

# The main part of the program will call simulate() repeatedly in a loop and count the number of simulated trials that return True
#
# The fraction of succcessful trials approximates the true winning probability

# We need random number generation to simuate the game
#
# random module contains two functions that we can use
# for random numbers: random and randint
#
# random() returrns a random float in [0.0,1.0]
# randint returna s random integer from a range
# for example, randint(1,6) to simulate a six-sided die

# import randint
from random import randint


# Write a simulate method
def simulate():
  """
  Simulate one round of passe dix 
  Roll three dice and return True if their sum > 10 
  """
  die1 = randint(1, 6)
  die2 = randint(1, 6)
  die3 = randint(1, 6)

  sum = die1 + die2 + die3

  return sum > 10


### Main 
num_trials = 10000
num_wins = 0

# Call simulate repeatedly in a loop
for trial in range(num_trials):
  if simulate():
    num_wins += 1

# Calculate teh fraction of trials that resulted in a win 
frac_wins = num_wins / num_trials

# print output 
#
# Reacall: %4f is the format specifier for four digits 
# after the decimal place 
print('%.4f' % frac_wins)