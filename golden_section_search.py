#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import functions

golden_ratio = (math.sqrt(5) - 1) / 2

def GSS(phi, bracket, tolerance):
    """
    Golden Section Search:
    phi -> function to be minimized
    bracket -> first guess
    tolerance -> error tolerance
    """

    a = 0
    s = bracket
    b = 2 * bracket
    
    while phi(b) < phi(s):
        a = s
        s = b
        b = 2 * b

    u = b - golden_ratio * (b - a)
    v = a + golden_ratio * (b - a)
    while abs(u - v) > tolerance:
        
        if phi(u) < phi(v):
            b = v
            v = u
            u = b - golden_ratio * (b - a)
        else:
            a = u
            u = v
            v = a + golden_ratio * (b - a)
            
    return (u + v) / 2
