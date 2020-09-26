import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
title = pygame.image.load(("./assets/title.png"))
def stillScene(picture,x,y,button):
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: 
				if event.key == button:
					done = True

			
			screen.blit(pygame.transform.scale(picture,(800,600)),(x,y))
			


			pygame.display.flip()


stillScene(title,0,0,pygame.K_SPACE)