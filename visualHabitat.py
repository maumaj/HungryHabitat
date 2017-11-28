import pygame 
import random
import numpy as np
import random

pygame.init()
screen = pygame.display.set_mode((800,800))
done = False

cat = pygame.image.load('cat.png')
position = cat.get_rect()
position = position.move(0,0)

def grass_background(screen, seed):
	
	random.seed(seed)	

	for i in range(0,800,50):
		for j in range(0,800,50):
			r_color = 0 + random.randint(0,60)
			g_color = 60 + random.randint(0,50)
			b_color = 0 + random.randint(0,60)
			pygame.draw.rect(screen, (r_color, g_color, b_color),
				 pygame.Rect(i,j,50,50))

while not done:
	for event in pygame.event.get():
		grass_background(screen,0)
		position = position.move(1,0)
		screen.blit(cat,position)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			#pygame.draw.rect(screen,(100,0,100),pygame.Rect(100,100,500,500)
			
			screen.blit(cat, (600,0))
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			
			screen.blit(cat, (40,40))
		if event.type == pygame.QUIT:
			done = True
	pygame.display.update()
	pygame.display.flip()
