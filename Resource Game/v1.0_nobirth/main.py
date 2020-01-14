#2 player Resource Simulation Game

#No evolution
#No groups, all individual

import players
import numpy as np
import simulate
import special_ai

import matplotlib.pyplot as plt

class World():
	def __init__(self,n):
		self.ts ={}
		self.n=n

	def add_humans(self):
		p=[]
		for i in range(1000):
			newph=players.Human(1, 1, 1, 1, 0)
			p.append(newph)
		return p

	def add_ai(self):
		p=[]
		for i in range(1000):
			newph=players.AI_prob(0.8,0.8,1,0.5,0)
			p.append(newph)
			newph=players.AI(1,0.5,0,0.2,0)
			p.append(newph)
		return p

	def add_sp_ai(self):
		p=[]
		for i in range(1000):
			newph=special_ai.AI_efficient()
			p.append(newph)
			newph=special_ai.AI_strong()
			p.append(newph)
			newph=special_ai.AI_human()
			p.append(newph)
		return p

	def new_world(self):
		p=[]
		#p+=self.add_humans()
		#p+=self.add_ai()
		p+=self.add_sp_ai()

		s=simulate.Simulate(p, 100)

		for i in range(400):
			s.simulate_day()

		return s.timeseries

	def add_to_ts(self,new_ts):
		if list(self.ts.keys())==[]:
			self.ts=new_ts

		r_key=list(self.ts.keys())[0]
		first_ts=self.ts[r_key]
		for i in range(len(first_ts)):
			for ptype in self.ts.keys():
				self.ts[ptype][i]+=new_ts[ptype][i]

	def average_ts(self,n):
		r_key=list(self.ts.keys())[0]
		first_ts=self.ts[r_key]
		for i in range(len(first_ts)):
			for ptype in self.ts.keys():
				self.ts[ptype][i]/=n

	def calculate(self):
		for i in range(self.n):
			new_ts=self.new_world()
			self.add_to_ts(new_ts)

		self.average_ts(self.n)

	def plot(self):
		for ptype in self.ts.keys():
			plt.plot(self.ts[ptype][1:])
			print(ptype," : ",self.ts[ptype][-1])
		plt.ylabel('population')
		plt.show()

w=World(1)  #Create the same configuration of the world 20 times and simulate
w.calculate()	#Add all simulation results and take average
w.plot()   # Plot the average time series
