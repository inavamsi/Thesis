import random
class Player():
	def __init__(self,total_turns):
		self.starting_move='C'
		self.my_move_history=[]
		self.opp_move_history=[]
		self.turn=1
		self.total_turns=total_turns
		self.amount=0

	def make_move(self):
		return None

	def update_reward(self,r):
		self.amount+=r

	def update_turn(self):
		self.turn+=1

	def update_move_history(self, my_move, opp_move):
		self.my_move_history.append(my_move)
		self.opp_move_history.append(opp_move)

	def total_reward(self):
		return self.amount

	def new_match(self):
		self.my_move_history=[]
		self.opp_move_history=[]
		self.turn=1

	def change_move(self,move):
		if move=='C':
			return 'NC'
		elif move =='NC':
			return 'C'
		else:
			print("Error: not a valid choice")
			return None

class ALLC(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.type="ALLC"

	def make_move(self):
		return 'C'

class ALLD(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='NC'
		self.type="ALLD"

	def make_move(self):
		return 'NC'

class TFT(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.type="TFT"

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		else:
			return self.opp_move_history[-1]

class GRIM(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.opp_defected=False
		self.type="GRIM"

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		else:
			if self.opp_move_history[-1]=='NC':
				self.opp_defected=True
			if self.opp_defected:
				return 'NC'
			else:
				return 'C'

	def new_match(self):
		self.opp_defected=False
		self.my_move_history=[]
		self.opp_move_history=[]
		self.turn=1

class Randomp(Player):
	def __init__(self,total_turns,p):
		Player.__init__(self,total_turns)
		self.p=p
		if random.random()<self.p:
			self.starting_move= 'NC'
			self.type="Random"

	def make_move(self):
		if random.random()<self.p:
			return 'C'
		else:
			return 'NC'

class Random(Randomp):
	def __init__(self,total_turns):
		Randomp.__init__(self,total_turns,0.5)

class Random_02(Randomp):
	def __init__(self,total_turns):
		Randomp.__init__(self,total_turns,0.2)

class Random_08(Randomp):
	def __init__(self,total_turns):
		Randomp.__init__(self,total_turns,0.8)

class Random_09(Randomp):
	def __init__(self,total_turns):
		Randomp.__init__(self,total_turns,0.9)

class Random_95(Randomp):
	def __init__(self,total_turns):
		Randomp.__init__(self,total_turns,0.95)

class Random_OppD_elseC(Randomp):
	def __init__(self,total_turns):
		Randomp.__init__(self,total_turns,0.5)

	def make_move(self):
		if self.turn!=1:
			if self.opp_move_history[-1] =='C':
				return 'C'

		if random.random()<self.p:
			return 'C'
		else:
			return 'NC'

class Random_OppC_elseD(Randomp):
	def __init__(self,total_turns):
		Randomp.__init__(self,total_turns,0.5)

	def make_move(self):
		if self.turn!=1:
			if self.opp_move_history[-1] =='NC':
				return 'NC'

		if random.random()<self.p:
			return 'C'
		else:
			return 'NC'

class STFT(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='NC'
		self.type="STFT"

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		else:
			return self.opp_move_history[-1]

class TTFT(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.type="TTFT"

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		elif self.turn==2:
			return self.opp_move_history[-1]
		else:
			if self.opp_move_history[-1] =='NC' or self.opp_move_history[-2]=='NC':
				return 'NC'
			return self.opp_move_history[-1]

class TFTT(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.type="TFTT"

	def make_move(self):
		if self.turn<=2:
			return self.starting_move
		else:
			if self.opp_move_history[-1] =='NC' and self.opp_move_history[-2]=='NC':
				return 'NC'
			return self.starting_move

class PAVLOV(Player):
	def __init__(self,total_turns):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.type="PAVLOV"
		# if R or T repeat else change

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		else:
			if self.opp_move_history[-1] =='C':
				return 'C'
			else:
				return self.change_move(self.my_move_history[-1])






