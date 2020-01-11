import DH_Game
import Memory_strategy
import random
import matplotlib.pyplot as plt

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

	def max_amount(self):
		maxp=self.pop[0]
		max_amt=maxp.amount

		for p in self.pop:
			if p.amount>max_amt:
				maxp=p
				max_amt=maxp.amount

		return maxp

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
		p_max=len(self.pop)
		new_pop=[]

		for i in range((int)(p_max*(1-n))):
			p=self.max_amount()
			self.pop.remove(p)
			new_pop.append(p.procreate(p.strategy_params))

		for i in range((int)(p_max*n)):
			sp1=random.choice(new_pop).strategy_params
			sp2=random.choice(new_pop).strategy_params
			new_sp=[]
			for i in range(len(sp1)):
				val=sp1[i]+sp2[i]+np.random.normal(0,0.01)
				val/=2
				new_sp.append(val)
			new_pop.append(random.choice(new_pop).procreate(new_sp))

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
			if i%100 ==0:
				print(i," days")

			self.play_day(mut_type)
			pop_series=self.append_to_popseries_types(pop_series,ptypes)
			
		self.plot(pop_series,vocab,n,total_res,ptypes,mut_type)
		for p in self.pop:
			print(p.strategy_params)

		return self.pop

	def plot(self,pop_series,vocab,n,total_res,ptypes,mut_type):

		for j in pop_series:
			print(j[-1],end=" ")
		print("")

		for ps in pop_series:
			plt.plot(ps)

		plt.title('Memory Types, '+' Days :'+str(n)+', Total resources :'+str(total_res)+' Mutation type: '+str(mut_type))
		plt.legend(ptypes,loc='upper right', shadow=True)

		plt.show()

def diff_memory_types():
	game_para=[0.5, 0, 1, 0.2]
	total_turns=100
	total_res=100
	pop=[]

	ptypes=['Mn_0.1_0_1','Mn_0.1_0_2','Mn_0.1_1_1','Mn_0.1_2_0','Mn_0.1_0_3','Mn_0.1_1_2','Mn_0.1_2_1','Mn_0.1_3_0']
	#ptypes=['Mn_0.01_0_1','Mn_0.01_0_2','Mn_0.01_1_1','Mn_0.01_2_0','Mn_0.01_0_3','Mn_0.01_1_2','Mn_0.01_2_1','Mn_0.01_3_0']

	for i in range(30):
		#pop.append(Memory_strategy.Mn(total_turns,0.1,0,1))
		#pop.append(Memory_strategy.Mn(total_turns,0.1,0,2))
		pop.append(Memory_strategy.Mn(total_turns,0.1,1,1))
		#pop.append(Memory_strategy.Mn(total_turns,0.1,0,3))
		#pop.append(Memory_strategy.Mn(total_turns,0.1,1,2))
		#pop.append(Memory_strategy.Mn(total_turns,0.1,2,1))
		#pop.append(Memory_strategy.Mn(total_turns,0.1,3,0))
		pop.append(Memory_strategy.Mn(total_turns,0.1,2,0))

	mut_type='all'
	#mut_type='one'
	r=Replicator(game_para,total_turns,total_res,pop)
	r.play_days(200,"types",total_res,ptypes,mut_type)

diff_memory_types()

