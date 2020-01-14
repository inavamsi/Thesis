#2 player Resource Simulation Game

#Definiton of players
import game
import random

class Special_AI():
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

	def strategy(self, opp_profile):

		if opp_profile['humanity'] >random.random():
			return ([0,1],self.strength, self.discount) #the Proability vector of the list of strategies
		#[1,0] represents 'coop'

		else:
			return ([1,0],self.strength, self.discount)

	def procreate(self):
		if self.savings > 5 :
			self.savings-=4
			return type(self)()
		return None

class AI_human(Special_AI):
	def __init__(self):
		Special_AI.__init__(self,1,1,0.56,1,0)
		self.type='AI_human'

class AI_strong(Special_AI):
	def __init__(self):
		Special_AI.__init__(self, 3.1,1,0.3,1,0)
		self.type='AI_strong'

class AI_efficient(Special_AI):
	def __init__(self):
		Special_AI.__init__(self, 1,1,0.3,0.66,0)
		self.type='AI_efficient'

class AI_efficient_human(Special_AI):
	def __init__(self):
		Special_AI.__init__(self, 1,1,0.65,0.83,0)
		self.type='AI_efficient_human'
#(self,1,1,0.557,1,0)
#(self, 3,1,0.3,1,0)

