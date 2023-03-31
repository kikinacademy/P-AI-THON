from numpy.lib.function_base import percentile 
# NUMERICAL 
# 1) DISCRETE: defined numbers (measures) 
# 2) CONTINUOUS: infinite numbers 
 
# CATEGORICAL: values that cannot be measured up against each other 
 
# ORDINAL: can be measured against each other 
 
# CENTRAL TENDENCY: mean, median, mode 
import numpy 
goals = [99,86,87,88,111,86,103,87,94,78,77,85,86] 
mean = numpy.mean(goals) 
print(f"Mean is --> {mean}") 
 
median = numpy.median(goals) 
print(f"Median is --> {median}") 
 
from scipy import stats 
mode = stats.mode(goals, axis=None, keepdims=True) 
print(f"Mode is --> {mode}") 
 
# STANDARD DEVIATION 
goals = [31,111,138,28,59,77,97] 
sigma = numpy.std(goals) 
print(f"\u03C3 is --> {sigma}") 
 
# VARIANCE 
variance = numpy.var(goals) 
print(f"\u03C3^2 is --> {variance}") 
 
 
# PERCENTILES 
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31] 
percentile = numpy.percentile(ages, 75) 
print(f"Percentile is --> {percentile}") 
 
# DATA DISTRIBUTION 
set = numpy.random.uniform(0.0,10.0,25) 
import matplotlib.pyplot as plt 
plt.hist(set,5) 
plt.show() 
 
set2 = numpy.random.uniform(0.0,5.0,10000) 
plt.hist(set2,5) 
plt.show()0000 
set3 = numpy.random.normal(5.0, 3.0, 25) 
plt.hist(set3,5) 
plt.show() 
