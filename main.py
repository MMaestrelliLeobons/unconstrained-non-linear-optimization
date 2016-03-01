#!/usr/bin/python
# -*- coding: utf-8 -*-

from functions import *
from methods import *

#test the methods
m = Method()
fileA = open("funcA_results","w")
fileB = open("funcB_results","w")

fileA.write("Initial_Guess " + "Iterations " + "Optimal_Point " + "Optimal_Value " + "Error " + "Time")
fileB.write("Initial_Guess " + "Iterations " + "Optimal_Point " + "Optimal_Value " + "Error " + "Time")

#funcA
x = [1e-6, 1e-6, 1e-6]
m.GDM(funcA(), x, 1e-4, -1, 10000)
print "GDM"
print"result = ", m.resultsGDM()
print " k = ", m.iterGDM()
print "time elapsed", m.timeGDM()

fileA.write(str(x) + " " + str(m.iterGDM()) + " " + str(m.resultsGDM()) + " " + str(funcA.Function(m.resultsGDM())) + " " + str(m.errorGDM()) + " " + str(m.timeGDM()))

# m.NM(funcA(), 1)
# print ("NM")
# print("result = ", m.resultsNM(), " k = ", m.iterNM())

# m.QNM(funcA(), 1)
# print ("QNM")
# print("result = ", m.resultsQNM(), " k = ", m.iterQNM())

#funcB
x = [1848,4]
m.GDM(funcB(), x, 1e-5, 1, 1000)
print "GDM"
print "result = ", m.resultsGDM()
print "k = " , m.iterGDM()
print "time elapsed", m.timeGDM()

fileB.write(str(x) + " " + str(m.iterGDM()) + " " + str(m.resultsGDM()) + " " + str(funcA.Function(m.resultsGDM())) + " " + str(m.errorGDM()) + " " + str(m.timeGDM()))

# m.NM(funcB(), [1,1])
# print ("NM")
# print("result = ", m.resultsNM(), " k = ", m.iterNM())

# m.QNM(funcB(), [1,1])
# print ("QNM")
# print("result = ", m.resultsQNM(), " k = ", m.iterQNM())

fileA.close()
fileB.close()