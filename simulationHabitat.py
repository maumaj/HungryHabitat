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
	def update(self): #add some kind of chance to make new plants in neighboring squares
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
def det_collision(board): #function to find collisions on board and resolve them.
	for i in range(20):
		for j in range(20):
			if(board[i][j].len()>1):
				resolve(board[i][j]) #pass square with >1 object to resolve function
def resolve(square):
	#if prey and predator, prey is removed.
	#if prey and prey, place new prey in adjacent square if you roll above chance to reproduce
	#if predator and predator, place new predator in adjacent square if you roll above chance to reproduce
	#if prey and plant, plant is removed.
	#if predator and plant, do nothing (could also have predators be omnivores)
	#if plant and plant, remove one of them (no need to double)
	return 1

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
		i.update() #each board object ubdates
	
	for j in range(20): #basic output
		print(board[j])
	print("\n")
