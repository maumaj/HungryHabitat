import random
#Just some ideas on implementation of simulation
#very object oriented. we could go other directions
w,h = 20, 20
board = [[[] for x in range(w)] for y in range(h)] #array of array of arrays
#print(board)

class Plant:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def update(self):
		return

class Prey:
	def __init__(self,x,y,repro):
		self.x=x
		self.y=y
		self.repro=repro
	def update(self):
		rand=random.randint(1,4) #needs collisions checks.
		board[self.x][self.y].remove(self) #think about modulo looping around maybe
		if(rand==1 and self.x+1<20):
			self.x=self.x+1
		if(rand==2 and self.x-1>-1):
			self.x=self.x-1
		if(rand==3 and self.y+1<20):
			self.y=self.y+1
		if(rand==4 and self.y-1>-1):
			self.y=self.y-1
                board[self.x][self.y].append(self)
		
class Predator:
	def __init__(self,x,y,repro):
                self.x=x
                self.y=y
                self.repro=repro
	def update(self):
                rand=random.randint(1,4) #needs collisions checks.
                board[self.x][self.y].remove(self) #think about modulo looping around maybe
                if(rand==1 and self.x+1<20):
                        self.x=self.x+1
                if(rand==2 and self.x-1>-1):
                        self.x=self.x-1
                if(rand==3 and self.y+1<20):
                        self.y=self.y+1
                if(rand==4 and self.y-1>-1):
                        self.y=self.y-1 
                board[self.x][self.y].append(self)

characters=[]
time_tot=100
dt=0.1
current_t=0
#randomly initalize 10 plants, 5 prey, 2 predators
for i in range(10): #plant=1
	x=random.randint(0, 19)
	y=random.randint(0, 19)
	plant=Plant(x,y)
	characters.append(plant)
	board[x][y].append(plant)

for i in range(5): #prey =2
        x=random.randint(0, 19)
        y=random.randint(0, 19)
        prey=Prey(x,y,3)
        characters.append(prey)	
        board[x][y].append(prey)

for i in range(2):#predator =3
        x=random.randint(0, 19)
        y=random.randint(0, 19)
        predator=Predator(x,y,1)
        characters.append(predator)
        board[x][y].append(predator)


while(current_t<time_tot):
	current_t=current_t+dt
	for i in characters:
		i.update()
	for j in range(20):
		print(board[j])
	print("\n")
