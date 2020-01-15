
import random
import numpy as np
import copy

class Player():
    def __init__(self,total_turns):
    	self.starting_move='C'
    	self.my_move_history=[]
    	self.opp_move_history=[]
    	self.turn=1
    	self.total_turns=total_turns
    	self.amount=0
    	self.type=None

    def reset(self):
    	self.my_move_history=[]
    	self.opp_move_history=[]
    	self.turn=1
    	self.amount=0

    def make_move(self):
    	return None

    def update_amount(self,r):
    	self.amount+=r

    def update_turn(self):
    	self.turn+=1

    def update_move_history(self, my_move, opp_move):
    	self.my_move_history.append(my_move)
    	self.opp_move_history.append(opp_move)

    def total_amount(self):
    	return self.amount

    def is_dead(self):
    	if self.amount<0:
    		return True
    	return False

    def change_move(self,move):
    	if move=='C':
    		return 'NC'
    	elif move =='NC':
    		return 'C'
    	else:
    		print("Error: not a valid choice")
    		return None

    def returnC(self, p):
    	r=random.random()
    	if r<p:
    		return 'C'
    	else:
    		return 'NC'

class Mn(Player): # A player with random attributes, mutation rate var, and memory given by (my_memory,opp_memory)
	def __init__(self,total_turns,var,my_memory,opp_memory,strategy_params=None):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		if strategy_params==None:
			self.strategy_params=[]
			# Memory is stored as a binary string of length my_memory+opp_memory. If 1 => 'C' was played
			#The value corresponds to the probability of playing 'C'
			for i in range(int(pow(2,my_memory+opp_memory))):
				self.strategy_params.append(random.random())
		else:
			self.strategy_params=strategy_params
		self.var=var
		self.my_memory=my_memory
		self.opp_memory=opp_memory
		self.type='Mn('+str(my_memory)+','+str(opp_memory)+')'
		#print(self.type,"  ",my_memory,"  ",opp_memory)

	def normalp(self):
		return np.random.normal(0,self.var)

	def procreate_allM(self):

		new_strat=[]
		for p in self.strategy_params:
			r = self.normalp()
			new_strat.append(max(0,min(1, p+r)))

		kid = Mn(self.total_turns,self.var,self.my_memory,self.opp_memory,new_strat)
		return kid

	def procreate_oneM(self):

		i = random.randint(0,len(self.strategy_params)-1)
		r = normalp()
		new_strat=copy.deepcopy(self.strategy_params)
		new_strat[i]=max(0,min(1, new_strat[i]+r))

		kid = Mn(self.total_turns,self.var,self.my_memory,self.opp_memory,new_strat)
		return kid

	def getp_from_strategy_params(self,para_list):
		index=0
		mult=1
		n=len(para_list)
		for i in range(n):
			if para_list[n-i-1]=='C':
				index+=mult

			mult*=2
		return self.strategy_params[index]

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		elif self.turn<max(self.my_memory,self.opp_memory):
			#Make better
			return self.returnC(0.5)
		else:
			if self.my_memory==0:
				para_list = self.opp_move_history[int(-self.opp_memory):]
			elif self.opp_memory==0:
				para_list = self.my_move_history[int(-self.my_memory):]
			else:
				para_list = self.my_move_history[int(-self.my_memory):]+self.opp_move_history[int(-self.opp_memory):]

			p = self.getp_from_strategy_params(para_list)
			return self.returnC(p)
