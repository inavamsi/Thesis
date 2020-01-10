import matplotlib.pyplot as plt
import Strategy
import Evolution
import copy

def plot(pop_series,ptypes,game_para,worlds):
	for j in pop_series:
		print(j[-1],end=" ")
	print("")

	for ps in pop_series:
		plt.plot(ps)
	leg=[]
	for p in ptypes:
		leg.append(p(1).type)
	plt.title('Replicator - No mutation , Worlds :'+str(worlds)+', Game Parameters: '+str(game_para)) 
	plt.legend(leg,loc='upper right', shadow=True)
	plt.show()

def world(no_worlds,days,pop_density):
	pop_series=[]

	for p in pop_density:
		pop_series.append([])

	for ps in range(len(pop_series)):
		for i in range(days):
			pop_series[ps].append(0)

	#Add pop series from many worlds
	for k in range(no_worlds):
		if k%10==0:
			print("World ",k)

		ptypes = [Strategy.ALLC,Strategy.ALLD,Strategy.Random,Strategy.GRIM,Strategy.TFT,Strategy.TTFT,Strategy.TFTT,Strategy.STFT,Strategy.PAVLOV]
		game_para=[0.5, 0, 1, 0.2]
		total_turns=20
		total_res=1000	

		r=Evolution.Replicator(game_para,total_turns,total_res,ptypes,copy.deepcopy(pop_density))
		tempps=r.play_days(days)
		for ps in range(len(pop_series)):
			for d in range(days):
				pop_series[ps][d]+=tempps[ps][d]

	#Take average of all worlds
	for ps in range(len(pop_series)):
		for d in range(days):
			pop_series[ps][d]/=no_worlds

	plot(pop_series,ptypes,game_para, no_worlds)


world(30,100,pop_density =[1,1,1,1,1,1,1,1,1])