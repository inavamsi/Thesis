import DH_Game
import Strategy
import random
import matplotlib.pyplot as plt

class Replicator():
	def __init__(self,game_para,total_turns,total_res,ptypes,pop_density):
		self.game = DH_Game.Game(game_para)
		self.pop_density=pop_density
		self.total_reward=[]
		self.total_res=total_res
		self.total_turns=total_turns
		self.ptypes=ptypes
		self.consumption= total_turns
		self.reproduce_cost=total_turns
		for pi in pop_density:
			self.total_reward.append(0)

	def random_player(self):
		tsum=0
		for i in self.pop_density:
			tsum+=i

		r=1
		while(r==1):
			r = random.random()

		sum_so_far=0
		for i in range(0,len(self.pop_density)):
			sum_so_far+=self.pop_density[i]
			if r<sum_so_far/tsum:
				return i
		print("Error in calulating random player. Pop density = ",self.pop_density)
		return None

	def play_match(self,p1_indx,p2_indx):
		#self.generate_fresh_pop()
		p1=self.ptypes[p1_indx](self.total_turns)
		p2=self.ptypes[p2_indx](self.total_turns)

		for i in range(0,self.total_turns):
			p1_move=p1.make_move()
			p2_move=p2.make_move()
			p1_reward,p2_reward = self.game.payoff(p1_move,p2_move)

			p1.update_turn()
			p1.update_reward(p1_reward)
			p1.update_move_history(p1_move,p2_move)

			p2.update_turn()
			p2.update_reward(p2_reward)
			p2.update_move_history(p2_move,p1_move)

		self.total_reward[p1_indx]+=p1.total_reward()
		self.total_reward[p2_indx]+=p2.total_reward()


	def play_day(self):
		#Daytime
		for r in range(self.total_res):
			p1_indx=self.random_player()
			p2_indx=self.random_player()
			self.play_match(p1_indx,p2_indx)

		#Nighttime
		for p in range(0,len(self.pop_density)):
			amount_made=self.total_reward[p]
			if amount_made <= self.consumption*self.pop_density[p]:
				alive=(int)(amount_made/self.consumption)
				self.pop_density[p]=alive
				self.total_reward[p] = amount_made - self.consumption*alive
			else:
				amount_made-=self.consumption*self.pop_density[p]
				kids=(int)(amount_made/self.reproduce_cost)
				self.pop_density[p]+=kids
				self.total_reward[p] = amount_made - self.reproduce_cost*kids

	def plot(self,pop_series):
		for j in pop_series:
			print(j[-1],end=" ")
		print("")

		for ps in pop_series:
			plt.plot(ps)
		plt.show()

	def play_days(self,n):
		pop_series=[]
		for p in self.pop_density:
			pop_series.append([p])

		for i in range(n):
			self.play_day()
			#print(self.total_reward)
			for j in range(len(self.pop_density)):
				pop_series[j].append(self.pop_density[j])

		#self.plot(pop_series)

		return pop_series

#ptypes = [Strategy.ALLC,Strategy.ALLD,Strategy.Random,Strategy.GRIM,Strategy.TFT]
#pop_density =[1,1,1,1,1]
#game_para=[0.5, 0, 1, 0.2]
#total_turns=20
#total_res=1000	

#r=Replicator(game_para,total_turns,total_res,ptypes,pop_density)
#r.play_days(100)


