import sys
import pygame

def main():

    pygame.init()

    main_surface = pygame.display.set_mode((800,600))
    image = pygame.image.load("image.jpg").convert()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        main_surface.fill((255,255,255))

        main_surface.blit(image,(0,0))
        
        pygame.display.flip()


if __name__=='__main__':
    main()

