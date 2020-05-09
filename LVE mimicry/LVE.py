import random
import numpy as np
import copy
import matplotlib.pyplot as plt
import math

Bap=0.1
Baq=0.1
Bbp=0
Bbq=0.1

alphaA=0.11
alphaB=0.1
deltaP=0.1
deltaQ=0.1
 
    
Uap=2
Uaq=3
Ubp=-3
Ubq=-2
print(Uap,Uaq,Ubp,Ubq)

dt=0.0001

def simulate(days, A,B,P,Q):
	A_list=[]
	B_list=[]
	P_list=[]
	Q_list=[]

	for i in range(days):
		
		dA = alphaA*A - Bap*A*P - Baq*A*Q
		dB = alphaB*B - Bbp*B*P - Bbq*B*Q
		dP = Bap*Uap*A*P + Bbp*Ubp*B*P - deltaP*P
		dQ = Baq*Uaq*A*Q + Bbq*Ubq*B*Q - deltaQ*Q
		'''if Uaq*A + Ubq*B > 0:
			dQ = Baq*Uaq*A*Q + Bbq*Ubq*B*Q - deltaQ*Q
		else:
			dQ = -delta*Q
		'''
		#print(dA," ",dB)
		A+=dA*dt
		B+=dB*dt
		P+=dP*dt
		Q+=dQ*dt

		A_list.append(A)
		B_list.append(B)
		P_list.append(P)
		Q_list.append(Q)

	plt.plot(A_list)
	plt.plot(B_list)
	plt.plot(P_list)
	plt.plot(Q_list)
	plt.xticks([])
	plt.yticks([])

	plt.title('Special Case 2 Perturbation')
	plt.legend(['A',"B","P","Q"],loc='upper right', shadow=True)
	print(A," ",B," ",P," ",Q)
	plt.show()


simulate(5000000,0.51, 0.25  , 0.1, 1)   
