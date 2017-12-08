'''
    Notice:
    1. The function for jit should locate in mfs
    2. For the usage of jit types and signatures, please refer Numba documentation <http://numba.github.com/numba-doc/0.14/index.html>
'''
from __future__ import absolute_import
from __future__ import print_function
from dpark import DparkContext, jit
import numpy
from six.moves import range

dpark = DparkContext()

@jit('f8(f8[:])')
def add1(x):
    sum = 0.0
    for i in range(x.shape[0]):
        sum += i*x[i]
    return sum

@jit
def add2(x):
    sum = 0.0
    for i in range(x.shape[0]):
        sum += i*x[i]
    return sum

def add3(x):
    sum = 0.0
    for i in range(x.shape[0]):
        sum += i*x[i]
    return sum

rdd = dpark.makeRDD(list(range(0, 10))).map(lambda x: numpy.arange(x*1e7, (x+1)*1e7))

print(rdd.map(add1).collect())
print(rdd.map(add2).collect())
print(rdd.map(add3).collect())
