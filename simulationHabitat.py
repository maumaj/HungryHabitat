import random
#Just some ideas on implementation of simulation
#very object oriented. we could go other directions
w,h = 20, 20
board = [[0 for x in range(w)] for y in range(h)]
print(board)

class Plant:
	def __init__(self,x,y):
		self.x=x
		self.y=y

class Prey:
	def __init__(self,x,y,repro):
		self.x=x
		self.y=y
		self.repro=repro
	def update(self):
		
		
class Predator:
	def __init__(self,x,y,repro):
                self.x=x
                self.y=y
                self.repro=repro

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
	board[x][y]=1

for i in range(5): #prey =2
        x=random.randint(0, 19)
        y=random.randint(0, 19)
        prey=Prey(x,y,3)
        characters.append(prey)	
        board[x][y]=2

for i in range(2):#predator =3
        x=random.randint(0, 19)
        y=random.randint(0, 19)
        predator=Predator(x,y,1)
        characters.append(predator)
        board[x][y]=3


while(current_t<time_tot):
	current_t=current_t+dt
	print(board)
