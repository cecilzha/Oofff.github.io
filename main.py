import sys,pygame,roomloader
import asyncio

RED=(255,0,0)
#missing hallwayright(lvl2)
#missing Mr.Veech
#missing Ms.Khin

async def start_screen():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 1, 512)

    if sys.platform == 'emscripten':
        pygame.mixer.music.load('mainsong.ogg')
    else:
        pygame.mixer.music.load('mainsong.mp3')
    pygame.mixer.music.play(-1)
    
    mainsurface=pygame.display.set_mode((800,533))
    fonte2=pygame.font.Font('Simon.ttf',20)
    fonte=pygame.font.Font('GypsyCurse.ttf',100)
    
    text=fonte2.render('Press Enter To Start',True,(179,39,20))
    title=fonte.render('YAPOCALYPSE',True,(225,225,225))
    logo = pygame.image.load('logo.png')
    box = pygame.image.load('Bio.png')
    (x,y) = (0,0)
    (deltax,deltay) = (5,5)
    done = False
    
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                if key == pygame.K_RETURN:
                    pygame.mixer.quit()
                    done = True
                    
        x = x+deltax
        y = y +deltay

        if x<=0 or x>=750:
            deltax = -deltax
        if y<=0 or y>=488:
            deltay = -deltay
    
        mainsurface.fill((0,0,0))
        mainsurface.blit(logo,(x,y))
       # mainsurface.blit(box,(250,300))
        mainsurface.blit(text,(300,325))
        mainsurface.blit(title,(180,100))    

        pygame.display.update()
        # await asyncio.sleep(0)


async def main():
    await start_screen()

    pygame.init()
    surface_height = 668
    surface_width = 800
    main_surface = pygame.display.set_mode((surface_width,surface_height))

    UI=pygame.image.load('Ui1.png')
    arrow=pygame.image.load("arrow.png")
    keys_cabinet = pygame.image.load("keys_cabinet.png")
    gas_can = pygame.image.load('gascanicon.jpg')
    

    roomslist = []
    itemlist = []
    imagelist = [keys_cabinet,keys_cabinet,gas_can,keys_cabinet,keys_cabinet]
    
    backbuttonrect = 325,500,150,40

    roomslist=roomloader.loadrooms()
    
    
    currentroomindex=65
        
    currentroom = roomslist[0]
    
    while True:
        await asyncio.sleep(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                currentroomindex=currentroom.clicked(pos,itemlist)

        currentroom=roomslist[currentroomindex]
                
        main_surface.fill((0,0,0))
        currentroom.draw(main_surface)
        
        main_surface.blit(UI,(150,600))
        main_surface.blit(arrow,(325,565))
                          
        if ((4 in itemlist) and (5 in itemlist)) and (6 not in itemlist):
            itemlist.append(6)
            

        for i,item in enumerate(itemlist):
            if item < 5:
                main_surface.blit(imagelist[item],(156+(56*i),615))

        #pygame.draw.rect(main_surface,RED,currentroom.rectlist[0][0][0:4])
        #pygame.draw.rect(main_surface,RED,currentroom.rectlist[0][1][0:4])
        
        pygame.display.flip()
        await asyncio.sleep(0)

if __name__=='__main__':
    asyncio.run(main())
