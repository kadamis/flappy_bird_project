import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird - Buttons")

x = 60
y = 60
width = 40
height = 60
vel = 6

run = True

while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x -= vel

	if keys[pygame.K_RIGHT]:
		x += vel

	if keys[pygame.K_UP]:
		y -= vel

	if keys[pygame.K_DOWN]:
		y += vel

	if keys[pygame.K_SPACE]:
		y -= vel

	if keys[pygame.K_ESCAPE]:
		pygame.quit()
		quit()

	win.fill((0,0,0))
	pygame.draw.rect(win, (255,0,0), (x, y, width, height))
	pygame.display.update()

pygame.quit()