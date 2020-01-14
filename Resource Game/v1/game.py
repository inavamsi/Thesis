#2 player Resource Simulation Game

#Definiton of interaction pf 2 players

class Game():  
	def __init__(self):
		self.strategies=['fight','coop']
		#['fight','coop']

	def __fighting_chance(strength1, strength2):
		return pow(strength1,2)/(pow(strength1,2)+pow(strength2,2))

	def payoff(my_strategy, opp_strategy, resource_value):
		(strategy_vec1,strength1,discount1)=my_strategy
		(strategy_vec2,strength2,discount2)=opp_strategy

		if strategy_vec1==[0,1]: # If my_strategy is to coop
			if strategy_vec2==[0,1]:
				return resource_value*discount1/2
			else: 
				return 0
			#return resource_value*strategy_vec2[1]*discount1/2 #return d/2 only if opp_strategy== coop

		elif strategy_vec1==[1,0]: # If my_strategy is to fight
			if strategy_vec2 == [1,0]: # opponent is also 'fight'
				return resource_value*Game.__fighting_chance(strength1,strength2)*discount1
			elif strategy_vec2 == [0,1]: # opponent is 'coop'
				return resource_value*discount1
