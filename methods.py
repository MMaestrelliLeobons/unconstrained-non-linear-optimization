import numpy as np
import math
import functions
import golden_section_search
import broyden_fletcher_goldfarb_shannon

class Method:

    def GDM(func, x, tolerance = 1e-5, bracket = 1, maxIter = 100): 
        """
        Gradient Descent Method:
        func -> function to be minimized
        x -> first guess
        tolerance -> error tolerance for Golden Section Search
        bracket -> Golden Section Search first guess
        maxIter -> maximum number of iterations
        """

        for k in range(0, maxIter - 1):
            direction = -func.fGradient(x).T
            func.preSearch(x, direction)
            step = GSS(func.phi, bracket, tolerance)
            aux = x
            x = x + step * direction
            k = k + 1
            if x == aux:
                break

        self.xGDM = x
        self.iterGDM = k

    def resultsGDM():
        return self.xGDM

    def iterGDM():
        return self.iterGDM

    def NM(func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
        """
        Newton Method:
        func -> function to be minimized
        x -> first guess
        tolerance -> error tolerance for Golden Section Search
        bracket -> Golden Section Search first guess
        maxIter -> maximum number of iterations
        """
        
        for k in range(0, maxIter - 1):
            direction = -np.dot(np.linalg.inv(func.Hessian(x)), func.Gradient(x))
            func.preSearch(x, direction)
            step = GSS(func.phi, bracket, tolerance)
            aux = x
            x = x + step * direction
            k = k + 1
            if x == aux:
                break

        self.xNM = x
        self.iterNM = k

    def resultsNM():
        return self.xNM

    def iterNM():
        return self.iterNM

    def QNM(func, x, tolerance = 1e-5, bracket = 1, maxIter = 100):
        """
        Quasi-Newton Method:
        func -> function to be minimized
        x -> first guess
        tolerance -> error tolerance for Golden Section Search
        bracket -> Golden Section Search first guess
        maxIter -> maximum number of iterations
        """

        hessian = np.linalg.inv(func.Hessian(x))

        for k in range(0, maxIter - 1):
            direction = -np.dot(hessian, func.Gradient(x))
            func.preSearch(x, direction)
            step = GSS(func.phi, bracket, tolerance)
            aux = x
            x = x + step * direction
            k = k + 1
            if x == aux:
                break
            hessian = BFGS(func, x, aux, hessian)

        self.xQNM = x
        self.iterQNM = k

    def resultsQNM():
        return self.xQNM

    def iterQNM():
        return self.iterQNM
