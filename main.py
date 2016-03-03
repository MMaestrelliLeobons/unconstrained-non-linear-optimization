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

#test the methods
m = Method()
fileA = open(results_path + "funcA_results", "w")
fileB = open(results_path + "funcB_results", "w")

fileA.write(header)
fileB.write(header)

#auxiliary functions
def handleGDM (file, func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
    m.GDM(func, x, tolerance, bracket, maxIter)
    line = "GDM\t" + str(x) + "\t" + str(m.iterGDM()) + "\t" + str(m.resultsGDM()) + "\t" + str(func.Function(x)) + "\t" + str(m.errorGDM()) + "\t" + str(m.timeGDM()) + "\n"

    print line
    file.write(line)

def handleNM (file, func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
    m.NM(func, x, tolerance, bracket, maxIter)
    line = "NM\t" + str(x) + "\t" + str(m.iterNM()) + "\t" + str(m.resultsNM()) + "\t" + str(func.Function(x)) + "\t" + str(m.errorNM()) + "\t" + str(m.timeNM()) + "\n"

    print line
    file.write(line)

def handleQNM (file, func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
    m.QNM(func, x, tolerance, bracket, maxIter)
    line = "QNM\t" + str(x) + "\t" + str(m.iterQNM()) + "\t" + str(m.resultsQNM()) + "\t" + str(func.Function(x)) + "\t" + str(m.errorQNM()) + "\t" + str(m.timeQNM()) + "\n"

    print line
    file.write(line)
    
#funcA
print "funcA\n"
print header

func_a = funcA()

handleGDM(fileA, func_a, [1e-6, 1e-6, 1e-6], 1e-4, -1, 1000)
# handleNM(fileA, func_a, [1, 4, 1])
# handleQNM(fileA, func_a, [1, 4, 1])

#funcB
print "funcB\n"
print header

func_b = funcB()
handleGDM(fileB, func_b, [1848, 4], 1e-5, 1, 1000)
handleNM(fileB, func_b, [1848, 4], 1e-5, 1, 1000)
handleQNM(fileB, func_b, [1848, 4], 1e-5, 1, 1000)

fileA.close()
fileB.close()

