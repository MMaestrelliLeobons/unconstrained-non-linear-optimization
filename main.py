#!/usr/bin/python
# -*- coding: utf-8 -*-

from functions import *
from methods import *
from os import mkdir
from os import path

results_path = "results/"
if not path.isdir(results_path):
    mkdir(results_path)

#lines
header = "Method\t" + "Initial_Guess\t" + "Iterations\t" + "Optimal_Point\t" + "Optimal_Value\t" + "Error\t" + "Time\t" + "\n"

print header

#test the methods
m = Method()
fileA = open(results_path + "funcA_results","w")
fileB = open(results_path + "funcB_results","w")

fileA.write(header)
fileB.write(header)

#auxiliary functions
def handleGDM (file, func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
    m.GDM(func, x, tolerance, bracket, maxIter)
    line = "GDM\t" + str(x) + " " + str(m.iterGDM()) + " " + str(m.resultsGDM()) + " " + str(func.Function(x)) + " " + str(m.errorGDM()) + " " + str(m.timeGDM()) + "\n"

    print line
    file.write(line)

#funcA
handleGDM(fileA, funcA(), [1e-6, 1e-6, 1e-6], 1e-4, -1, 1000)

# m.NM(funcA(), 1)
# print ("NM")
# print("result = ", m.resultsNM(), " k = ", m.iterNM())

# m.QNM(funcA(), 1)
# print ("QNM")
# print("result = ", m.resultsQNM(), " k = ", m.iterQNM())

#funcB
handleGDM(fileB, funcB(), [1848, 4], 1e-5, 1, 1000)
# m.NM(funcB(), [1,1])
# print ("NM")
# print("result = ", m.resultsNM(), " k = ", m.iterNM())

# m.QNM(funcB(), [1,1])
# print ("QNM")
# print("result = ", m.resultsQNM(), " k = ", m.iterQNM())

fileA.close()
fileB.close()

