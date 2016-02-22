#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import math
from golden_section_search import *
from broyden_fletcher_goldfarb_shanno import *

class Method:

    def __init__(self):
        self._xGDM = -1
        self._iterGDM = -1
        self._xNM = -1
        self._iterNM = -1
        self._xQNM = -1
        self._iterQNM = -1

    def GDM(self, func, x, tolerance = 1e-5, bracket = 1, maxIter = 100): 
        """
        Gradient Descent Method:
        func -> function to be minimized
        x -> first guess
        tolerance -> error tolerance for Golden Section Search
        bracket -> Golden Section Search first guess
        maxIter -> maximum number of iterations
        """

        for k in range(1, maxIter):
            direction = -func.Gradient(x).T
            func.preSearch(x, direction)
            step = GSS(func.phi, bracket, tolerance)
            aux = x
            print x, step, direction
            x = x + step * direction
            if np.allclose(x, aux, atol=tolerance) == 1:
                break

        self._xGDM = x
        self._iterGDM = k

    def resultsGDM(self):
        return self._xGDM

    def iterGDM(self):
        return self._iterGDM

    def NM(self, func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
        """
        Newton Method:
        func -> function to be minimized
        x -> first guess
        tolerance -> error tolerance for Golden Section Search
        bracket -> Golden Section Search first guess
        maxIter -> maximum number of iterations
        """
        
        for k in range(1, maxIter):
            direction = -np.dot(np.linalg.inv(func.Hessian(x)), func.Gradient(x))
            func.preSearch(x, direction)
            step = GSS(func.phi, bracket, tolerance)
            aux = x
            x = x + step * direction
            if np.allclose(x, aux, atol=tolerance) == 1:
                break

        self._xNM = x
        self._iterNM = k

    def resultsNM(self):
        return self._xNM

    def iterNM(self):
        return self._iterNM

    def QNM(self, func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
        """
        Quasi-Newton Method:
        func -> function to be minimized
        x -> first guess
        tolerance -> error tolerance for Golden Section Search
        bracket -> Golden Section Search first guess
        maxIter -> maximum number of iterations
        """

        hessian = np.linalg.inv(func.Hessian(x))

        for k in range(1, maxIter):
            direction = -np.dot(hessian, func.Gradient(x))
            func.preSearch(x, direction)
            step = GSS(func.phi, bracket, tolerance)
            aux = x
            x = x + step * direction
            if np.allclose(x, aux, atol=tolerance) == 1:
                break
            hessian = BFGS(func, x, aux, hessian)

        self._xQNM = x
        self._iterQNM = k

    def resultsQNM(self):
        return self._xQNM

    def iterQNM(self):
        return self._iterQNM
