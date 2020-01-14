class Game():
    def __init__(self,payoff_list):
        [self.R,self.S,self.T,self.P]=payoff_list
        #T>R>P>S
        if self.T <= self.R or self.R <=self.P or self.P <=self.S :
            print("Error: Game not porper IPD/DH")

    def payoff(self,s1,s2):
        if s1 =='C':
            if s2 =='C':
                return (self.R,self.R)
            elif s2 =='NC':
                return (self.S,self.T)
            else :
                print("Error: Wrong strategy input   :",s1,"   ",s2)
                return None
        elif s1 =='NC':
            if s2 =='C':
                return (self.T,self.S)
            elif s2 =='NC':
                return (self.P,self.P)
            else :
                print("Error: Wrong strategy input")
                return None
        else:
            print("Error: Wrong strategy input   :",s1,"   ",s2)
            return None

    
