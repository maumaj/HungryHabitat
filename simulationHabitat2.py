import random
import pygame

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
		self.count = 50
		self.x=x
		self.y=y
		self.repro=repro

	def update(self):
		rand=random.randint(1,4) #needs collisions checks.
		try:
			board[self.x][self.y].remove(self) #think about modulo looping around maybe
		except ValueError:
			return

		if(rand==1 and self.x+1<20):
			self.x=self.x+1
		if(rand==2 and self.x-1>-1):
			self.x=self.x-1
		if(rand==3 and self.y+1<20):
			self.y=self.y+1
		if(rand==4 and self.y-1>-1):
			self.y=self.y-1

		if (len(board[self.x][self.y]) > 0):
			for u in (board[self.x][self.y]):
				if type(u) == Predator:
					print('prey eaten')
					characters.remove(self)
					return
				if type(u) == Plant:
					print('prey eat plant')
					board[self.x][self.y].remove(u)
					characters.remove(u)
					self.count = 50
					board[self.x][self.y].append(self)
					return
				else:
					board[self.x][self.y].append(self)
					self.count -= 1
					return
		else:
			board[self.x][self.y].append(self)

class Predator:

	def __init__(self,x,y,repro):
				self.count = 50
				self.x=x
				self.y=y
				self.repro=repro

	def update(self):
				rand=random.randint(1,4) #needs collisions checks.
				try:
					board[self.x][self.y].remove(self) #think about modulo looping around maybe
				except ValueError:
					return

				if(rand==1 and self.x+1<20):
						self.x=self.x+1
				if(rand==2 and self.x-1>-1):
						self.x=self.x-1
				if(rand==3 and self.y+1<20):
						self.y=self.y+1
				if(rand==4 and self.y-1>-1):
						self.y=self.y-1

				if (len(board[self.x][self.y]) > 0):
					for u in (board[self.x][self.y]):
						if type(u) == Prey:
							board[self.x][self.y].remove(u)
							characters.remove(u)
							self.count = 50
							board[self.x][self.y].append(self)
							return
						else:
							board[self.x][self.y].append(self)
							return
				else:
					board[self.x][self.y].append(self)

characters=[]
time_tot=1000
dt=0.01
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


pygame.init()
screen = pygame.display.set_mode((800,800))
done = False

def draw_background():
	for i in range(0,800,40):
		for j in range(0,800,40):
			r_color = 0 + random.randint(0,60)
			g_color = 60 + random.randint(0,50)
			b_color = 0 + random.randint(0,60)
			pygame.draw.rect(screen, (0,60,0),
					pygame.Rect(i,j,40,40))

while not done:
	for event in pygame.event.get():
		for p in range(1):
			draw_background()
			current_t+=+dt
			for i in characters:
				i.update()
				color = (0,0,0)
				if type(i) == Prey:
					color = (0,0,100,50)
				elif type(i) == Predator:
					color = (100,0,0,50)
				elif type(i) == Plant:
					color = (100,0,100,50)
				pygame.draw.rect(screen,(color),pygame.Rect(i.x * 40,i.y * 40,40,40))
				pygame.display.update()

		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and ((current_t<time_tot)):
			pass
		if event.type == pygame.QUIT:
			done = True
		pygame.display.update()
		pygame.display.flip()

endnum = 0
for j in range(20):
	for i in range(20):
		endnum += len(board[j][i])
print (endnum)
