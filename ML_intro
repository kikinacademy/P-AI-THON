# NUMERICAL: numbers that can be classified into two categories.
# A) DISCRETE: defined numbers
# B) CONTINUOS: no known values

# CATEGORICAL: values that cannot be measured up against each other.

# ORDINAL: can be measured against others.

# CENTRAL TENDENCY MEASURES:
# - MEAN: average
# - MEDIAN: mid point
# - MODE: most common

import numpy
goals = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# MEAN: (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77
mean = numpy.mean(goals)
print(f"Mean is --> {mean}")

# MEDIAN: 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
median = numpy.mean(goals)
print(f"Median is --> {median}")

# MODE: 99, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86 = 86
from scipy import stats
mode = stats.mode(goals, axis=None, keepdims=True)
print(f"Mode is --> {mode}")

# STANDARD DEVIATION: how spread out values are
goals = [32,111,138,28,59,77,97]
sigma = numpy.std(goals)
print(f"\u03C3 is --> {sigma}")

# VARIANCE: square root of variance = standard deviation
variance = numpy.var(goals)
print(f"\u03C3^2 is --> {variance}")

# PERCENTILES: divides a set so that x% of data is lower
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
percentile = numpy.percentile(ages, 75) # Searching for the 75 percent value
print(f"Percentile is --> {percentile}")


##########################################
# DATA DISTRIBUTION
# BIG DATA TESTING SETS
set = numpy.random.uniform(0.0, 5.0, 250) # GENERATES 250 random floats 0<x<5
# VISUALIZE IT IN HISTOGRAM
import matplotlib.pyplot as plt
plt.hist(set, 5) # Number of bars
plt.show()

# A REAL BIG DATA
big_set = numpy.random.uniform(0.0, 10.0, 100000)
plt.hist(set, 10)
plt.show()

# NORMAL/GAUSSIAN DATA DISTRIBUTION: (concentrated arround given value)
set = numpy.random.normal(5.0, 1.0, 100000) # MEAN = 5, STANDARD DEVIATION = 1
plt.hist(set, 100)
plt.show()

# SCATTER PLOT

