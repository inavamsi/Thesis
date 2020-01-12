import DH_Game
import Memory_strategy
import random
import matplotlib.pyplot as plt
import copy

class Replicator():
	def __init__(self,game_para,total_turns,total_res,pop):
		self.game = DH_Game.Game(game_para)
		self.pop=pop
		self.total_res=total_res
		self.total_turns=total_turns
		self.consumption= total_turns
		self.reproduce_cost=total_turns

	def random_player(self):
		if(len(self.pop)<2):
			print("Error: Pop is less than 2")
			return None
		return random.randint(0,len(self.pop)-1)
		

	def play_match(self,p1_indx,p2_indx):
		#self.generate_fresh_pop()
		
		p1=self.pop[p1_indx]
		p2=self.pop[p2_indx]

		for i in range(0,self.total_turns):
			p1_move=p1.make_move()
			p2_move=p2.make_move()
			p1_reward,p2_reward = self.game.payoff(p1_move,p2_move)

			p1.update_turn()
			p1.update_amount(p1_reward)
			p1.update_move_history(p1_move,p2_move)

			p2.update_turn()
			p2.update_amount(p2_reward)
			p2.update_move_history(p2_move,p1_move)

	def play_day(self,mut_type):
		#Daytime
		if self.pop==[]:
			print("Error: No Pop")
		elif len(self.pop)==1:
			pop[1].update_reward(game.max_reward()*self.total_turns)
		else:
			for r in range(self.total_res):
				p1_indx=self.random_player()
				p2_indx=self.random_player()
				while(p1_indx==p2_indx):
					p2_indx=self.random_player()
				self.play_match(p1_indx,p2_indx)

		#Nighttime
		new_pop=[]
		for p in self.pop:
			p.update_amount(-p.consumption)
			if not p.is_dead():
				while (p.total_amount()>self.reproduce_cost+p.consumption):
					if mut_type=='all':
						kid=p.procreate_allM()
					elif mut_type=='one':
						kid=p.procreate_oneM()
					else :
						print("Error. Wrong mut_type.")
						return None
					new_pop.append(kid)
					p.update_amount(-self.reproduce_cost)
					#print("***",p.strategy_params,"-->",kid.strategy_params)
				new_pop.append(p)
			#else :
				#print("***",p.strategy_params)

		self.pop = new_pop

	def append_to_popseries_types(self,pop_series,ptypes):
		pop_density=[]
		for i in ptypes:
			pop_density.append(0)

		for p in self.pop:
			if p.type in ptypes:
				pop_density[ptypes.index(p.type)]+=1
			else:
				print("Error. Type not in ptypes. p.type = ",p.type)
				return None

		for i in range(len(pop_series)):
			pop_series[i].append(pop_density[i])

		return pop_series

	def play_days(self,n,vocab,total_res,ptypes,mut_type):
		pop_series=[]
		for i in ptypes:
			pop_series.append([])

		pop_series=self.append_to_popseries_types(pop_series,ptypes)

		for i in range(n):
			#if i%100 ==0:
				#print(i," days")

			self.play_day(mut_type)
			pop_series=self.append_to_popseries_types(pop_series,ptypes)
			
		#self.plot(pop_series,vocab,n,total_res,ptypes,mut_type)
		#for p in self.pop:
			#print(p.strategy_params)

		return pop_series

def world(w, days,vocab,total_res,ptypes,mut_type, game_para,total_turns,pop):
	#print("World 1")
	temp_pop=copy.deepcopy(pop)
	r=Replicator(game_para,total_turns,total_res,temp_pop)
	pop_series = r.play_days(days,vocab,total_res,ptypes,mut_type)
	
	for i in range(w-1):
		#print("World ",i+2)
		temp_pop=copy.deepcopy(pop)

		r=Replicator(game_para,total_turns,total_res,temp_pop)
		ts = r.play_days(days,vocab,total_res,ptypes,mut_type)

		for p in range(len(ptypes)):
			for d in range(days+1):
				pop_series[p][d]+=ts[p][d]

	for p in range(len(ptypes)):
		for d in range(days+1):
			pop_series[p][d]/=w

	maxpop=0
	maxindx=0
	for indx,j in enumerate(pop_series):
		if maxpop<j[-1]:
			maxindx=indx
			maxpop=j[-1]

	return ptypes[maxindx]

def best_in_group(s):
	game_para=[0.5, 0, 1, 0.2]
	total_turns=100
	total_res=100*(s[0]+s[1]+s[2]+s[3]+s[4])
	pop=[]

	consumption_per=5
	for i in range(30):
		if s[0]:
			pop.append(Memory_strategy.Mperp(100,0.1,0,1,[2],consumption_per))
		if s[1]:
			pop.append(Memory_strategy.Mperp(100,0.1,0,2,[2],consumption_per))
		if s[2]:
			pop.append(Memory_strategy.Mperp(100,0.1,0,3,[2],consumption_per))
		if s[3]:
			pop.append(Memory_strategy.Mperp(100,0.1,1,2,[2],consumption_per))
		if s[4]:
			pop.append(Memory_strategy.Mperp(100,0.1,1,1,[2],consumption_per))
		#pop.append(Memory_strategy.Mperp(100,0.1,0,6,[]))
		
	ptypes=[]
	for p in pop:
		if p.type not in ptypes:
			ptypes.append(p.type)
	mut_type='all'
	#mut_type='one'
	return world(10,300,"types",total_res,ptypes,mut_type,game_para,total_turns,pop)

def f(l):
		return [0]+l
def g(l):
	return [1]+l

def comb(n):
	if n==0:
	return [[]]
	l=[]
	small=comb(n-1)
	l=list(map(f,small))+list(map(g,small))
	return l

def main():
	l=comb(5)

	for s in l:
		if sum(s)<2:
			continue
		print(s, " -> ",best_in_group(s))




