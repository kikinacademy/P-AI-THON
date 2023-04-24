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

goals = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
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
goals = [32, 111, 138, 28, 59, 77, 97]
sigma = numpy.std(goals)
print(f"\u03C3 is --> {sigma}")

# VARIANCE: square root of variance = standard deviation
variance = numpy.var(goals)
print(f"\u03C3^2 is --> {variance}")

# PERCENTILES: divides a set so that x% of data is lower
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
percentile = numpy.percentile(ages, 75)  # Searching for the 75 percent value
print(f"Percentile is --> {percentile}")


##########################################
# DATA DISTRIBUTION
# BIG DATA TESTING SETS
set = numpy.random.uniform(0.0, 5.0, 250)  # GENERATES 250 random floats 0<x<5
# VISUALIZE IT IN HISTOGRAM
import matplotlib.pyplot as plt

plt.hist(set, 5)  # Number of bars
plt.show()

# A REAL BIG DATA
big_set = numpy.random.uniform(0.0, 10.0, 100000)
plt.hist(set, 10)
plt.show()

# NORMAL/GAUSSIAN DATA DISTRIBUTION: (concentrated arround given value)
set = numpy.random.normal(5.0, 1.0, 100000)  # MEAN = 5, STANDARD DEVIATION = 1
plt.hist(set, 100)
plt.show()

# DATA DISTRIBUTION
# UNIFORM
set = numpy.random.uniform(0.0, 10.0, 25)
import matplotlib.pyplot as plt

plt.hist(set, 5)
plt.show()

set2 = numpy.random.uniform(0.0, 5.0, 10000)
plt.hist(set2, 5)
plt.show()
# GAUSSIAN
set3 = numpy.random.normal(5.0, 3.0, 25)
plt.hist(set3, 5)
plt.show()

# SCATTER
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()

# LINEAR REGRESSION
import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(
    x, y
)  # r: coefficient , p: hypothesis test , std_err: standard error, icpt_error: intercept error


def func(x):
    return slope * x + intercept


Model = list(map(func, x))

plt.scatter(x, y)
plt.plot(x, Model)
plt.show()

## POLYNOMIAL REGRESSION
import numpy
import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

Model = numpy.poly1d(numpy.polyfit(x, y, 3))

Line = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(Line, Model(Line))
plt.show()

## R-SQUARED
import numpy
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

## import numpy
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)

## BAD FIT
import numpy
import matplotlib.pyplot as plt

x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

print(r2_score(y, mymodel(x)))

## MULTIPLE REGRESSION  [Linear regression +1 ind val & predicting on +2 var
import pandas
df = pandas.read_csv("data.csv")
X = df[['Weight', 'Volume']] # values
y = df['CO2'] # dependent
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X, y)
# predict CO2 emission when the w=2300 & v=1300
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
print(regr.coef_)

predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2) # 107.2087328 + (1000 * 0.00755095) = 114.75968
