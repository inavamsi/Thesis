import DH_Game
import Strategy
import random
import matplotlib.pyplot as plt
import copy
import math

class Std_Tournament():
	def __init__(self,game_para,total_turns,ptypes,pop_indx):
		self.game = DH_Game.Game(game_para)
		self.pop =[]
		self.total_reward=[]
		self.total_turns=total_turns
		self.ptypes=ptypes
		self.pop_indx=pop_indx
		self.generate_fresh_pop()
		self.total_reputation=[]
		self.total_reward=[]
		for pi in pop_indx:
			self.total_reward.append(0)
			self.total_reputation.append(1)
		
	def generate_fresh_pop(self):
		self.pop=[]
		for pi in self.pop_indx:
			self.pop.append(self.ptypes[pi](self.total_turns))

	def play_match(self,p1_indx,p2_indx,rep_type, verifier):
		#self.generate_fresh_pop()
		p1=self.pop[p1_indx]
		p2=self.pop[p2_indx]
		p1.new_match()
		p2.new_match()

		(fn,penalty,walkover,rep_penalty,threshold)=rep_type
		p1_play=fn(self.total_reputation[p1_indx],self.total_reputation[p2_indx])
		p2_play=fn(self.total_reputation[p2_indx],self.total_reputation[p1_indx])

		score=self.total_turns*self.game.R

		if(not p1_play and not p2_play):
			return
		elif(not p1_play):
			self.total_reward[p1_indx]+=score-penalty
			self.total_reward[p2_indx]+=score+walkover
			return
		elif(not p2_play):
			self.total_reward[p2_indx]+=score-penalty
			self.total_reward[p1_indx]+=score+walkover
			return

		p1_round_reward=0
		p2_round_reward=0

		for i in range(0,self.total_turns):
			p1_move=p1.make_move()
			p2_move=p2.make_move()
			p1_reward,p2_reward = self.game.payoff(p1_move,p2_move)
			p1_round_reward+=p1_reward
			p2_round_reward+=p2_reward

			p1.update_turn()
			p1.update_reward(p1_reward)
			p1.update_move_history(p1_move,p2_move)

			p2.update_turn()
			p2.update_reward(p2_reward)
			p2.update_move_history(p2_move,p1_move)

		p2byp1 = (p2_round_reward+0.1)/(p1_round_reward+0.1)

		if verifier == 'Naive Cooperation':
			if p2byp1 > 1+threshold:
				self.total_reputation[p2_indx]/=rep_penalty
				self.total_reputation[p1_indx]=(self.total_reputation[p1_indx]*rep_penalty)
			elif 1/p2byp1 > 1+threshold:
				self.total_reputation[p2_indx]=(self.total_reputation[p2_indx]*rep_penalty)
				self.total_reputation[p1_indx]/=rep_penalty	
		if verifier =='Strict':
			self.total_reputation[p1_indx]=(self.total_reputation[p1_indx]*(p2byp1))
			self.total_reputation[p2_indx]=(self.total_reputation[p2_indx]*(1/p2byp1))

		if verifier=='Good Behaviour':
			if p2byp1 > 1+threshold:
				self.total_reputation[p2_indx]/=rep_penalty
				self.total_reputation[p1_indx]=(self.total_reputation[p1_indx]*rep_penalty)
			elif 1/p2byp1 > 1+threshold:
				self.total_reputation[p2_indx]=(self.total_reputation[p2_indx]*rep_penalty)
				self.total_reputation[p1_indx]/=rep_penalty	
			else:
				self.total_reputation[p1_indx]=(self.total_reputation[p1_indx]*pow(rep_penalty,threshold))
				self.total_reputation[p2_indx]=(self.total_reputation[p2_indx]*pow(rep_penalty,threshold))

		if verifier =="Retaliating":
			if p2byp1 > 1+2*threshold:
				self.total_reputation[p1_indx]/=rep_penalty
			elif 1/p2byp1 > 1+2*threshold:
				self.total_reputation[p2_indx]/=rep_penalty

		self.total_reward[p1_indx]+=p1.total_reward()
		self.total_reward[p2_indx]+=p2.total_reward()

	def play_RR(self, rep_type,verifier):

		for p1_indx in range(0,len(self.pop)-1):
			for p2_indx in range(p1_indx+1,len(self.pop)):
				self.play_match(p1_indx,p2_indx,rep_type,verifier)

		for i in range(len(self.total_reputation)):
			self.total_reputation[i]=min(1,self.total_reputation[i])

	def pop_type(self):
		return list(map(type,self.pop))

def prob_fn(my_rep,opp_rep):
	r= random.random()
	if r <= opp_rep:
		return True
	return False

def smart_prob_fn(my_rep,opp_rep):
	r= random.random()
	if r <= opp_rep or my_rep<opp_rep:
		return True
	return False

def simulation(p_types,pop_indx,game_para,number_of_rounds,rep_type,verifiers,verifier):

	rep_s=[[]]
	T = Std_Tournament(game_para,number_of_rounds,p_types,pop_indx)
	for i in pop_indx:
		rep_s[0].append(1)
	for i in range(200):
		T.play_RR(rep_type,verifiers[random.choice(verifier)])
		rep_s.append(copy.deepcopy(T.total_reputation))

	return rep_s
	#print(T.total_reward)

def add_to_ts(ts,ts_new):
	for time in range(len(ts)):
		for agent_no in range(len(ts[time])):
			ts[time][agent_no]+=ts_new[time][agent_no]

	return ts

def avg_ts(ts,n):
	for time in range(len(ts)):
		for agent_no in range(len(ts[time])):
			ts[time][agent_no]=ts[time][agent_no]/n

	return ts

def world(n):
	#p_types=[Strategy.Random,Strategy.Random_02,Strategy.Random_08,Strategy.Random_09,Strategy.Random_95,Strategy.Random_OppD_elseC,Strategy.Random_OppC_elseD]
	#pop_indx=[0,1,2,3,4,5,6]
	p_types = [Strategy.ALLC,Strategy.ALLD,Strategy.Random,Strategy.GRIM,Strategy.TFT,Strategy.TTFT,Strategy.TFTT,Strategy.STFT,Strategy.PAVLOV,Strategy.Random_OppD_elseC,Strategy.Random_OppC_elseD]
	pop_indx =[0,1,2,3,4,5,6,7,8]#,9,10]
	game_para=[0.5, 0, 1, 0.2]

	number_of_rounds=100

	rep_type=(smart_prob_fn,10,10,1.1,0.01)#lambdafunction, penalty of withdrawal, reward for opp withdrawal, reputation penalty,threshold)
	

	
	legend=[]
	for i in pop_indx:
		legend.append(p_types[i])
	verifiers=["Naive Cooperation","Strict","Good Behaviour","Retaliating"]
	verifier=[3]

	rep_s =simulation(p_types,pop_indx,game_para,number_of_rounds,rep_type,verifiers,verifier)
	for i in range(n-1):
		new_ts=simulation(p_types,pop_indx,game_para,number_of_rounds,rep_type,verifiers,verifier)
		rep_s=add_to_ts(copy.deepcopy(rep_s),new_ts)

	rep_s=avg_ts(copy.deepcopy(rep_s),n)

	plt.plot(rep_s)
	plt.title('Reputation,  rep_type ='+str(rep_type)+", Verifier="+str(verifier))
	plt.legend(legend,loc='upper left', shadow=True)

	plt.show()

world(30)
