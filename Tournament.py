import DH_Game
import Strategy

class Std_Tournament():
	def __init__(self,game_para,total_turns,ptypes,pop_indx):
		self.game = DH_Game.Game(game_para)
		self.pop =[]
		self.total_reward=[]
		self.total_turns=total_turns
		self.ptypes=ptypes
		self.pop_indx=pop_indx
		self.generate_fresh_pop()
		

	def generate_fresh_pop(self):
		self.pop=[]
		for pi in self.pop_indx:
			self.pop.append(self.ptypes[pi](self.total_turns))

	def play_match(self,p1_indx,p2_indx):
		self.generate_fresh_pop()
		p1=self.pop[p1_indx]
		p2=self.pop[p2_indx]

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

	def play_RR(self):
		self.total_reward=[]
		for pi in self.pop_indx:
			self.total_reward.append(0)

		for p1_indx in range(0,len(self.pop)-1):
			for p2_indx in range(p1_indx+1,len(self.pop)):
				self.play_match(p1_indx,p2_indx)

		return self.total_reward

	def pop_type(self):
		return list(map(type,self.pop))

def best_in_group(s):
	p_types = [Strategy.ALLC,Strategy.ALLD,Strategy.Random,Strategy.GRIM,Strategy.TFT,Strategy.TTFT,Strategy.TFTT,Strategy.STFT,Strategy.PAVLOV]
	pop_indx =s
	game_para=[0.5, 0, 1, 0.2]
	total_turns=100

	T = Std_Tournament(game_para,total_turns,p_types,pop_indx)
	reward_list=T.play_RR()

	max_val=0
	for i in reward_list:
		if max_val<i:
			max_val=i

	for indx in s:
		print(p_types[indx](total_turns).type,end=" ")
	print("->",end=" ")
	for indx in range(len(s)):
		if reward_list[indx]==max_val:
			print(p_types[s[indx]](total_turns).type,end=" ")

	print("")
	print("")

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item



def main():
	l = [1, 2, 3, 4,5,6,7,8,0]
	l = [x for x in powerset(l)]

	for s in l:
		if len(s)<2:
			continue
		best_in_group(s)
main()
