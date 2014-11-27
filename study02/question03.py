# coding: UTF-8
import numpy as np
import math

p_syouga = np.array([2,5])
p_myouga = np.array([-1,2])
px = np.array([1,1])

def distance(a, b):
    return sum((a-b)**2)

print "distance(p_syouga, px) = %f" % distance(p_syouga, px)
print "distance(p_myouga, px) = %f" % distance(p_myouga, px)

if distance(p_syouga, px) > distance(p_myouga, px):
    result = "ミョウガ"
else:
    result = "ショウガ"

print "識別結果は『%s』です!!" % result