import random
import numpy as np
import copy
import matplotlib.pyplot as plt
import math
from scipy.optimize import least_squares
from scipy.optimize import minimize

alphaA=0.1
alphaB=0.1
deltaP=0.3
deltaQ=0.35

Bap=0.1
Baq=0.1
Bbp=0
Bbq=0.1

Uap=3
Uaq=-2
Ubp=-3
Ubq=2
print(Uap,Uaq,Ubp,Ubq)

dt=0.0001

def fn(input):
	[A,B,P,Q,alphaA,alphaB,deltaP,deltaQ]=input
	dA = alphaA - Bap*P - Baq*Q
	dB = alphaB - Bbp*P - Bbq*Q
	dP = Bap*Uap*A + Bbp*Ubp*B - deltaP
	dQ = Baq*Uaq*A + Bbq*Ubq*B - deltaQ
	return dA*dA+dB*dB+dP*dP+dQ*dQ

#res=least_squares(fn,[0,0,10,0])
#print(res.x)


cons = ({'type': 'ineq', 'fun': lambda x:  x[0]},
         {'type': 'ineq', 'fun': lambda x: x[1]},
         {'type': 'ineq', 'fun': lambda x: x[2]},
         {'type': 'ineq', 'fun': lambda x: x[3]},
         {'type': 'ineq', 'fun': lambda x: x[4]-0.1},
         {'type': 'ineq', 'fun': lambda x: x[5]-0.1},
         {'type': 'ineq', 'fun': lambda x: x[6]-0.1},
         {'type': 'ineq', 'fun': lambda x: x[7]-0.1})
bnds = ((0, None), (0, None), (0, None), (0, None),(0, None), (0, None), (0, None), (0, None))

res = minimize(fn, [0,0,0,0,0,0,0,0], method='SLSQP', bounds=bnds,constraints=cons)
print(res)