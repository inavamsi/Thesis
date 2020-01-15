import random
import DH_Game 
import Memory_strategy
import Perceptron_strategy
import Strategy
import Discounted_Var_Strategy
import RM

game_para=[0.5, 0, 1, 0.2]
game = DH_Game.Game(game_para)


#To check if an agent behaves like TFT
# Play with ALLC, ALLD, TFT, Random

def match(p1,p2,total_turns):

	p1.my_move_history=[]
	p1.opp_move_history=[]
	p1.turn=1

	p2.my_move_history=[]
	p2.opp_move_history=[]
	p2.turn=1

	p1r=0
	p2r=0
	for i in range(0,total_turns):
		p1_move=p1.make_move()
		p2_move=p2.make_move()

		p1.update_turn()
		p1.update_move_history(p1_move,p2_move)

		p2.update_turn()
		p2.update_move_history(p2_move,p1_move)

		p1_reward,p2_reward = game.payoff(p1_move,p2_move)
		p1r+=p1_reward
		p2r+=p2_reward


	return (p1r,p2r)

def in_threshold(p1,p2,p,total_turns,threshold):
	s1=match(p1,p,total_turns)[0]
	s2=match(p2,p,total_turns)[0]
	#total+=1
	if abs(s1-s2)<= threshold*total_turns/100:
		return True
	return False

def agent_similarity(p1,p2,total_turns,threshold):
	passed=0
	total=0
	'''for p_class in [Strategy.ALLC,Strategy.ALLD,Strategy.TFT,Strategy.PAVLOV,Strategy.STFT]:
		p=p_class(total_turns)
		for i in range(20):
			s1=match(p1,p,total_turns)[0]
			s2=match(p2,p,total_turns)[0]
			total+=1
			if abs(s1-s2)<= threshold*total_turns/100:
				passed+=1
				'''
	for p_class in [Strategy.DetRandom,Strategy.DetRandom,Strategy.DetRandom,Strategy.ALLC,Strategy.ALLD,Strategy.TFTT,Strategy.TTFT,Strategy.PAVLOV,Strategy.GRIM]:

		p=p_class(total_turns)
		p1.reset()
		p2.reset()
		if not in_threshold(p1,p2,p,total_turns,threshold):
			return False

	return True


		
	#return passed*100/total

def perceptron_like_TFT(my_memory,opp_memory,total_turns,threshold):
	#Threshold and Support are percentages
	for layer_list in [[],[2],[3],[2,2],[3,2],[4],[3,3],[3,2,2],[2,2,2]]:
		total=0
		passed=0

		for i in range(10000):
			#if i%1000==0:
			#	print(i," samples")
			#p1=Perceptron_strategy.Mperp(total_turns,0,my_memory,opp_memory,layer_list,0)
			p1=Perceptron_strategy.Mperp(total_turns,0,0,1,[2],0)
			#print(p1.weights,"   ",p1.bias)
			p2=Strategy.TFT(total_turns)
			total+=1
			if agent_similarity(p1,p2,total_turns,threshold):
				passed+=1

		print(layer_list," -> ", passed*100/total)

#p1=Perceptron_strategy.Mperp(100,0,0,1,[],0,([[[0]]],[[0]]))
#print(p1.getp_from_strategy_params(['C']))
def agent_like_TFT(total_turns,threshold):
	#Threshold and Support are percentages
	agent_l=[Perceptron_strategy.Mperp(total_turns,0,0,1,[2],0),
			Perceptron_strategy.Mperp(total_turns,0,1,1,[2],0),
			Perceptron_strategy.Mperp(total_turns,0,0,2,[2],0),
			RM.Mperp(total_turns,0,0,1,[2],0),
			RM.Mperp(total_turns,0,1,1,[2],0),
			RM.Mperp(total_turns,0,0,2,[2],0),
			Memory_strategy.Mn(total_turns,0,0,1),
			Memory_strategy.Mn(total_turns,0,1,1),
			Memory_strategy.Mn(total_turns,0,0,2)
			]
	for j in range(len(agent_l)):
		total=0
		passed=0
		

		for i in range(100000):
			agent_l=[Perceptron_strategy.Mperp(total_turns,0,0,1,[2],0),
			Perceptron_strategy.Mperp(total_turns,0,1,1,[2],0),
			Perceptron_strategy.Mperp(total_turns,0,0,2,[2],0),
			RM.Mperp(total_turns,0,0,1,[2],0),
			RM.Mperp(total_turns,0,1,1,[2],0),
			RM.Mperp(total_turns,0,0,2,[2],0),
			Memory_strategy.Mn(total_turns,0,0,1),
			Memory_strategy.Mn(total_turns,0,1,1),
			Memory_strategy.Mn(total_turns,0,0,2)
			]
			p2=Strategy.TFT(total_turns)
			total+=1
			if agent_similarity(agent_l[j],p2,total_turns,threshold):
				passed+=1

		print(agent_l[j].type," -> ", passed*100/total)

agent_like_TFT(20,10)
#perceptron_like_TFT(0,1,20,0)
'''total_turns=100
p1=Strategy.TFT(total_turns)
p2=Strategy.PAVLOV(total_turns)
p3=Strategy.TTFT(total_turns)
p4=Strategy.TFTT(total_turns)
p5=Strategy.Random(total_turns)
print(agent_similarity(p5,p5,total_turns,5))
print(agent_similarity(p1,p3,total_turns,5))
print(agent_similarity(p1,p4,total_turns,5))

'''







