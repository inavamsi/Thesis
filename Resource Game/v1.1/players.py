#2 player Resource Simulation Game

#Definiton of players
import game
import random

class Player():
	def __init__(self, initial_traits, trait_improvement_function, trait_improvement_pvector, trait_improvement_conditions):
		self.trait_list=list(traits.keys())
		self.strength=traits['strength']
		self.discount=traits['discount']
		self.humanity=traits['humanity']
		self.consumption_rate=traits['consumption_rate']	#per day basis
		self.savings=traits['savings']
		self.procreate_cost=traits['procreate_cost']
		self.action_cost=traits['action_cost'] # lambda functions for cost for improvement
		self.action_chance=traits['action_chance'] # lambda functions for chance of doing stuff in a day provided it can afford it

	def update_savings(self,reward):
		self.savings+=reward

	def consume(self):
		self.savings-=self.consumption_rate

	def is_dead(self):
		if self.savings<0:
			return True
		return False

	def procreate(self):
		if self.type=='Human':
			return None
		if self.savings > 10 :
			self.savings-=9
			return type(self)(self.strength, self.discount, self.humanity, self.consumption_rate,0)
		return None

class Human(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='Human'
		self.profile={'humanity':self.humanity,'strength':self.strength,'type':self.type}

	def strategy(self, opp_profile):
		return ([1,0],self.strength, self.discount) #the Probability vector of the list of strategies
		#[1,0] represents 'fight'
		#the Proability vector of the list of strategies

class AI(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='AI'
		self.profile={'humanity':self.humanity,'strength':self.strength,'type':self.type}

	def strategy(self, opp_profile):
		if opp_profile['humanity']==1:
			return ([0,1],self.strength, self.discount) #the Proability vector of the list of strategies
		#[1,0] represents 'coop'

		elif opp_profile['humanity']!=1:
			return ([1,0],self.strength, self.discount)
		
class AI_prob(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='prob_AI'
		self.profile={'humanity':self.humanity,'strength':self.strength,'type':self.type}

	def strategy(self, opp_profile):
		if opp_profile['humanity']==1:
			r=random.random()
			if self.humanity > r:
				return ([1,0],self.strength, self.discount)  #With the probility of its humanity it plays like human
			return ([0,1],self.strength, self.discount) #the Proability vector of the list of strategies
		#[1,0] represents 'coop'

		elif opp_profile['humanity']!=1:
			return ([1,0],self.strength, self.discount)

