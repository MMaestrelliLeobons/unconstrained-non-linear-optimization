import numpy as np
import math

class funcA:

    def Function(x):
        return math.sqrt(np.sum(x))

    def Gradient(x):
        x_grad = 1 / (2 * math.sqrt(np.sum(x)))
        grad = np.array([x_grad, x_grad, x_grad])
        return grad

    def Hessian(x):
        x_hessian = -1 / (4 * math.pow(np.sum(x), 3/2))
        hessian = np.array([[x_hessian, x_hessian, x_hessian],
                            [x_hessian, x_hessian, x_hessian],
                            [x_hessian, x_hessian, x_hessian]])
        return hessian

    def preSearch(x, direction):
        self.xPhi = x
        self.directionPhi = direction

    def phi(alpha):
        return math.sqrt(np.sum(self.xPhi) + np.sum(self.directionPhi) * alpha)
        

class funcB:

    def Function(x):
        return math.log(1 + math.pow(x[0] - 2, 2) + math.pow(x[1] - 1, 2))

    def Gradient(x):
        denominator = math.pow(x[0] - 2, 2) + math.pow(x[1] - 1, 2) + 1
        x1_grad = 2 * (x[0] - 2) / denominator
        x2_grad = 2 * (x[1] - 1) / denominator
        grad = np.array([x1_grad, x2_grad])
        return grad

    def Hessian(x):
        denominator = math.pow(x[0] - 2, 2) + math.pow(x[1] - 1, 2) + 1
        x11_hessian = (2 / denominator) - math.pow(2 * x[0] - 4, 2) / math.pow(denominator, 2)
        x12_hessian = -4 * (x[0] - 2) * (x[1] - 1) / math.pow(denominator, 2)
        x21_hessian = x12_hessian
        x22_hessian = (2 / denominator) - math.pow(2 * x[1] - 2, 2) / math.pow(denominator, 2)
        hessian = np.array([[x11_hessian, x12_hessian],
                            [x21_hessian, x22_hessian]])
        return hessian

    def preSearch(x, direction):
        self.xPhi = x
        self.directionPhi = direction

    def phi(alpha):
        return math.log(1 + math.pow(self.xPhi[0] + alpha * self.directionPhi[0] - 2, 2) + math.pow(self.xPhi[1] + alpha * self.directionPhi[1] - 1, 2))
                      
        
    
