#2 player Resource Simulation Game

#No evolution
#No groups, all individual

import random
import players
import game
import numpy as np

class Simulate():
	def __init__(self,pop, resource):
		self.pop =pop #list of player entities
		self.resource = resource #limit per day
		self.resource_value=1
		temp_ts =self.__demography()
		self.timeseries={}
		for ptype in temp_ts.keys():
			self.timeseries[ptype]=[temp_ts[ptype]]
		temp_trait_mean_ts=self.__trait_means()
		self.traits_mean_ts={}  #average savings,humanity, strength...
		for trait in temp_trait_mean_ts.keys():
			self.traits_mean_ts[trait]=[temp_trait_mean_ts[trait]]

	def __trait_means(self):
		mean={'savings':[],'humanity':[], 'strength':[],'consumption_rate':[]}
		total_savings=0
		total_humanity=0
		total_strength=0
		total_consumption_rate=0
		for p in self.pop:
			total_savings+=p.savings
			total_humanity+=p.humanity
			total_strength+=p.strength
			total_consumption_rate+=p.consumption_rate
		
		if(self.pop==[]):
			mean['savings']=0
			mean['humanity']=0
			mean['strength']=0
			mean['consumption_rate']=0
		else:
			mean['savings']=total_savings/len(self.pop)
			mean['humanity']=total_humanity/len(self.pop)
			mean['strength']=total_strength/len(self.pop)
			mean['consumption_rate']=total_consumption_rate/len(self.pop)
		return mean


	def __demography(self): #calculates demography of population
		demo={}
		for p in self.pop:
			if p.type in demo.keys():
				demo[p.type]+=1
			else:
				demo[p.type]=0
		return demo

	def __choose_players(self):  #return 2 players from the population
		player1=random.randint(0,len(self.pop)-1)
		player2=random.randint(0,len(self.pop)-1)			
		while(player2==player1):
			player2=random.randint(0,len(self.pop)-1)

		return(player1,player2)

	def __update_play(self,player1,player2):  #Update the rewards gained by each player in an encounter
		strat1=self.pop[player1].strategy(self.pop[player2].profile)  #player1's startegy seeing player2's profile
		strat2=self.pop[player2].strategy(self.pop[player1].profile)  #player2's startegy seeing player1's profile
		reward1 = game.Game.payoff(strat1,strat2,self.resource_value)	#player 1 reward
		reward2 = game.Game.payoff(strat2,strat1,self.resource_value)	#player 2 reward
		self.pop[player1].update_savings(reward1)
		self.pop[player2].update_savings(reward2)

	def __consume(self):
		for p in self.pop:
			p.consume()

	def __kill(self):  #remove those who have died
		temp=[]
		for p in self.pop:
			if not p.is_dead():
				temp.append(p)
		self.pop=temp

	def __birth(self): # add new life
		for p in self.pop:
			child =p.procreate()
			if child!=None:
				self.pop.append(child)

	def simulate_day(self): #simulate all changes to population in a unit time duration
		for i in range(0,self.resource):
			(player1,player2)=self.__choose_players()
			self.__update_play(player1,player2)
		self.__consume()
		self.__kill()
		self.__birth()

		for ptype in self.timeseries.keys():
			if ptype in self.__demography().keys():
				self.timeseries[ptype].append(self.__demography()[ptype])
			else:
				self.timeseries[ptype].append(0)

		for trait in self.traits_mean_ts.keys():
			self.traits_mean_ts[trait].append(self.__trait_means()[trait])


