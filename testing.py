import pygame
from pygame.locals import *
pygame.init()

W, H = 800, 600
WIN = pygame.display.set_mode((W,H))

background = pygame.image.load("stage.png")
background = pygame.transform.scale(background,(W,H))

game_sound = pygame.mixer.music.load("sound.wav")
pygame.mixer.music.play(-1)

def main():

    run = True
    while run:
        WIN.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

if __name__=="__main__":
    main()
