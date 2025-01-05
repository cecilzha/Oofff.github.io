import pygame,sys



def main():
    pygame.init()
    mainsurface=pygame.display.set_mode((800,533))
    UI=pygame.image.load('Ui1.jpg')
    arrow=pygame.image.load("arrow.png")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                #Enter mouse input here
                if key == pygame.K_1:
                    pass

        mainsurface.fill((0,255,255))
        mainsurface.blit(UI,(150,464))
        mainsurface.blit(arrow,(325,430))

        #size of UI is 500W by 69L
        
        pygame.display.update()
main()

            

                



    
                
                
                
                
        

    
    
