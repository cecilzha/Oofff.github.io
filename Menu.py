import pygame,sys,time


def start_screen():
    pygame.init()
    pygame.font.init()
    mainsurface=pygame.display.set_mode((800,533))
    fonte=pygame.font.SysFont('Neotic',20,True,False)
    text=fonte.render('Press Enter To Start',True,(225,225,225))
    logo = pygame.image.load('logo.png')
    (x,y) = (0,0)
    (deltax,deltay) = (5,5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                if key == pygame.K_RETURN:
                    break
                
            
        
        x = x+deltax
        y = y +deltay

        
        if x<=0 or x>=750:
            deltax = -deltax
        if y<=0 or y>=488:
            deltay = -deltay
        

        mainsurface.fill((0,0,0))
        mainsurface.blit(logo,(x,y))
        mainsurface.blit(text,(325,300))
        

        

        pygame.display.update()
        
start_screen()
main()            
                
                

