#!/usr/bin/python
# -*- coding: utf-8 -*-

from functions import *
from methods import *

#test the methods
m = Method()

#funcA
m.GDM(funcA(), [1e-6, 1e-6, 1e-6], 1e-4, -1, 10000)
print "GDM"
print"result = ", m.resultsGDM()
print " k = ", m.iterGDM()
print "time elapsed", m.timeGDM()

# m.NM(funcA(), 1)
# print ("NM")
# print("result = ", m.resultsNM(), " k = ", m.iterNM())

# m.QNM(funcA(), 1)
# print ("QNM")
# print("result = ", m.resultsQNM(), " k = ", m.iterQNM())

#funcB
m.GDM(funcB(), [1848,4], 1e-5, 1, 1000)
print "GDM"
print "result = ", m.resultsGDM()
print "k = " , m.iterGDM()
print "time elapsed", m.timeGDM()

# m.NM(funcB(), [1,1])
# print ("NM")
# print("result = ", m.resultsNM(), " k = ", m.iterNM())

# m.QNM(funcB(), [1,1])
# print ("QNM")
# print("result = ", m.resultsQNM(), " k = ", m.iterQNM())