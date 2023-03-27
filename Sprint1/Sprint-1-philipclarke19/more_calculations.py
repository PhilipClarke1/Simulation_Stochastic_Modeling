import matplotlib
from matplotlib import pyplot as plt
import math
"""
Practice working with the data.txt file 

Key ideas: opening and looping through a file line-by-line
"""

## Keep working on this file
#
# Add elements to calculate the other components that you need:
# Mean, quartiles, etc
#
# Standard deviation


def calc_mean(values):
  """
  Calculate the mean of the given list of values 
  input values: a list of floats
  output the mean of those values
  """

  return sum(values) / len(values)


def calc_median(values):
  values.sort()
  length = len(values)
  
  if length % 2 == 0:
    mid = values[length // 2]
    midup = values[length // 2 + 1]
    return (mid + midup) / 2
  else:
    return values[length // 2 + 1]

def calc_variance(values):
  mean = calc_mean(values)
  length = len(values)
  sum = 0
  for i in values:
    num = (i - mean) * (i - mean)
    sum += num
  return sum / (length - 1)
                
def calc_stdev(values):
  mean = calc_mean(values)
  length = len(values)
  sum = 0
  for i in values:
    num = (i - mean) * (i - mean)
    sum += num
  return math.sqrt(sum / (length - 1))
  



# To open a file use open
f = open('data.txt', 'r')

# Make a list to hold the lines from the file
#
# Lists vs. Arrays
#
# Arrays are fixed in size and single type
# Lists can be mixed type and dynamically resizeable
data = []

# Use a for loop to iterate over the lines in f
for line in f:
  data.append(float(line))

# Calculate the mean using a function
print("Mean:", calc_mean(data))

# calculate the median using a function
print("Median:", calc_median(data))

# calculate the variance 
print("Variance:", calc_variance(data))

# calculate the standard deviation
print("Standard Deviation:", calc_stdev(data))

# Create a new figure -- you must do this before calling a plotting function
plt.figure()

# Create a histogram with 15 bins
plt.hist(data, 15)

# Title and axis labels
plt.title('Histogram')
plt.xlabel('Data value')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('histogram.pdf', bbox_inches='tight')

# Create a new figure -- you must do this before calling a plotting function
plt.figure()


fig = plt.figure()
# Create an axes instance
ax = fig.add_axes([0,0,1,1])

bp = ax.boxplot(data)

plt.title('Boxplot')
plt.xlabel('Data Values')
plt.ylabel('Count')
# Create the boxplot
plt.savefig('Boxplot.png', bbox_inches='tight')