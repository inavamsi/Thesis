import random
import numpy as np
from discreteMarkovChain import markovChain
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def bar(p):
	return 1-p

def M1(p1_p,p2_p):
	(pc,pd)=p1_p
	(qc,qd)=p2_p

	m=[]
	for initial_s in ['CC','CD','DC','DD']:
		row=[]
		for final_s in ['CC','CD','DC','DD']:
			if initial_s[1]=='C':
				p=pc
			else:
				p=pd
			if initial_s[0]=='C':
				q=qc
			else:
				q=qd

			if final_s[0]!='C':
				p=bar(p)
			if final_s[1]!='C':
				q=bar(q)

			row.append(p*q)

		m.append(row)

	return np.array(m)

def point(p1_p,p2_p):
	P = M1(p1_p,p2_p)
	mc = markovChain(P)
	mc.computePi('linear') #We can also use 'power', 'krylov' or 'eigen'
	return [mc.pi[-1],mc.pi[-2],mc.pi[-3],mc.pi[-4]]


def plot_first():
	fig = plt.figure()
	ax = plt.axes(projection='3d')

	ax = plt.axes(projection='3d')

	zdata=[]
	xdata=[]
	ydata=[]
	col=[]
	for i in range(1000):
		r=random.random()
		s=random.random()
		t=random.random()
		p1_p=(r,s)
		p2_p=(r,t)

		# Data for three-dimensional scattered points
		zdata.append(r)
		xdata.append(s)
		ydata.append(t)
		if s>t:
			col.append(point(p1_p,p2_p))
		else:
			col.append(point(p2_p,p1_p))

	ax.scatter3D(xdata, ydata, zdata, c=col, cmap='Greens');

	plt.show()

#plot_first()

def plot_CnD():
	fig = plt.figure()
	ax = plt.axes(projection='3d')

	ax = plt.axes(projection='3d')

	zdata=[]
	xdata=[]
	ydata=[]
	col=[]
	for i in range(10000):
		r=random.random()
		s=random.random()
		t=random.random()
		p1_p=(r,s)
		p2_p=(r,t)

		# Data for three-dimensional scattered points
		
		if s>t:
			l=point(p1_p,p2_p)
		else:
			l=point(p2_p,p1_p)
		
		if l[-1]>0.8 :
			zdata.append(r)
			xdata.append(s)
			ydata.append(t)
			col.append([0,1,0])
		if l[0]>0.8 :
			zdata.append(r)
			xdata.append(s)
			ydata.append(t)
			col.append([1,0,0])

	ax.scatter3D(xdata, ydata, zdata, c=col, cmap='Greens');

	plt.show()

plot_CnD()