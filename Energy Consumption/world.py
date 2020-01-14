import Memory_strategy
import Memory_main

def plot(pop_series,vocab,n,total_res,ptypes,mut_type,w):

	for j in pop_series:
		print(j[-1],end=" ")
	print("")

	for ps in pop_series:
		plt.plot(ps)

	plt.title('Number of Worlds : '+str(w)+',  Memory Types, '+' Days :'+str(n)+', Total resources :'+str(total_res)+' Mutation type: '+str(mut_type))
	plt.legend(ptypes,loc='upper left', shadow=True)

	plt.show()

def world(w, days,vocab,total_res,ptypes,mut_type, game_para,total_turns,pop,flag):
	#print("World 1")
	temp_pop=copy.deepcopy(pop)
	r=Replicator(game_para,total_turns,total_res,temp_pop)
	pop_series = r.play_days(days,vocab,total_res,ptypes,mut_type)
	
	for i in range(w-1):
		#print("World ",i+2)
		temp_pop=copy.deepcopy(pop)

		r=Memory_main.Replicator(game_para,total_turns,total_res,temp_pop)
		ts = r.play_days(days,vocab,total_res,ptypes,mut_type)

		for p in range(len(ptypes)):
			for d in range(days+1):
				pop_series[p][d]+=ts[p][d]

	for p in range(len(ptypes)):
		for d in range(days+1):
			pop_series[p][d]/=w

	if flag : plot(pop_series,vocab,days,total_res,ptypes,mut_type,w)
	maxpop=0
	maxindx=0
	for indx,j in enumerate(pop_series):
		if maxpop<j[-1]:
			maxindx=indx
			maxpop=j[-1]

	return ptypes[maxindx]

def energy_consumption(n,flag):
	game_para=[0.5, 0, 1, 0.2]
	total_turns=100
	total_res=200
	pop=[]

	consumption_per=n
	for i in range(100):
		pop.append(Memory_strategy.Mperp(100,0.1,0,1,[2],consumption_per))
		pop.append(Memory_strategy.Mperp(100,0.1,0,2,[2],consumption_per))
		pop.append(Memory_strategy.Mperp(100,0.1,0,3,[2],consumption_per))
		pop.append(Memory_strategy.Mperp(100,0.1,0,2,[3],consumption_per))
		pop.append(Memory_strategy.Mperp(100,0.1,0,3,[3],consumption_per))
		#pop.append(Mperp(100,0.1,0,6,[]))
		
	ptypes=[]
	for p in pop:
		if p.type not in ptypes:
			ptypes.append(p.type)
	mut_type='all'
	#mut_type='one'
	return world(10,100,"types",total_res,ptypes,mut_type,game_para,total_turns,pop,flag)
