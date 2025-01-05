import pygame, os

class Room:

    def __init__(self,roomInfo,roomInfo2=None):

        self.state = 0
        self.index = roomInfo[0]
        self.filename = [roomInfo[1]]
        self.rectlist = [roomInfo[2]]

        if roomInfo2 != None:
            self.filename.append(roomInfo2[1])
            self.rectlist.append(roomInfo2[2])
            
    def clicked(self, mouse_pos,itemlist):

        for rect in self.rectlist[self.state]:

            # mou_pos is mouse coordinate
            if mouse_pos[0] >= rect[0] and mouse_pos[0] <= rect[0] + rect[2]:
                if mouse_pos[1] >= rect[1] and mouse_pos[1] <= rect[1] + rect[3]:
                    
                    if rect[6] == -1:
                        if rect[7] == -1:
                            if rect[5] != -1:
                                self.state=rect[5]
                            return rect[4]
                        else:
                            itemlist.append(rect[7])
                            self.state=rect[5]
                            return rect[4]
                        
                    elif rect[6] in itemlist:
                        self.state = rect[5]
                        if rect[7]!=-1:
                            itemlist.append(rect[7])
                        return rect[4]

                    elif rect[6] not in itemlist:
                        return self.index
                    
                    return rect[4]

        return self.index     

    def draw(self, SCREEN):
        print(os.listdir('/data/data/oofff-main/assets/images/'))
        base = os.path.abspath(os.getcwd())
        image = pygame.image.load(base + "/images/{0}.jpg".format(self.filename[self.state]))
        SCREEN.blit(image,(0,0))

