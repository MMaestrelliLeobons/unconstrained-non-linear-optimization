import numpy as np
import math

class funcA:

    def __init__(self):
        self.xPhi = np.zeros(3)
        self.directionPhi = np.zeros(3)

    def Function(self, x):
        """
            f(x) = sqrt(x1 + x2 + x3)
            x -> [x1, x2, x3]
        """
        return math.sqrt(np.sum(x))

    def Gradient(self, x):
        """
            x -> [x1, x2, x3]
        """
        x_grad = 1 / (2 * math.sqrt(np.sum(x)))
        grad = np.array([x_grad, x_grad, x_grad])
        return grad

    def Hessian(self, x):
        """
            x -> [x1, x2, x3]
        """
        x_hessian = -1 / (4 * math.pow(np.sum(x), 3/2))
        hessian = np.array([[x_hessian, x_hessian, x_hessian],
                            [x_hessian, x_hessian, x_hessian],
                            [x_hessian, x_hessian, x_hessian]])
        return hessian

    def preSearch(self, x, direction):
        """
            x -> [x1, x2, x3]
            direction -> [d1, d2, d3]
        """
        self.xPhi = x
        self.directionPhi = direction

    def phi(self, alpha):
        return math.sqrt(np.sum(self.xPhi) + np.sum(self.directionPhi) * alpha)
        

class funcB:

    def __init__(self):
        self.xPhi = np.zeros(2)
        self.directionPhi = np.zeros(2)

    def Function(self, x):
        """
            f(x) = log(1 + (x1 - 2)^2 + (x2 - 1)^2)
            x -> [x1, x2]
        """
        return math.log(1 + math.pow(x[0] - 2, 2) + math.pow(x[1] - 1, 2))

    def Gradient(self, x):
        """
            x -> [x1, x2]
        """
        denominator = math.pow(x[0] - 2, 2) + math.pow(x[1] - 1, 2) + 1
        x1_grad = 2 * (x[0] - 2) / denominator
        x2_grad = 2 * (x[1] - 1) / denominator
        grad = np.array([x1_grad, x2_grad])
        return grad

    def Hessian(self, x):
        """
            x -> [x1, x2]
        """
        denominator = math.pow(x[0] - 2, 2) + math.pow(x[1] - 1, 2) + 1
        x11_hessian = (2 / denominator) - math.pow(2 * x[0] - 4, 2) / math.pow(denominator, 2)
        x12_hessian = -4 * (x[0] - 2) * (x[1] - 1) / math.pow(denominator, 2)
        x21_hessian = x12_hessian
        x22_hessian = (2 / denominator) - math.pow(2 * x[1] - 2, 2) / math.pow(denominator, 2)
        hessian = np.array([[x11_hessian, x12_hessian],
                            [x21_hessian, x22_hessian]])
        return hessian

    def preSearch(self, x, direction):
        """
            x -> [x1, x2]
            direction -> [d1, d2]
        """
        self.xPhi = x
        self.directionPhi = direction

    def phi(self, alpha):
        return math.log(1 + math.pow(self.xPhi[0] + alpha * self.directionPhi[0] - 2, 2) + math.pow(self.xPhi[1] + alpha * self.directionPhi[1] - 1, 2))

if __name__ == "__main__":
    #Test the functions              
    a = funcA()
    print(a.Function([1,2,3]))
    print(a.Gradient([1,2,3]))
    print(a.Hessian([1,2,3]))
    print(a.preSearch([1,2,3], [0,0,1]))
    print(a.phi(3))
    
    b = funcB()
    print(b.Function([1,2]))
    print(b.Gradient([1,2]))
    print(b.Hessian([1,2]))
    print(b.preSearch([1,2], [0,1]))
    print(b.phi(3))

