#2 player Resource Simulation Game

#Definiton of players
import game
import random

class Player():
	def __init__(self, strength, discount, humanity, consumption_rate, savings):
		self.strength=strength
		self.discount=discount
		self.humanity=humanity
		self.consumption_rate=consumption_rate	#per day basis
		self.savings=savings
		self.profile={'humanity':humanity,'strength':strength}

	def update_savings(self,reward):
		self.savings+=reward

	def consume(self):
		self.savings-=self.consumption_rate

	def is_dead(self):
		if self.savings<0:
			return True
		return False

class Human(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='Human'

	def strategy(self, opp_profile):
		return ([1,0],self.strength, self.discount) #the Probability vector of the list of strategies
		#[1,0] represents 'fight'
		#the Proability vector of the list of strategies

class AI(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='AI'

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

	def strategy(self, opp_profile):
		if opp_profile['humanity']==1:
			r=random.random()
			if self.humanity > r:
				return ([1,0],self.strength, self.discount)  #With the probility of its humanity it plays like human
			return ([0,1],self.strength, self.discount) #the Proability vector of the list of strategies
		#[1,0] represents 'coop'

		elif opp_profile['humanity']!=1:
			return ([1,0],self.strength, self.discount)

class AI_undiscounted(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='AI_undiscounted'

	def strategy(self, opp_profile):
		if opp_profile['humanity']==1:
			return ([0,1],self.strength, self.discount) #the Proability vector of the list of strategies
		#[1,0] represents 'coop'

		elif opp_profile['humanity']!=1:
			return ([1,0],self.strength, self.discount)

class AI_strong(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='AI_strong'

	def strategy(self, opp_profile):
		if opp_profile['humanity']==1:
			return ([0,1],self.strength, self.discount) #the Proability vector of the list of strategies
		#[1,0] represents 'coop'

		elif opp_profile['humanity']!=1:
			return ([1,0],self.strength, self.discount)

class AI_efficient(Player):
	def __init__(self, strength, discount, humanity, consumption_rate, savings=0):
		Player.__init__(self, strength, discount, humanity, consumption_rate, savings)
		self.type='AI_efficient'

	def strategy(self, opp_profile):
		if opp_profile['humanity']==1:
			return ([0,1],self.strength, self.discount) #the Proability vector of the list of strategies
		#[1,0] represents 'coop'

		elif opp_profile['humanity']!=1:
			return ([1,0],self.strength, self.discount)
