import numpy as np
import math
import functions

def BFGS(func, x, xOld, hessian):
	"""
	Broyden–Fletcher–Goldfarb–Shanno Algorithm:
	func -> function to have its Hessian estimated
	x and xOld -> used to calculate BFGS paremeters p and q
	hessian -> Hessian to be updated
	"""

	p = x - xOld
	q = func.Gradient(x) - func.Gradient(xOld)
	denominator = np.dot(p.T, q)

	hessian = hessian + (1 + np.dot(np.dot(q.T, hessian), q) / denominator) * (np.dot(p, p.T) / denominator) - (np.dot(np.dot(p, q.T), hessian) + np.dot(np.dot(hessian, q), p.T)) / denominator

	return hessian